"""
Tags: Samsara
"""

class Pallet:
    def __init__(self, id, weight):
        self.__id = id
        self.__weight = weight

    def get_id(self):
        return self.__id

    def get_weight(self):
        return self.__weight

class Trailer:
    def __init__(self):
        self.__total_weight = 0
        self.__pallet_map = {}
        self.__weight_history = [(0, 0)]

    def load(self, pallet: Pallet, time_stamp):
        self.__pallet_map[pallet.get_id()] = pallet
        self.__total_weight += pallet.get_weight()
        self.__weight_history.append((time_stamp, self.__total_weight))

    def unload(self, pallet_id, time_stamp):
        pallet = self.__pallet_map.get(pallet_id, None)

        if not pallet:
            print("NO SUCH PALLET")
            return None

        del self.__pallet_map[pallet_id]
        self.__total_weight -= pallet.get_weight()
        self.__weight_history.append((time_stamp, self.__total_weight))
        return pallet

    def get_total_weight(self, time_stamp=None):
        if time_stamp is None:
            return self.__total_weight
        return self.__search(time_stamp)

    def __search(self, time_stamp):
        l = 0
        r = len(self.__weight_history) - 1
        while l + 1 < r:
            mid = (l+r) // 2
            if self.__weight_history[mid][0] >= time_stamp:
                r = mid
            else:
                l = mid
        if self.__weight_history[r][0] <= time_stamp:
            return self.__weight_history[r][1]
        return self.__weight_history[l][1]

p1 = Pallet(1, 2)
p2 = Pallet(2, 3)
p3 = Pallet(3, 4)

t = Trailer()
t.load(p1, 1)
print(t.get_total_weight())
t.load(p2, 2)
print(t.get_total_weight())
t.load(p3, 5)
print(t.get_total_weight())
t.unload(p3.get_id(), 7)
print(t.get_total_weight())
t.unload(p2.get_id(), 8)
print(t.get_total_weight())
t.unload(p1.get_id(), 9)
print(t.get_total_weight())
print()

for i in range(10):
    print("weight at time " + str(i) + " : " + str(t.get_total_weight(i)))
