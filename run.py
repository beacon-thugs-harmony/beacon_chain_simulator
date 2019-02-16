import fuzzer
import Crypto
from Crypto.PublicKey import RSA

#constants
SIMULATION_EPOCHS = 20
VDF_DELAY = 10

# create 2048 bit RSA modulus using a secure ceremony
key = RSA.generate(2048)
N = key.n # N is used for VDF creation

print(key.n)
print(key.n.bit_length())


def randao_mix(beacon):
    #STUB

def vdf_calc(entropy):
    #The VDF should be calculated as Y = X**(2**T) % N
    #For the simulation - we'll use the VDF_DELAY constant to specify how many epochs this calculation takes
    return (VDF_DELAY)

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

    for j in range(128):
        beacon.request_proposal()

    #In each epoch, first do the randao mixing, and then calculate the vdf
    beacon.entropy = randao_mix(beacon)

    [epochs_delayed,beacon.entropy] = vdf_calc(beacon.entropy) #evaluator
    #VDF output is used to select proposers

