from hashlib import blake2b


def hash(x):
    return blake2b(x).digest()[:32]

def lmd_ghost(store, start):
    validators = start.state.validator_registry
    active_validators = [validators[i] for i in
                         get_active_validator_indices(validators, start.state.slot)]
    attestation_targets = [get_latest_attestation_target(store, validator)
                           for validator in active_validators]
    def get_vote_count(block):
        return len([target for target in attestation_targets if
                    get_ancestor(store, target, block.slot) == block])

    head = start
    while 1:
        children = get_children(head)
        if len(children) == 0:
            return head
        head = max(children, key=get_vote_count)
