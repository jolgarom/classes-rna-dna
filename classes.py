class Rna(str):
    sequence = ''
    
    def __init__(self, sequence):
        if isinstance(self.sequence, str):
            self.sequence = sequence.upper()
        else:
            raise TypeError
            
    def gc(self):
        gc_count = self.sequence.count('C') + self.sequence.count('G')
        gc_content = gc_count * 100 / len(self.sequence)
        return round(gc_content, 2)

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 'u').replace('U', 'a').replace('G', 'c').replace('C', 'g')
        complement_sequence = complement_sequence.upper()
        return complement_sequence[::-1]


class Dna(Rna):
    def __init__(self, sequence):
        if isinstance(self.sequence, str):
            self.sequence = sequence.upper()
        else:
            raise TypeError

    def transcribe(self):
        return self.sequence.replace('T', 'U')

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        complement_sequence = complement_sequence.upper()
        return complement_sequence[::-1]
