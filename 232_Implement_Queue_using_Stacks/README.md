Implement the following operations of a queue using stacks.
  
* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.
  
Notes:  
* You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
  
***  
Hint:  
* Use 2 stack to simulate a queue
  * For push(), we always push to stack1
  * For pop(), we iteratively pop from stack1 and push to stack2. After this process, the top of stack2 is the head of stack1. So we simply pop the stack2
  * For peek(), exactly the same as pop(), we iteratively pop stack1 and push to stack2, and return the value of the top of stack2
  * For isEmpty, simply determine both the stack1 and stack2 are empty
