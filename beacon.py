import validator_pool
import fuzzer
import random
import utils

class Beacon(object):
    def __init__(self, address):
        self.address = address
        self.validator_pool = validator_pool.ValidatorPool()
        self.stakes = []
        self.revealed_entropy = fuzzer.zero_string()
        self.proposers = []
        self.proposal_hashes = []

    def stake(self, validator):
        if(validator.address.balance<32):
            return False
        self.validator_pool.add(validator)
        self.address.balance +=32
        validator.address.balance-=32
        return True

    def request_single_proposal(self):
        if(len(self.proposal_hashes) == 0):
            return
        # get the randomly selected validator        
        selected_validator = random.choice(self.validator_pool.validators)
        # ask the random validator to propose a block
        if(selected_validator.propose()):
            entropy = selected_validator.get_entropy()
            if(self.proposal_hashes[0] == str(hash((entropy)))):
                self.revealed_entropy = utils.xor(self.revealed_entropy,entropy)        
            else:
                pass #will include punishment here
        else:
            pass #will include punishment here
              
        del self.proposal_hashes[0]

    def request_proposal_hash(self, validator):
        self.proposal_hashes.append(validator.get_entropy_hash())

    def assign_validators(self,shard, validators):
        #STUB
        shard.validators = validators[0:255]
        return
