from .models.sequence import Sequence, AminoAcidSequence
from .config import OptimizationConfig
from .load_codon.CodonTable_loader import load_codon_table
from .strategies import get_optimization_strategy
from loguru import logger


class CodonOptimizator:
    """Class for sequence optimization"""

    def __init__(self, params: OptimizationConfig = None):

        self.params = params or OptimizationConfig()
        self.codon_table = load_codon_table(self.params.organism)

        if not self.codon_table:
            available = ", ".join(self._find_available_organisms())
            raise ValueError(
                f"No codon table found for organism: {self.params.organism}. "
                f"Available organisms: {available}"
            )

    def optimize(self, input_sequence: str) -> Sequence:
        """Input Sequence Optimisation

        Args: Input_sequence: Amino acid sequence

        Returns: Optimised Sequence object
        """
        try:

            sequence = Sequence(input_sequence)

            logger.info("The Sequence is created")

            strategy = get_optimization_strategy(self.params.strategy_name, sequence) 

            return strategy.seq_optimize( # у каждой стратегии методот должен быть реализован - суть наследования от абстрактного класса
                sequence=sequence,
                codon_table=self.codon_table,
                params=self.params
            )
 

        except Exception as e:
            raise ValueError(f"CodonOptimizator failed: {str(e)}")

    def _find_available_organisms(self) -> list[str]:
        """Helper to list available organisms (implementation depends on your loader)."""
        return ["e_coli", "yeast"]
    

