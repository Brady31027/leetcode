A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.

***
**Operations**
* Addition
* Deletion
* Subsitution
  
**Strategy**
* If length is less than 6, prefer addtion
* If length is greater than 6, prefer deletion
* If length is valid, prefer subsitution 

**Cases**
* If s < 6
  * aaaaa
    * aaAaa1 -> x2
  * aaaA
    * aa1aAb -> x2
  * aA
    * aA1BCD -> x4
  * Conclusion: step = max(6 - totalCnt, 3 - typeCnt)
* If s >= 6
  * deleteCnt = max(totalCnt - 20, 0)
  * changeCnt = sum(r/3 for r in repeatCnt)
  * step = deleteCnt + max(changeCnt, 3 - typeCnt)
  
***  
* Recommanded solution: https://discuss.leetcode.com/topic/63341/simple-python-solution/2
* Another solution: https://github.com/kamyu104/LeetCode/blob/master/Python/strong-password-checker.py
