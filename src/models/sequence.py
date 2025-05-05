from abc import ABC, abstractmethod


class Sequence(ABC):
    """Abstract base class for biological sequences

    Args:
        ABC (_type_): Abstract Base Class from abc module

    Methods:
        __len__(self): Returns the length of the biological sequence
        __getitem__(self, key): Allows accessing individual elements or slices of the sequence
        __repr__(self): Returns a string representation of the object
        correct_alphabet(sequence, alphabet): Static method to check  sequence
    """

    def __init__(self, sequence: str, sequence_type: str = None):

        self.sequence = sequence
        self.type = sequence_type

    def __len__(self):
        """Returns the length of the biological sequence

        Returns:
            int: Length of the biological sequence
        """
        return len(self.sequence)

    def __repr__(self):
        """
        Returns a string representation of the object

        Returns:
            str: String representation of the object
        """
        return (
            f"{self.__class__.__name__(self.sequence[:10])}"  # только несколько первых
        )

    @staticmethod
    def correct_alphabet(sequence: str, alphabet: str):
        """
        Static method to check if a sequence
        contains only valid characters from a given alphabet

        Args:
            sequence (str): Biological sequence
            alphabet (str): Valid contain for the biological sequence

        Raises:
            ValueError: If the sequence contains
            characters not present in the alphabet
        """
        return all(letter.upper() in alphabet for letter in sequence)


class DNASequence(Sequence):
    """Initialization of the DNA sequence

    Args:
        Sequence (_type_):
    """

    def __init__(self, sequence):
        super().__init__(sequence, sequence_type="DNA")
        self.alphabet = "ATCG"
        self.sequence = sequence
        self.type = "DNA"
        if not self.correct_alphabet(self.sequence, self.alphabet):
            raise ValueError(f"Invalid nuclein acid in sequence: {self.sequence}")


class AminoAcidSequence(Sequence):
    """Initialization of the amino acid sequence

    Args:
        Sequence (_type_):
    """

    def __init__(self, sequence):
        super().__init__(sequence, sequence_type="PROTEIN")
        self.alphabet = "ACDEFGHIKLMNPQRSTVW"
        self.sequence = sequence
        self.type = "PROTEIN"
        if not self.correct_alphabet(self.sequence, self.alphabet):
            raise ValueError(f"Invalid amino acid in sequence: {self.sequence}")
