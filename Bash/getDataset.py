problem = open('problem.html').read()
sampledataset = problem.split('<h2 id="sample-dataset">Sample Dataset</h2>')[1]
sampledataset = sampledataset.split('<div class="codehilite"><pre>')[1]
sampledataset = sampledataset.split('</pre></div>')[0]
print sampledataset[:-1]
