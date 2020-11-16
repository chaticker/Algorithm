[LeetCode.1004 - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)


def longestOnes(self, a: List[int], k: int) -> int:
        st, res = 0, 0
        for i in range(len(a)):
            if a[i] == 0 and k:
                k -= 1
            elif a[i] == 0:
                while a[st] != 0:
                    st += 1
                st += 1              
            res = max(res, i-st+1)
        return res

