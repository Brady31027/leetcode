Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
<pre>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
</pre>
***
**Hint**
E.g.   input = [5, 6, 7, 4,  5]   
then   stack = [0, 1, 2, -1, 1]   
and    min   = [5, 5, 5, 4,  4]   
  
Conclusion:  
* During push(), if x - min < 0, update min
* During pop(), if x < 0, update min
* During top(), if x < 0, return min. else return stack[ -1 ]
* During getMin(), just return min
