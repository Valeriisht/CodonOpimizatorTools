from .models import Sequence
from .config import OptimizationConfig
from .codontable_load import CodonTable_loader
from .strategies import OptimizationStrategy


class CodonOptimizator:
    """Class for sequence optimization"""

    def __init__(self, params: OptimizationConfig = None):

        self.params = params or OptimizationConfig()
        self.codon_table = CodonTable_loader(self.params.organism)
        self.strategy = OptimizationStrategy(self.params.strategy_name)

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
            return self.strategy.optimize(
                sequence=sequence, codon_table=self.codon_table, params=self.params
            )

        except Exception as e:
            raise ValueError(f"Optimization failed: {str(e)}")

    def _find_available_organisms(self) -> list[str]:
        """Helper to list available organisms (implementation depends on your loader)."""
        # Реализация зависит от вашего CodonTable_loader
        return ["e_coli", "yeast"]
