#733,leetcode
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        if image[sr][sc]==color:
            return image
        queue=deque()
        queue.append((sr,sc))
        startval=image[sr][sc]
        image[sr][sc]=color
        while queue:
            node=queue.popleft()
            h,l=node[0],node[1]
            if l-1>=0: #left
                if image[h][l-1]==startval:
                    image[h][l-1]=color
                    queue.append((h,l-1))
            if l+1<len(image[h]):#right
                if image[h][l+1]==startval:
                    image[h][l+1]=color
                    queue.append((h,l+1))
            if h-1>=0:#up
                if image[h-1][l]==startval:
                    image[h-1][l]=color
                    queue.append((h-1,l))
            if h+1<len(image):#down
                if image[h+1][l]==startval:
                    image[h+1][l]=color
                    queue.append((h+1,l))
        return image