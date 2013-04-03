from os import path
directory = path.dirname(path.realpath(__file__)).split('/')[-1]
problemName = directory
inputProblem = open('rosalind_'+problemName+'.txt').read()[:-1]
inputSample = open('rosalind_sample_'+problemName+'.txt').read()[:-1]
outputSample = open('rosalind_sample_'+problemName+'_solution.txt').read()[:-1]

# Functions to solve problem

# Solution of problem
def solve(inputAsText):
    return

# Make sure the solution works for the test case
assert solve(inputSample) == outputSample

# Solve the problem.
with open('_rosalind_'+problemName+'_solution.txt', 'w+') as solutionFile:
    solutionFile.write(solve(inputProblem))
