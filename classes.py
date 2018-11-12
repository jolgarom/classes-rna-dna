class Rna(str):
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        if not all(symb in 'ACUG' for symb in self.sequence):
            raise Exception('Error: incorrect sequence')

    def gc(self):
        gc_count = self.sequence.count('C') + self.sequence.count('G')
        gc_content = gc_count * 100 / len(self.sequence)
        return round(gc_content, 2)

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 'u').replace('U', 'a').replace('G', 'c').replace('C', 'g')
        return Rna(complement_sequence[::-1].upper())


class Dna(Rna):
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        if not all(symb in 'ACTG' for symb in self.sequence):
            raise Exception('Error: incorrect sequence')

    def transcribe(self):
        return Rna(self.sequence.replace('T', 'U'))

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        return Dna(complement_sequence[::-1].upper())
