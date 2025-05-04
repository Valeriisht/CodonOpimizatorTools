import json
from pathlib import Path

def load_codon_table(organism: str, data_dir: str = "data/codon_table"):
    """Function for codon loading"""

    path = Path(data_dir + f"/{organism}.json")

    with open(path) as f:
        return json.load(f)