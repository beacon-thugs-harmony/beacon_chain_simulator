import fuzzer

#create 2048 bit RSA modulus using a secure ceremony

print(fuzzer.fuzzy_number_function()())
beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(100)
for validator in validators:
    beacon.stake(validator)

while(true):
    for i in range(128):
        beacon.request_proposal()
    verifiable_delay_function(beacon.entropy) #evaluator
    #VDF output is used to select propsers

