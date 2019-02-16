import fuzzer
import Crypto
from Crypto.PublicKey import RSA
import random

#constants
SIMULATION_EPOCHS = 20
AMAX = 10
EPOCH = 0;

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

    bytes_entropy=bytes(entropy, 'utf-8')
    byte_exponent = (bytes(extend_to_power_of_2(bytearray(bytes_entropy)))) #X**2**T
    modulus = int.from_bytes(byte_exponent, 'big', signed=False) % N

    bytes_entropy = (bytes(str(modulus), "ascii"))
    return str(bytes_entropy, 'utf-8')

# set up beacon and validators

beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(1000)

#stake validators
for validator in validators:
    beacon.stake(validator)

#set up epoch list - each list contains the most up-to-date information for that epoch

shards = [Shard]

epoch_states = a = [None] * (AMAX + SIMULATION_EPOCHS)
for x in range(AMAX):
    epoch_states[x] = fuzzer.fuzzy_string()

for i in range(SIMULATION_EPOCHS):
    random.seed(hash(epoch_states[i]))
    random.shuffle(validators)
    beacon.request_proposals(random)
    for shard in shards:
        shard.request_block(random)
    epoch_states[i+AMAX] = (vdf_calc(beacon.revealed_entropy))
    beacon.reset_proposals()
    for validator in validators:
        beacon.request_proposal_hash(validator)

for i in epoch_states:
    print(i)