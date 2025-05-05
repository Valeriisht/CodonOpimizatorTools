from dataclasses import dataclass
from .models import Sequence
from .config import OptimizationConfig
from abc import ABC, abstractmethod
from loguru import logger


class BaseOptimizationStrategy(ABC):
    """Abstract base class for all optimization strategies"""

    @abstractmethod
    def seq_optimize(
        self, sequence: Sequence, codon_table: dict, params: OptimizationConfig
    ) -> Sequence:

        raise NotImplementedError

    def _validate_sequence(self, sequence: Sequence) -> None:
        """Validate input amino acid sequence"""
        if not isinstance(sequence, Sequence):
            raise TypeError("Input must be a Sequence object")
        if not sequence.sequence:
            raise ValueError("Sequence cannot be empty")


class MaxFrequencyStrategy(BaseOptimizationStrategy):
    """Optimize only by frequency"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table

        Args:
            sequence (Sequence):
            codon_table (dict):
            params (OptimizationConfig):

        Raises:
            ValueError: Invalid AminoAcid

        Returns:
            Sequence: optimization DNA sequence
        """

        self._validate_sequence(sequence)
        logger.info("Checking Sequence in MaxFrequencyStrategy")

        dna_seq = []
        for aa in sequence.sequence:
            if aa not in codon_table:
                raise ValueError(f"Invalid AminoAcid {aa}")

            best_codon = max(codon_table[aa].items(), key=lambda x: x[1]["frequency"])[
                0
            ]
            dna_seq.append(best_codon)

        return Sequence("".join(dna_seq), sequence_type="DNA")


class WithGCStrategy(BaseOptimizationStrategy):
    """Optimize by frequency and gc-content"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table

        Args:
            sequence (Sequence):
            codon_table (dict):
            params (OptimizationConfig):

        Raises:
            ValueError: Invalid AminoAcid

        Returns:
            Sequence: optimization DNA sequence
        """
        logger.warning(
            "You are using GC strategy which is under development. "
            "For production use, consider 'frequency' or 'cai' strategies."
        )

        dna_seq = []
        self._validate_sequence(sequence)

        logger.info("Checking Sequence in WithGCStrategy")

        optimized_codons = self._find_gc_codon(
            sequence.sequence, codon_table, params.gc_target
        )

        if not optimized_codons:
            raise ValueError("Could not find solution with required GC content")

        return Sequence("".join(optimized_codons), sequence_type="DNA")

    # требует глубокого осмысления - надо продумать бэктреккинг
    def _find_gc_codon(self, amino_acids: str, codon_table: dict, target_gc_bases: int):
        """Finding a combination of codons that satisfies GC requirements

        Backtraining with pruning:
        1. The most frequently occurring
        2. Them pathways that cannot reach the target GC are discarded"""
        # через рекурсию тут пробовать
        pass


class CAIOptimizationStrategy(BaseOptimizationStrategy):
    """Optimize codons based on Codon Adaptation Index (CAI)"""

    def seq_optimize(
        self, sequence: Sequence, codon_table: dict, params: OptimizationConfig
    ) -> Sequence:
        """Converts protein sequence to DNA using codon table

        Args:
            sequence (Sequence):
            codon_table (dict):
            params (OptimizationConfig):

        Raises:
            ValueError: Invalid AminoAcid

        Returns:
            Sequence: optimization DNA sequence
        """

        self._validate_sequence(sequence)

        logger.info("Checking Sequence in CAIOptimizationStrategy")

        weight = self._calculate_weight(codon_table)

        logger.info("Calculate weight")

        dna_seq = []

        for aa in sequence.sequence:
            if aa not in codon_table:
                raise ValueError(f"Invalid AminoAcid {aa}")

            codons_for_aa = codon_table[aa]  # все кодоны для вот этой аминокислоты

            best_codon = max(codons_for_aa.items(), key=lambda x: weight[x[0]])[
                0
            ]  # нужен ключ
            dna_seq.append(best_codon)

        return Sequence("".join(dna_seq), sequence_type="DNA")

    # определяем предпочтительные кодоны
    def _calculate_weight(self, codon_table):
        """Calculate adaptiveness (weight) for each codon"""
        weight_values = {}

        # It is  maximum frequency for each amino acid
        max_freq = {
            aa: max(freqs.values(), key=lambda x: x["frequency"])["frequency"]
            for aa, freqs in codon_table.items()
        }

        for aa, codons in codon_table.items():
            for codon, freq in codons.items():
                weight_values[codon] = freq["frequency"] / max_freq[aa]

        return weight_values


# хорошо бы еще реализовать стратегию с повторами

# class RepeatStrategy

# упрощю - как-будто излишне - хотя как паттерн проективрования - фабрика - может быть стоило усовершенствовать
# class OptimizationStrategy():
#     """Choose strategy"""

#     STRATEGIES = {
#         "frequency": MaxFrequencyStrategy,
#         "cai": CAIOptimizationStrategy,
#     }

#     def __init__(self, params: OptimizationConfig):
#         self.strategy = self._get_strategy(params.strategy_name)
#         # сразу стратегию оптимизации запускаем (может проще через функцию организовать?)

#     def _get_strategy(self, name):
#         strategy = self.STRATEGIES.get(name) # вытаскиваем стратегию
#         if not strategy:
#             raise ValueError("Invalid strategy name")
#         return strategy()


def get_optimization_strategy(
    name: str, sequence: Sequence
) -> BaseOptimizationStrategy:
    """Choosing of strategy"""

    strategies = {
        "frequency": MaxFrequencyStrategy(),
        "cai": CAIOptimizationStrategy(),
    }

    return strategies.get(name, MaxFrequencyStrategy())  # по умолчанию макс оставим
