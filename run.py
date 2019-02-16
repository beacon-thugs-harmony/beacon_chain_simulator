import fuzzer
import Crypto
from Crypto.PublicKey import RSA

#constants
SIMULATION_EPOCHS = 20

# create 2048 bit RSA modulus using a secure ceremony
key = RSA.generate(2048)
N = key.n # N is used for VDF creation

print(key.n)
print(key.n.bit_length())

def randao_mix():
    #STUB

def vdf_calc():
    #STUB


# set up beacon and validators

print(fuzzer.fuzzy_number_function()())
beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(1000)

#stake validators
for validator in validators:
    beacon.stake(validator)

#set up epoch list - each list contains the most up-to-date information for that epoch
epoch_states = []


for i in range(SIMULATION_EPOCHS):
    #In each epoch, first do the randao mixing, and then calculate the vdf
    randao_out = randao_mix()

    for i in range(128):
        beacon.request_proposal()
    vdf_calc(beacon.entropy) #evaluator
    #VDF output is used to select proposers

