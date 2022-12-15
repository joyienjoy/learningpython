Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string



```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size = len(strs)
        if (size == 0):
            return ""
 
        if (size == 1):
            return strs[0]
 
        strs.sort()   #sort 
     
        # find the minimum length
        end = min(len(strs[0]), len(strs[size - 1]))
 
        # find the common prefix
        i = 0
        while (i < end and strs[0][i] == strs[size - 1][i]):
            i += 1
 
        prefix = strs[0][0: i]
        return prefix
```
