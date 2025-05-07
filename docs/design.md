# The architecture of the project CodonOptimizator

This tool is designed for the codon-optimization of DNA sequences, with the aim of maximising protein expression.

 The tool is composed of the following main components:

1. **Main optimization component** - Codon optimization algorithms
2. **Optimization Strategies** - Optimization modules
3. **Data** - Tables of codons and frequencies of their occurrence in producer organisms
4. **Interfaces** - CLIs file

- The tool is written using classes (OOP Concept). Perhaps some principles of code organisation will be considered and improved in the next version of the program.

### The structure of repo 

```bash
├── cli.py
├── data
│   └── codon_table
│       ├── e_coli.json
│       └── yeast.json
├── docs
│   └── design.md
├── errors_logs.log
├── main.py
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── load_codon
│   ├── models
│   │   ├── __init__.py
│   │   └── sequence.py
│   ├── optimizer.py
│   └── strategies.py
└── tests
    ├── integration_tests
    └── unit_tests
```
