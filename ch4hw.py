file = open("input.txt")
output = open("trimmed.txt","w")
for dna in file:
    trimmed_dna = dna [14:]
    output.write(trimmed_dna)
    print str(len(trimmed_dna))
    
    
genomic_dna = open ("genomic_dna.txt").read()
exon_locations = open("exons.txt")
coding_sequence = ""
for line in exon_locations:
    positions = line.split(",")
    start = int(positions[0])
    stop = int(positions[1])
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
