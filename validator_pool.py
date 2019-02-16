import validator

class ValidatorPool:

    def __init__(self):
        self.validators = [];

    def add(self,validator):
        self.validators.append(validator);

    def remove(self,validator_address):
        filtered_validators = []
        for validator in validators:
            if(validator.address != validator_address):
                filtered_validators.append(validator)
        self.validators = filtered_validators
