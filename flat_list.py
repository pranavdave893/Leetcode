abc = [[1,1],[2,[1,1,[3,4]]]]
abc_2 = [1,[4,[6]]]
def get_abc(abc):
    for x in abc:
        yield x

answer = []
def get_next_element(mmm, answer):
    for i in mmm:
        if type(i) is not int:
            yield get_next_element(i, answer)
        else:
            yield i

abc = get_next_element(abc, answer)
import pdb; pdb.set_trace()
print (answer)
