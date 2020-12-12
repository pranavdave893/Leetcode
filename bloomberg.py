import heapq

from collections import Counter
'''

{
    'quiz.sports.q1.question' = 'Which one is correct team name in NBA?',
    'quiz.sports.q1.options[0]' = 'New York Bulls',
    'quiz.sports.q1.options[1]' = 'Los Angeles Kings',
    ...
    'quiz.sports.q1.answer' = 'Huston Rocket'
}

{
    'quiz.sports.q1.quesitons.a[0]' 
}
'''
"""
{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ]},
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    10,
                    11,
                    12,
                    13
                ],
                "answer": 12
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    1,
                    2,
                    3,
                    4
                ],
                "answer": 4
            }
        }
    }
}
"""


ans = {}

def recur(dct, ans_str=''):
    ct = 0
    for key in dct:
        
        ans_str += (key + ".")      # quiz.
        val_1 = dct[key]
        
        if type(val_1) == dict:
            recur(val_1, ans_str)
        
        elif type(val_1) != dict:
            if type(val_1) == list:
                for idx, x in enumerate(val_1):
                    ans[ans_str + str(idx)] = x
            else:
                ans_str = ans_str[:len(ans_str)-1]
                print (ans_str)
                ans[ans_str] = val_1
        
        ct += 1
        
    return ans


"""
https://leetcode.com/discuss/interview-question/688722/bloomberg-phone/696597
a = [21,5,6,56,88,52], output = [5,5,5,4,-1,-1]
"""

from heapq import *

def find_right_index(nums):

    ans = [-1]*len(nums)
    heap = []
    
    for idx, x in enumerate(nums):
        heappush(heap, (-x, idx))
    
    max_idx = -1

    while heap:

        temp = heappop(heap)

        val, curr_idx = -temp[0], temp[1]

        if max_idx == -1 or curr_idx > max_idx or nums[max_idx] == nums[curr_idx]:
            max_idx = max(curr_idx, max_idx)
            continue

        ans[curr_idx] = max_idx
        max_idx = max(curr_idx, max_idx)
    
    return ans

# find_right_index([21,5,6,56,88,5])
class UDP(object):
    def __init__(self):
        self.dct = {}
    
    def udp_packets(self, number):

        dct = self.dct
        if dct:
            if number-1 in dct and number+1 not in dct:
                print (number-1, number)
                del dct[number-1]
            
            if number-1 in dct and number+1 in dct:
                print (number-1, number, number+1)
                del dct[number-1]
                del dct[number+1]
                return
            
            if number+1 in dct and number-1 not in dct:
                print (number+1, number)
                del dct[number+1]
                return
            
            if number +1 in dct and number-1 not in dct:
                print (number-1, number, number+1)
                del dct[number-1]
                del dct[number+1]
                return
        
        dct[number] = number


# abc = UDP()
# abc.udp_packets(2)
# abc.udp_packets(4)
# abc.udp_packets(6)
# abc.udp_packets(5)
# abc.udp_packets(7)
# abc.udp_packets(3)
# abc.udp_packets(4)
# abc.udp_packets(8)
# abc.udp_packets(10)
# abc.udp_packets(9)
# abc.udp_packets(15)
# abc.udp_packets(12)
# abc.udp_packets(11)
# abc.udp_packets(17)
# abc.udp_packets(14)
# abc.udp_packets(13)
# abc.udp_packets(11)
# abc.udp_packets(19)
# abc.udp_packets(22)



class frequency():


    def output(self, nums):
        cnt = {}
        
        for item in nums:
            if item not in cnt:
                cnt[item] = 1
            else:
                cnt[item] += 1
                
        newCnt = sorted(cnt.items(), key=lambda x: (x[1], -x[0]))
                
        soln = []
        for item in newCnt:
            element, count = item
            soln.extend([element] * count)
            
        print (soln)
        # heap = []
        # element_to_frequency = Counter(elements)
        # elements = []

        # for element, frequency in element_to_frequency.items():
        #     heapq.heappush(heap, (frequency, -element))

        # while heap:
        #     frequency, element = heapq.heappop(heap)
        #     elements.extend([-element] * frequency)

        # return elements

abc = frequency()
abc.output([3, 4, 2, 5, 2, 3, 4, 3, 6,6,6,6])


    

