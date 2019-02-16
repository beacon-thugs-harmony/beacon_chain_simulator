import fuzzer
import Crypto
from Crypto.PublicKey import RSA
import random

#constants
SIMULATION_EPOCHS = 20
AMAX = 10
EPOCH = 0;
>>>>>>> 5dfe8c55b0eac58d1bd2d2c99a876e402dbfdfb2
# create 2048 bit RSA modulus using a secure ceremony
key = RSA.generate(2048)
N = key.n # N is used for VDF creation

print(key.n)
print(key.n.bit_length())

def randao_mix(beacon):

def vdf_calc(entropy):
    #The VDF should be calculated as Y = X**(2**T) % N
    #For the simulation - we'll use the VDF_DELAY constant to specify how many epochs this calculation takes
    return (entropy)

# set up beacon and validators

print(fuzzer.fuzzy_number_function()())
beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(1000)

#stake validators
for validator in validators:
    beacon.stake(validator)

#set up epoch list - each list contains the most up-to-date information for that epoch

epoch_states = a = [None] * (AMAX + SIMULATION_EPOCHS)
for x in range(AMAX):
    epoch_states[x] = fuzzer.fuzzy_string()

for i in range(SIMULATION_EPOCHS):
    random.seed(hash(epoch_states[i]))
    random.shuffle(validators)
    #In each epoch, first do the randao mixing, and then calculate the vdf
    for j in beacon.proposers:
        beacon.request_proposal(validators[j])
    epoch_states[i+AMAX] = (vdf_calc(beacon.revealed_entropy))
    beacon.reset_proposals()
    for j in range(128):
        beacon.request_proposal_hash(validators[j])
