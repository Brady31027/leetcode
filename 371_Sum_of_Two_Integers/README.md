Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Note:
```python
max = 0x7FFFFFFF  # 1 * 31
mask = 0xFFFFFFFF # 1 * 32
a = -1    # 0b11111111111111111111111111111111
b = -2    #
print "bin(a) = %s" % (bin(a))
print "bin(b) = %s" % (bin(b))
while b:
	carry = (a & b) & mask
	a = (a ^ b) & mask
	b = carry << 1
print "a = %d" % (a) # 4294967293
print "bin(a) = %s" %(bin(a)[2:]) # 11111111111111111111111111111101
print "bin(a) => 0: %d , 1: %d" % (bin(a)[2:].count('1'), bin(a)[2:].count('0'))
# according to 2'comp, leading 1 means negative number
# rules: -x = comp(x-1), where comp(0) = 1, comp(1) = 0
c = a ^ mask
print "bin(c) = %s" % (bin(c)) # 10
c = ~c # 1111111111111111111111111111111111111111111111111111111111111101
# 2's comp of (-3) = comp(2) = comp(10) = 111...11101
print "c = %d" %(c)
```
