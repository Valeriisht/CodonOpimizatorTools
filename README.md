## Codon-optimization Tool

- This tool has been developed for the codon-optimization of DNA sequences with the objective of maximising protein expression.

## Content
- [System specifications](#system-specifications)
- [Installation](#Installation)
- [Testing](#Testing)
- [Contributing](#Contributing)

## Installation

To get the tool clone the git repository:

```sh
git clnone git@github.com:Valeriisht/CodonOpimizatorTools.git
```
Create a conda environment with the necessary packages. 
Activate it: requirements.txt

## Usage

Parameters in config 

## Implemented strategies

- Frequency strategy (ready) - selection of the most frequent codons
- CAI strategy (ready) - optimization based on codon adaptation index
- GC strategy (in development) - optimization based on GC-composition

⚠️ GC-strategy in the current version is under active development.

About architecture of tools you can find out in design.md 

## Examples of working

For yeast - "protein = "GIVEQCCTSICSLYQLENYCN" 

```2025-05-05 19:15:19.495 | INFO     | __main__:main:30 - Starting main function
2025-05-05 19:15:19.495 | INFO     | __main__:main:33 - Inizialization of CodonOptimizator
2025-05-05 19:15:19.495 | INFO     | src.optimizer:optimize:34 - The Sequence is created
2025-05-05 19:15:19.495 | INFO     | src.strategies:seq_optimize:46 - Checking Sequence in MaxFrequencyStrategy
2025-05-05 19:15:19.495 | INFO     | __main__:main:39 - Success of CodonOptimizator working
2025-05-05 19:15:19.495 | INFO     | __main__:main:40 - Ending main function
Optimization Sequence : GGTATTGTTGAACAATGTTGTACTTCTATTTGTTCTTTGTATCAATTGGAAAATTATTGTAAT, type: DNA```

## Testing

Three types of tests: unit tests, integration tests, and generation tests cover the project.
Processsing...

To run it, execute the command:

```
python main.py

```
