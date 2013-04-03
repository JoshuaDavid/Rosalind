dnaProblem = open('./rosalind_dna.txt').read()
dnaSample = open('./rosalind_sample_dna.txt').read()
# newline at EOF
outputSample = open('./rosalind_sample_dna_solution.txt').read()[:-1]

def getNucleotideCountACGT(dna):
    return str(dna.count('A')) + " " + str(dna.count('C')) + " " + str(dna.count('G')) + " " + str(dna.count('T'))

assert getNucleotideCountACGT(dnaSample) == outputSample
print getNucleotideCountACGT(dnaProblem)
