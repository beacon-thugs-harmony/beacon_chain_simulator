# Eth 2.0 Beacon Chain Simulation
> Implements a simulation for the sharded pos ethereum 2.0.

## Spec
Built using: https://ethresear.ch/t/minimal-vdf-randomness-beacon/3566

## Motivation

The Eth 2.0 Spec is very difficult to understand, even for experienced developers. 
It starts with a list of assumptions and then makes the some statements immediately, without fleshing out why it works (or doesn't work).

We decided to make it easier for the community to understand, by building a live simulation from the most recent beacon chain spec.

This helps to get more people able to contribute to the scalability development.

It also meant gathering information from incomplete, disparate sources, including github repos, ethresear.ch, youtube videos, and the mauve whitepaper from Vitalik, and basically bashed our heads against the wall until we understood how it worked. 

Specifically, the simulation visually shows how the system:
1) Creates N using the One-time RSA Ceremony
2) Generates randomness in the beacon chain
3) Guarantees the system from attackers who want to bias the randomness, and 
4) How the system tries to deter attackers who want to frontrun the random validator selection process
5) Provides randomness to the rest of the system
6) This is used to choose the next block proposer both in the beacon chain and in the shard chains

## Application
Use this simulator to visually conceptualize the workings of Eth 2.0

## Instructions

Run simulation.py

## Unit Testing

Run testing.py

## Simulation Output

Put image from the simulation output here

## Insights from the Simulation

Calculating the VDF is basically like Proof of Work. 

The difference here with traditional Proof of Work is that the calculation here is deterministic.

(Also, importantly, there's no reward for doing the work - the current design relies on altruistic actors doing it out of goodwill.)

##Contribution to Ethereum 2.0 from the Beacon Thugs n Harmony vs. Quantstamp

