from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.keytimes = defaultdict(list)
        self.dct = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None: 
        
        #guaranteed to be in increasing order timestamp so i can binary search when i get
        self.keytimes[key].append(timestamp)
        self.dct[(key,timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keytimes: return ""
        times = self.keytimes[key]

        l, r = 0, len(times) - 1
        # base case: rules out the fact that i'm not going to find the timestamp.
        if not times or times[l] > timestamp: return ""
        if timestamp > times[r]: return self.dct[(key, times[r])]

        # print(times)
        while l <= r:
            # print(l,r)
            c = (l+r)//2
            if l == r or times[c] <= timestamp < times[c+1]: return self.dct[(key, times[c])]
            elif timestamp >= times[c+1]: l = c + 1
            else: r = c
        return ""
        
