[LeetCode.739 - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

```python
T = [73, 74, 75, 71, 69, 72, 76, 73]

stack = []
answer = [0] * len(T)

for i in range(len(T)):
    while len(stack) and T[stack[-1]] < T[i]:
        a = stack.pop()
        answer[a] = i - a #
    stack.append(i)
print(answer)

```
