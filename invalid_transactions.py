from collections import defaultdict
class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

class Solution:
    def invalidTransactions(self, transactions):
        transactions = [Transaction(*transaction.split(',')) for transaction in transactions]
        transactions.sort(key=lambda t: t.time) # O(nlogn) time

        trans_indexes = defaultdict(list)
        for i, t in enumerate(transactions): # O(n) time
            trans_indexes[t.name].append(i)

        res = []
        for name, indexes in trans_indexes.items(): # O(n) time
            left = right = 0
            
            for t_index in indexes:
                
                t = transactions[t_index]
                
                if (t.amount > 1000):
                    res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                    continue
                
                while left < len(indexes) and transactions[indexes[left]].time < t.time - 60: # O(60) time
                    left += 1
                
                while right < len(indexes)-1 and transactions[indexes[right+1]].time <= t.time + 60: # O(60) time
                    right += 1
                
                for i in range(left,right+1): # O(120) time
                    if transactions[indexes[i]].city != t.city:
                        res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                        break

        return res
abc = Solution()
abc.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"])              
                
                