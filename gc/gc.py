from os import path
directory = path.dirname(path.realpath(__file__)).split('/')[-1]
problemName = directory
inputProblem = open('rosalind_'+problemName+'.txt').read()[:-1]
inputSample = open('rosalind_sample_'+problemName+'.txt').read()[:-1]
outputSample = open('rosalind_sample_'+problemName+'_solution.txt').read()[:-1]

# Functions to solve problem
def dnastrandsFromText(text):
    rawdnastrands = text.split('\n>')
    dnastrands = {}
    for rawdnastrand in rawdnastrands:
        name = rawdnastrand.split('\n')[0]
        dnastrand = ''.join(rawdnastrand.split('\n')[1:])
        dnastrands[name] = dnastrand
    return dnastrands

def gcPercentContent(dnastrand):
    gcCount = dnastrand.count('G') + dnastrand.count('C')
    print len(dnastrand)
    nucleotideCount = len(dnastrand)
    gcPercent = 100.0 * float(gcCount) / float(nucleotideCount)
    return gcPercent

# Solution of problem
def solve(inputAsText):
    dnastrands = dnastrandsFromText(inputAsText)
    gcContents = {}
    maxGcContent = 0
    maxGcContentStrand = None
    for dnastrandName in dnastrands:
        dnastrand = dnastrands[dnastrandName]
        print dnastrand
        gcContent = gcPercentContent(dnastrand)
        if gcContent > maxGcContent:
            maxGcContent = gcContent
            maxGcContentStrand = dnastrandName
        gcContents[dnastrandName] = gcContent
    return "{0}\n{1}".format(maxGcContentStrand, str(maxGcContent)[:9])

# Make sure the solution works for the test case
assert solve(inputSample) == outputSample, "{0} != {1}".format(solve(inputSample), outputSample)

# Solve the problem.
with open('_rosalind_'+problemName+'_solution.txt', 'w+') as solutionFile:
    solutionFile.write(solve(inputProblem))
