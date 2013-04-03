from os import path
directory = path.dirname(path.realpath(__file__)).split('/')[-1]
problemName = directory
inputProblem = open('rosalind_'+problemName+'.txt').read()[:-1]
inputSample = open('rosalind_sample_'+problemName+'.txt').read()[:-1]
outputSample = open('rosalind_sample_'+problemName+'_solution.txt').read()[:-1]

# Functions to solve problem
def rabbitModel(numMonths, reproductionRate):
    # All of the rabbits reproduce every 2 months.
    month = 1
    numRabbitPairsByMonth = [0, 1]
    while month < numMonths:
        numRabbitPairs = numRabbitPairsByMonth[-1]
        numRabbitPairs += reproductionRate * numRabbitPairsByMonth[-2]
        numRabbitPairsByMonth.append(numRabbitPairs)
        month += 1
    return numRabbitPairsByMonth[numMonths]

# Solution of problem
def solve(inputAsText):
    numMonths = int(inputAsText.split(' ')[0])
    reproductionRate = int(inputAsText.split(' ')[1])
    return str(rabbitModel(numMonths, reproductionRate))

# Make sure the solution works for the test case
assert str(solve(inputSample)) == str(outputSample)

# Solve the problem.
with open('_rosalind_'+problemName+'_solution.txt', 'w+') as solutionFile:
    solutionFile.write(solve(inputProblem))
