problem = open('problem.html').read()
sampleoutput = problem.split('<h2 id="sample-output">Sample Output</h2>')[1]
sampleoutput = sampleoutput.split('<div class="codehilite"><pre>')[1]
sampleoutput = sampleoutput.split('</pre></div>')[0]
print sampleoutput[:-1]
