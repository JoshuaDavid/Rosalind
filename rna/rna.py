problemName = 'rna'
inputProblem = open('rosalind_'+problemName+'.txt').read()[:-1]
inputSample = open('rosalind_sample_'+problemName+'.txt').read()[:-1]
outputSample = open('rosalind_sample_'+problemName+'_solution.txt').read()[:-1]

def reverse(string):
    return string[::-1]

def rnaComplementFromDna(dna):
    complements = {
        'A': 'U', 
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    rnaComplement = ''
    for nucleotide in dna:
        rnaComplement += complements[nucleotide]
    return rnaComplement

def rnaFromDna(dna):
    rna = dna.replace('T', 'U')
    return rna


def solve(inputAsText):
    dna = inputAsText
    return rnaFromDna(dna)

assert solve(inputSample) == outputSample
with open('rosalind_'+problemName+'_solution.txt', 'w+') as solutionFile:
    solutionFile.write(solve(inputProblem))
