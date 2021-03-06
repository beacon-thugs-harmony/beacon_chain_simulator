# Eth 2.0 Beacon Chain Simulation
Implements a prototype and interactive simulation for the sharded pos ethereum 2.0.

## Motivation

The Eth 2.0 Spec is very difficult to understand and we thought making it easier to visualize is one of the most impactful things we could do to drive scalability development forward for the community.

The challenging research task involved pulling together incomplete outlines and disparate sources, including ethresear.ch, presentations from Justin Drake, and the mauve whitepaper from Vitalik.

We are grateful to contribute this very technically challenging solution because we think it will offer benefits to society, by making it cheaper and faster for everyone to use Dapps.

Specifically, the simulation visually shows how the system:
1) Creates N using the One-time RSA Ceremony
2) Generates randomness in the beacon chain
3) Guarantees the system from attackers who want to bias the randomness, and 
4) How the system tries to deter attackers who want to frontrun the random validator selection process
5) Provides randomness to the rest of the system
6) This is used to choose the next block proposer both in the beacon chain and in the shard chains

## Simulation Output

![Beacon Chain Web App Image](Beacon_WebApp.png?raw=true "Beacon Chain Simulation")

## Spec

Built using: https://ethresear.ch/t/minimal-vdf-randomness-beacon/3566
And: https://cdn.hackaday.io/files/10879465447136/Mauve%20Paper%20Vitalik.pdf

## Website

www.beacon-chain.com

## Instructions

Run run.py

### Ethereum 2.0 - Beacon Thugs n Harmony vs Quantstamp, for EthDenver
Team: Richard Ma, Poming Lee, Nathan Frenette, Derek Alia

### Note
We found a _potential_ attack vector to the beacon chain while we were building the simulation. 
a malicious actor can DDoS the validator during their RANDAO slot, between the hash submission and the reveal - and cause them to lose money via the penalty. This shows the value of having a simulation
