from .models.sequence import Sequence, AminoAcidSequence
from .config import OptimizationConfig
from .load_codon.CodonTable_loader import load_codon_table
from .strategies import OptimizationStrategy


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

            return OptimizationStrategy(sequence, self.params)
            
            

        except Exception as e:
            raise ValueError(f"Optimization failed: {str(e)}")

    def _find_available_organisms(self) -> list[str]:
        """Helper to list available organisms (implementation depends on your loader)."""
        return ["e_coli", "yeast"]
    

protein = AminoAcidSequence("MAKEPEPTIDE")
