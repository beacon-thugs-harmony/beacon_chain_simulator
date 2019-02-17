import validator_pool
import fuzzer
import utils


class Beacon(object):
    def __init__(self, address):
        self.address = address
        self.validator_pool = validator_pool.ValidatorPool()
        self.stakes = []
        self.revealed_entropy = fuzzer.fuzzy_string()
        self.proposers = []
        self.proposal_hashes = {}

    def stake(self, validator):
        if(validator.address.balance<32):
            return False
        self.validator_pool.add(validator)
        self.address.balance +=32
        validator.address.balance-=32
        return True

    def request_proposals(self, random):
        # ask random validator to propose a block
        keys = list(self.proposal_hashes.keys())
        if(len(keys) == 0):
            return
        random.shuffle(keys)
        for i in range (128):
            validator = self.validator_pool.get_validator(keys[i%len(keys)])
            if(validator.propose()):
                entropy = validator.get_entropy()
                if(self.proposal_hashes[validator.address] == str(hash((entropy)))):
                    self.revealed_entropy = utils.xor(self.revealed_entropy,entropy)
                else:
                    pass #will include punishment here
        self.proposal_hashes = {}

    def request_proposal_hash(self, validator):
        self.proposal_hashes[validator.address] = validator.get_entropy_hash()

    def assign_validators(self,shard, validators):
        #STUB
        shard.validators = validators[0:255]
        return
