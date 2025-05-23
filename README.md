# Codon-optimization Tool

<img align=right src="https://github.com/user-attachments/assets/86306224-642a-4b98-a3b5-045a5f8444ba" alt="# Codon-optimization Tool" width="100"/>

- A bioinformatics tool has been developed for the codon-optimization of DNA sequences with the objective of maximising protein expression.


## Content
- [Installation](#Installation)
- [Usage](#Usage)
- [Implemented strategies](#implemented-strategies)
- [Examples](#examples-of-working)
- [Testing](#Testing)
- [Contributing](#Contributing)

## Installation

To get the tool clone the git repository:

```sh
git clone git@github.com:Valeriisht/CodonOpimizatorTools.git
```
Create a conda environment with the necessary packages. 

Activate it: requirements.txt

```
conda create -n codon_opt python=3.11
conda activate codon_opt
pip install -r requirements.txt
```

## Usage

Parameters in config. In order to start the programme, please specify the necessary parameters in the config file. 

You can start the programme in the following way

``` 
python main.py
```

The ability to work with the script from the command line (cli.py) will be added soon.
(*Note: Command line interface (CLI) version coming soon.*)

## Implemented strategies

- Frequency strategy (ready) - selection of the most frequent codons (#freguency)
- CAI strategy (ready) - optimization based on codon adaptation index (#cai)
- GC strategy (in development) - optimization based on GC-composition

⚠️ GC-strategy in the current version is under active development.

About architecture of tool you can find out in [design.md](https://github.com/Valeriisht/CodonOpimizatorTools/blob/main/docs/design.md)

## Examples of working

For yeast - "protein = "GIVEQCCTSICSLYQLENYCN"  - it's one of insulin chain (not pre-pro - as example)

```
2025-05-05 19:15:19.495 | INFO     | __main__:main:30 - Starting main function
2025-05-05 19:15:19.495 | INFO     | __main__:main:33 - Inizialization of CodonOptimizator
2025-05-05 19:15:19.495 | INFO     | src.optimizer:optimize:34 - The Sequence is created
2025-05-05 19:15:19.495 | INFO     | src.strategies:seq_optimize:46 - Checking Sequence in MaxFrequencyStrategy
2025-05-05 19:15:19.495 | INFO     | __main__:main:39 - Success of CodonOptimizator working
2025-05-05 19:15:19.495 | INFO     | __main__:main:40 - Ending main function

Optimization Sequence : GGTATTGTTGAACAATGTTGTACTTCTATTTGTTCTTTGTATCAATTGGAAAATTATTGTAAT, type: DNA
```

For *e_coli* - "protein = "MAKLEHISTVQWRNDYFCPG" (cai startegy)

```
2025-05-15 19:12:22.203 | INFO     | __main__:main:34 - Starting main function
2025-05-15 19:12:22.234 | INFO     | __main__:main:37 - Inizialization of CodonOptimizator
2025-05-15 19:12:22.234 | INFO     | src.optimizer:optimize:34 - The Sequence is created
2025-05-15 19:12:22.235 | INFO     | src.strategies:seq_optimize:133 - Checking Sequence in CAIOptimizationStrategy
2025-05-15 19:12:22.235 | INFO     | src.strategies:seq_optimize:137 - Calculate weight
2025-05-15 19:12:22.235 | INFO     | __main__:main:43 - Success of CodonOptimizator working
2025-05-15 19:12:22.235 | INFO     | __main__:main:44 - Ending main function

Optimization Sequence : ATGGCAAAACTGGAACATATTAGCACCGTTCAGTGGCGTAATGATTATTTTTGTCCGGGT, type: DNA
```

## Testing

Three types of tests: unit tests, integration tests, and generation tests cover the project.

Processsing of realization...

## Contributing

Contributions are welcome!

Please:

1) Fork the repository
2) Create a feature branch
3) Submit a pull request




