#933,leetcode,easy
from collections import deque
class RecentCounter:

    def __init__(self):
        self.windows=deque()

    def ping(self, t: int) -> int:
        self.windows.append(t)
        count=0
        for i in self.windows:
            if i<=t and i>=t-3000:
                count+=1
            elif i>t:
                break
        return count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
#这里使用的是把整个接收都储存，然后再找区间

from collections import deque
class RecentCounter:

    def __init__(self):
        self.windows=deque()

    def ping(self, t: int) -> int:
        self.windows.append(t)
        while self.windows:
            if self.windows[0]<t-3000:
                self.windows.popleft()
            else:
                break
        return len(self.windows)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
#这里是使用了滑动窗口的算法


from collections import deque
class RecentCounter:

    def __init__(self):
        self.windows=deque()

    def ping(self, t: int) -> int:
        self.windows.append(t)
        while self.windows and self.windows[0]<t-3000:
            self.windows.popleft()
        return len(self.windows)
            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
#while条件的更改，将原代码修改得更简洁