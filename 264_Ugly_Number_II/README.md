Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example,
<pre>
 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 
</pre>
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

***
  
TLE solution
```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt, i = 0, 1
        while True:
            j = i
            for div in [2, 3, 5]:
                while j % div == 0:
                    j /= div
            if j == 1: cnt += 1
            if cnt == n: return i
            i += 1          
```  
***  
** Observation and Regression  
* All ugly numbers are based on certain known ugly numbers
* E.g.
| Known ugly   |  1  |  2  |  3  |  4  |  5  |  6  |  8  |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1st iter x2  | 1*2 | 2*2 | 3*2 | 4*2 | 5*2 | 6*2 | 8*2 |
| 2nd iter x3  | 1*3 | 2*3 | 3*3 | 4*3 | 5*3 | 6*3 | 8*2 |
| 3rd iter x5  | 1*5 | 2*5 | 3*5 | 4*5 | 5*5 | 6*5 | 8*5 |


