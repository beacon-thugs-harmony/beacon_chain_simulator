import fuzzer
import Crypto
from Crypto.PublicKey import RSA
import random
import shard

#constants
SIMULATION_EPOCHS = 3
AMAX = 10
EPOCH = 0
NSHARDS = 4

# create 2048 bit RSA modulus using a secure ceremony
key = RSA.generate(2048)
N = key.n # N is used for VDF creation

print("The RSA Random N is:\n" + str(key.n) +"\n")

def next_power_of_2(x):
    return x if x == 1 else next_power_of_2((x+1) // 2) * 2

def extend_to_power_of_2(bytez):
    return bytez + b'\x00' * (next_power_of_2(len(bytez)) - len(bytez))

def vdf_calc(entropy):
    #The VDF should be calculated as Y = X**(2**T) % N, here we use T=1 to reduce simulation runtime
    #The AMAX constant specifies how many epochs this calculation takes on ASIC chips

    bytes_entropy=bytes(entropy, "ascii")
    bytes_entropy = (bytes(extend_to_power_of_2(bytearray(bytes_entropy)))) #X**2**T
    bytes_entropy = ((int.from_bytes(bytes_entropy, 'big', signed=False) % N).to_bytes(32, byteorder='big')) #take the modulus by N

    return str(bytes_entropy, "ascii")

# set up beacon and validators

beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(1000)

#stake validators
for validator in validators:
    beacon.stake(validator)

#set up epoch list - each list contains the most up-to-date information for that epoch

shards = [None]*NSHARDS
for i in range(len(shards)):
    shards[i] = shard.Shard()

epoch_states = a = [None] * (AMAX + SIMULATION_EPOCHS)
for x in range(AMAX):
    epoch_states[x] = fuzzer.fuzzy_string()

for i in range(SIMULATION_EPOCHS * 128):
    if(i%128==0):
        epoch = i // 128
        random.seed(hash(epoch_states[epoch]))
        random.shuffle(validators)  # shuffle proposals for entropy
        beacon.request_proposals(random)
        epoch_states[epoch+AMAX] = (vdf_calc(beacon.revealed_entropy))

        for validator in validators:
            beacon.request_proposal_hash(validator)

        for unique_shard in shards:
            random.shuffle(validators)  # validator shard assignment
            beacon.assign_validators(unique_shard,validators)
            unique_shard.request_block() # print validator x is proposing block at slot n

for i in epoch_states:
    print(i)
