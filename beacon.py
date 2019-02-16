import validator_pool
import fuzzer

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

    def request_proposal(self, validator):
        # ask random validator to propose a block
        if(validator.propose()):
            entropy = validator.get_entropy()
            if(self.propsal_hashes[validator.address] == str(hash((entropy)))):
                self.revealed_entropy = self.revealed_entropy^validator.get_entropy()
            else:
                pass #will include punishment here

    def reset_proposals(self):
        self.propsers = []

    def request_proposal_hash(self, validator):
        self.proposal_hashes[validator.address] = (validator.get_entropy_hash())
