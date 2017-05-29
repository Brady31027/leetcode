Write a function to find the longest common prefix string amongst an array of strings.
  
***
  
**Hint**
Use the 1st string as the anchor, char by char to compare every other strings.
  
```python
for i in xrange(len(strs[0])):
    for s in strs[1:]:
        if i >= len(s) or strs[0][i] != s[i]:
            return s[:i]
return strs[0]
```
