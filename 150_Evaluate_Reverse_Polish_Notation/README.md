Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
<pre>
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
</pre>
  
***  
**Trap**  
Python int calculation results lean to round to the smallest point
  
Example:    
* >>> 6/10
  * Get 0
  * Explanation: 0.6 trancate to 0
  
* >>> 6/-10
  * Get -1
  * Explanation: -0.6 round to -1
  
* >>> 6.0/10
  * 0.6
  * Explanaiton: convert to float or double first to avoid this problem  
  * use int() will coverge to 0

* >>> int(6.0/10)
  * Get 0
  * Explanation: equal to int(0.6) = 0

* >>> int(6.0/10)
  * Get 0
  * Explanation: equal to int(-0.6) = 0
