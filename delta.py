class BeaconDelta
    def __init__(self, provided_by, previous, provided, current, new_random):
        self.provided_by = provided_by
        self.previous = previous
        self.provided = provided
        self.current = current
        self.new_random = new_random

class ValidatorDelta
    def __init__(self, address,commit_reward, reveal_reward, block_reward, shards_watched):
        self.address = address
        self.commit_reward = commit_reward
        self.reveal_reward = reveal_reward
        self.block_reward = block_reward
        self.shards_watched = shards_watched

class ShardDelta
    def __init__(self, address, added_block, added_validators):
        self.address = address
        self.added_block = added_block
        self.added_validators = added_validators

class TimeBlockDelta
    def __init__(self, beacon_delta, validator_deltas):
        self.beacon_delta = beacon_delta
        self.validator_deltas = validator_deltas