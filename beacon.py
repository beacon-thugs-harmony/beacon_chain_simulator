import validator_pool

class Beacon(object):
    def __init__(self, address):
        self.address = address
        self.validator_pool = validator_pool.ValidatorPool()
        self.stakes = []
        self.entropy = fuzzer.fuzzy_string()

    def stake(self, validator):
        if(validator.address.balance<32):
            return False
        self.validator_pool.add(validator)
        self.address.balance +=32
        validator.address.balance-=32
        return True

    def request_proposal(self):
        # get random validator
        # ask random validator to propose a block