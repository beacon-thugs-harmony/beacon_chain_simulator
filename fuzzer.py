import random
import string
import validator
import validator_pool
import beacon
import honesty
import address

random.seed(10)

def fuzzy_string():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32));

def fuzzy_number():
    return random.random();

def fuzzy_number_function():
    return random.random

def honest_available_unbiased():
    return lambda:1

def fuzzy_beacon():
    return beacon.Beacon(empty_address())

def empty_address():
    return address.Address(fuzzy_string(),0)

def fuzzy_address():
    return address.Address(fuzzy_string(),random.random()*64)

def good_address():
    return address.Address(fuzzy_string(),1000)

def fuzzy_validator():
    return validator.Validator(fuzzy_address(),fuzzy_number_function(),fuzzy_number_function(),fuzzy_number_function())

def good_validator():
    return validator.Validator(good_address(),honest_available_unbiased(),honest_available_unbiased(),honest_available_unbiased());

def fuzzy_validator_pool():
    return validator_pool.ValidatorPool();

def create_validators(num_validators):
    validators = [];
    for x in range(num_validators):
        validators.append(good_validator())
    return validators

def create_fuzzy_validators(num_validators):
    validators = [];
    for x in  range(num_validators):
        validators.append(fuzzy_validator())
    return validators