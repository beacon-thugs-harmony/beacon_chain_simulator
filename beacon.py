import validator_pool
import stake

class Beacon(object):
    def __init__(self, address):
        self.address = address
        self.validator_pool = validator_pool.ValidatorPool()
        self.stakes = []

    def stake(self, validator):
    	if(validator.address.balance<32):
    		return False;
    	self.validator_pool.add(validator);
    	self.stakes.append(stake.Stake(self.address,validator.address));
    	return True;