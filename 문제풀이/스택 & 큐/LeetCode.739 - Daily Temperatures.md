[LeetCode.739 - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)
        for i in range(len(T)):
            while len(stack) and T[stack[-1]] < T[i]:
                a = stack.pop()
                answer[a] = i - a
            stack.append(i)
        return answer
```
![KakaoTalk_20201104_024327412](https://user-images.githubusercontent.com/23302973/98021403-a41ff080-1e47-11eb-9bff-a05d4f3c5a89.jpg)
![KakaoTalk_20201104_024327744](https://user-images.githubusercontent.com/23302973/98021406-a4b88700-1e47-11eb-938c-4431b6166140.jpg)
![KakaoTalk_20201104_024327964](https://user-images.githubusercontent.com/23302973/98021409-a5511d80-1e47-11eb-8126-1b164b14e1cc.jpg)
