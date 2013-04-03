from os import path
directory = path.dirname(path.realpath(__file__)).split('/')[-1]
problemName = directory
inputProblem = open('rosalind_'+problemName+'.txt').read()[:-1]
inputSample = open('rosalind_sample_'+problemName+'.txt').read()[:-1]
outputSample = open('rosalind_sample_'+problemName+'_solution.txt').read()[:-1]

# Functions to solve problem
def diff(string1, string2):
    assert len(string1) == len(string2), "Strings must be the same length"
    differences = 0
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            differences += 1
    return differences

# Solution of problem
def solve(inputAsText):
    dnastrand1 = inputAsText.split('\n')[0]
    dnastrand2 = inputAsText.split('\n')[1]
    return str(diff(dnastrand1, dnastrand2))

# Make sure the solution works for the test case
assert solve(inputSample) == outputSample

# Solve the problem.
with open('_rosalind_'+problemName+'_solution.txt', 'w+') as solutionFile:
    solutionFile.write(solve(inputProblem))
