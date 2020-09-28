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

        if max_idx == -1 or curr_idx > max_idx or nums[max_idx] == num[curr_idx]:
            max_idx = max(curr_idx, max_idx)
            continue

        ans[curr_idx] = max_idx
        max_idx = max(curr_idx, max_idx)
    
    return ans

    
        
        


    

