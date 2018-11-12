def gc(self):
    gc_count = self.sequence.count('C') + self.sequence.count('G')
    gc_content = gc_count * 100 / len(self.sequence)
    return round(gc_content, 2)


class Dna:
    sequence = ''
    gc = gc

    def __init__(self, sequence):
        if isinstance(self.sequence, str):
            self.sequence = sequence.upper()
        else:
            raise TypeError

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        complement_sequence = complement_sequence.upper()
        return complement_sequence[::-1]


class Rna(Dna):
    def __init__(self, sequence_object):
        if isinstance(sequence_object, Dna):
            self.__transcribe_dna(sequence_object.sequence)
        elif isinstance(sequence_object, str):
            self.sequence = sequence_object.upper()
        else:
            raise TypeError

    def __transcribe_dna(self, sequence):
        self.sequence = sequence.replace('T', 'U')

    def reverse_complement(self):
        complement_sequence = self.sequence.replace('A', 'u').replace('U', 'a').replace('G', 'c').replace('C', 'g')
        complement_sequence = complement_sequence.upper()
        return complement_sequence[::-1]