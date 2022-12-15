Given an integer x, return true if x is a palindrome, and false otherwise.

```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        number = x
        reverse = 0
        while x > 0:
            digit = (x % 10)
            reverse = (reverse * 10) + digit
            x = x // 10
        if (number == reverse):
            return True
        else:
            return False
```
