[LeetCode217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                return True
        return False
```
