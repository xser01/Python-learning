class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
        for char in t:
            count[char]=count.get(char,0)-1
        return all(v==0 for v in count.values())

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s)==Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hmap1:dict={}
        hmap2:dict={}
        for char1,char2 in zip(s,t):
            if char1 not in hmap1.keys():
                hmap1.update({char1:1})
            else:
                hmap1[char1]+=1
            if char2 not in hmap2.keys():
                hmap2.update({char2:1})
            else:
                hmap2[char2]+=1
        return hmap1==hmap2