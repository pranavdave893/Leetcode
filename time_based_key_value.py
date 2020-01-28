from heapq import heappush
from collections import defaultdict
        
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        heap = self.dict[key]
        heappush(heap, (-timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        for ts, value in self.dict[key]:
            if -ts <= timestamp:
                return value
        
        return ""

abc = TimeMap()
abc.set("ctondw", "ztpearaw", 1)
abc.set("ctondw", "gszaw", 4)
abc.get("ctondw", 6)



["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
[[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]