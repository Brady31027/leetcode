The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
<pre>
"123"
"132"
"213"
"231"
"312"
"321"
</pre>
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

***

#### Experiments
    
Even the following one-line code leads to TLE, so it is probably not suitable to actually applying permutation methods. Try to use mathmatical approach instead.
 
```python
return "".join(list(itertools.permutations([str(i+1) for i in range(n)]))[k-1])
```
  
#### Observation and Regression:
* case 1: n = 3
<pre>
123
132
213
231
312
321
</pre>
In descending order:
  * leading 1: x2
    * followed by 2: x1
    * followed by 3: x1
  * leading 2: x2
    * followed by 1: x1
    * followed by 3: x1
  * leading 3: x2
    * followed by 1: x1
    * followed by 2: x1

* case 2: n = 4
<pre>
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
</pre>
In descending order:
* leading 1: x6
* leading 2: x6
  
#### Conclusion
Given input n, the most significant digit has **(n-1)*(n-2)** options
<pre>
(n-1)*(n-2) can be calculated by math.factorial(n-1)
</pre>

* Algorithm
  * Pick a digit from the candidates list by calculating k/math.factorial(n-1)
  * Update k = k % facorial because we've narrowed down the scope
  * Update n -= 1 because the number of candidates will decrease one by one
  * Update candidates = candidates[:picked_index] + candidates[picked_index+1:]
  * Update factorial by calculating (n-1)*(n-2) or math.factorial(n-1)
  * Loop again and again if len(candidates) > 0 which means that all the digits are picked
