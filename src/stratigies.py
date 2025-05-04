from dataclasses import dataclass
from .models import Sequence
from .models.config import OptimizationConfig


class BaseOptimizationStrategy(ABC):
    """Abstract base class for all optimization strategies"""

    @abstractmethod
    def seq_optimize(
        self, sequence: Sequence, codon_table: Dict, params: OptimizationConfig
    ) -> Sequence:

        raise NotImplementedError

    def _validate_sequence(self, sequence: Sequence) -> None:
        """Validate input amino acid sequence"""
        if not isinstance(sequence, Sequence):
            raise TypeError("Input must be a Sequence object")
        if not sequence.value:
            raise ValueError("Sequence cannot be empty")


class MaxFrequencyStrategy(BaseOptimizationStrategy):
    """Optimize only by frequency"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: Dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table"""

        self._validate_sequence(sequence)

        dna_seq = []
        for aa in sequence.value:
            best_codon = max(codon_table[aa].items(), key=lambda x: x[1])[0]
            dna_seq.append(best_codon)

        return Sequence("".join(dna_seq))


class WithGCStrategy(BaseOptimizationStrategy):
    """Optimize by frequency and gc-content"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: Dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table"""

        dna_seq = []
        self._validate_sequence(sequence)

        optimized_codons = self._find_gc_codon(
            sequence.value, codon_table, params.gc_target
        )

        if not optimized_codons:
            raise ValueError("Could not find solution with required GC content")

        return Sequence("".join(optimized_codons), sequence_type="DNA")

    # требует глубокого осмысления - надо продумать бэктреккинг
    def _find_gc_codon(self, amino_acids: str, codon_table: Dict, target_gc_bases: int):
        """Finding a combination of codons that satisfies GC requirements

        Backtraining with pruning:
        1. The most frequently occurring
        2. Them pathways that cannot reach the target GC are discarded"""
        # через рекурсию тут пробовать
        pass


class CAIOptimizationStrategy(BaseOptimizationStrategy):
    """Optimize codons based on Codon Adaptation Index (CAI)"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: Dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table"""

        self._validate_sequence(sequence)

        weight = self._calculate_weight(codon_table)

        dna_seq = []
        for aa in sequence.value:
            best_codon = max(codon_table[aa].items(), key=lambda x: weight[x[0]])
            dna_seq.append(best_codon)

        return Sequence("".join(dna_seq), sequence_type="DNA")

    # определяем предпочтительные кодоны
    def _calculate_weight(self, codon_table):
        """Calculate adaptiveness (weight) for each codon"""
        weight_values = {}

        # It is  maximum frequency for each amino acid
        max_freq = {aa: max(freqs.values()) for aa, freqs in codon_table.items()}

        for aa, codons in codon_table.items():
            for codon, freq in codons.items():
                weight_values[codon] = freq / max_freq[aa]

        return weight_values


# хорошо бы еще реализовать стратегию с повторами

# class RepeatStrategy


class OptimizationStrategy(self):
    """Choose strayegy"""

    STRATEGIES = {
        "frequency": MaxFrequencyStrategy,
        "cai": CAIOptimizationStrategy,
    }

    def __init__(self, params: OptimizationConfig):
        self.strategy = self._get_strategy(params.strategy_name)
        self.params = params

    def _get_strategy(name):
        strategy = self.STRATEGIES.get(name)
        if not strategy:
            raise ValueError("Invalid strategy name")
        return strategy()
