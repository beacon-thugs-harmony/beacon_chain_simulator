import fuzzer


print(fuzzer.fuzzy_string())
print(fuzzer.fuzzy_number_function()())
beacon = fuzzer.fuzzy_beacon()
validators = fuzzer.create_validators(100)
for validator in validators:
    beacon.stake(validator)
