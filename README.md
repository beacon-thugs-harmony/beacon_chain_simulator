# Eth 2.0 Beacon Chain Simulation
Implements a simulation for the sharded pos ethereum 2.0.

## Motivation

Implements a simulation for the sharded pos ethereum 2.0.

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

## Spec

Built using: https://ethresear.ch/t/minimal-vdf-randomness-beacon/3566
And: https://cdn.hackaday.io/files/10879465447136/Mauve%20Paper%20Vitalik.pdf

## Website

www.beacon-chain.com

## Application

Use this simulator to visually conceptualize the workings of Eth 2.0

## Instructions

Run simulation.py

## Unit Testing

Run testing.py

## Insights from the Simulation

Calculating the VDF is basically like Proof of Work. 

The difference here with traditional Proof of Work is that the calculation here is deterministic.

(Also, importantly, there's no reward for doing the work - the current design relies on altruistic actors doing it out of goodwill.)

### Ethereum 2.0 - Beacon Thugs n Harmony vs Quantstamp, for EthDenver

