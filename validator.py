import fuzzer
import random

class Validator:
    #Honesty, bias, availability will be 0-1, 1 being 'good'
    def __init__(self, address, honesty, availability, bias):
        self.address = address;
        self.honesty = honesty;
        self.availability = availability;
        self.bias = bias;
        self.current_entropy = fuzzer.fuzzy_string();

    def availiable(self):
        return random.random() < self.availability()

    def get_entropy(self):
        return self.current_entropy

    def get_entropy_hash(self):
        self.current_entropy = fuzzer.fuzzy_string()
        return str(hash(self.current_entropy))