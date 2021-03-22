"""
tags : Samsara, telephone interview
"""
# import re
from markdown.markdown.core import Markdown
# class Soluition():
    
#     def markdown(self, s):
#         tags = {
#             ">": "<blockquote>",
#             "": "<br />",
#         }

#         in_line_tags = {
#             "*": ["<em>"],
#             "~~": ["<del>"],
#             "**": ["<strong>"],
#             '***': ["<strong>", "<em>"]
#         }

#         s.strip()
#         para = s.split("\n\n")

#         print (s)

#         ans = []
        
#         start_tag_stack = []
        
#         st = set()
        
#         for line in s:
#             if line == "":
#                 if start_tag_stack:
#                     tag = start_tag_stack.pop()
#                     tag = tag[:1] + "/" + tag[1:]
#                     ans.append(tag)
                
#                 ans.append("</p>")
            
#             elif line != "" and line[0] in tags and tags[line[0]] not in st:
#                 tag = tags[line[0]] #<blockquote>
#                 ans.append(tag)
#                 st.add(tag)
#                 start_tag_stack.append(tag)
            
#             elif line[0] in tags and tags[line[0]] in st:
#                 ans.append(line[2:])
                        
#             elif line != "":
#                 for temp in in_line_tags.keys():
#                     occurences = [m.start() for m in re.finditer(temp, line)]
#                     if occurences and len(occurences) >=2:
#                         idx = 1
#                         while idx < len(occurences) - 1:
#                             first, second = occurences[idx-1], occurences[idx]
#             else:
#                 ans.append("</br>")


#         if start_tag_stack:
#             ans.append(start_tag_stack.pop())
            

# md = Soluition()
# md.markdown('''This is a paragraph with a soft
# line break.

# This is another paragraph that has
# > Some text that
# > is in a
# > block quote.

# This is another paragraph with a ~~strikethrough~~ word kjbbjbkjb

# # This is H1 tag
# ## this is H2 tag
# ''')

"""
st = [(~~)]
temp = strikethrough


***

1) split by "\n\n" <= paragraph
2) split by "\n" <= line break
=> if any Header encountered then whole add header tag in stack
3) split by space
4) if encounter special characters(~~, **, *) in the beginneing and ending then add tags for the character.
5) if starting with special character and not ending then check next words ending.
6) if next word ending contains that character then update all the words with the tag.

[8, 14, 16, 18, 19]
abcd[:start] + tag + abcd[start+2:end] + tag + abcd[end+2:]
"""

class Sol():

    def get_closing_tag(self, tag):
        return tag[:1] + "/" + tag[1:]

    def md(self, s):

        two_char_symbol = {
            "~~": "<del>",
            "**": "<b>",
        }

        bq = {
            '>': "<blockquote>"
        }

        s = s.split("\n\n")
        ans = []
        stack = []
        st = set()
        
        for idx, line in enumerate(s):
            lines = line.split("\n")
            new_ans = []
            
            for new_line in lines:
                if not new_line:
                    continue

                if not stack:
                    ans.append("<p>")
                
                temp = ''
                word_lines = new_line.split()
                for word_id, word in enumerate(word_lines):
                    if word.startswith('~~') or word.startswith('**'):
                        stack.append(word[0]+word[1])
                        new_ans.append(word[2:-2])
                        
                        if word.endswith('~~') or word.endswith('~~'):
                            open_tag = two_char_symbol[stack.pop()]
                            ans.append(open_tag)
                            ans += new_ans
                            new_ans = []
                            ans.append(self.get_closing_tag(open_tag))
                    
                    elif word.endswith('~~') or word.endswith('~~'):
                        open_tag = two_char_symbol[stack.pop()]
                        ans.append(open_tag)
                        ans += new_ans
                        new_ans = []
                        ans.append(self.get_closing_tag(open_tag))
                        
                    elif len(word) == 1 and word[0] == ">":
                        if ('>') in st:
                            continue
                        stack.append('>')
                        st.add(">")
                    
                    if word_id != len(word_lines)-1 or word_id != 0:
                        word +=  " "
                    
                    if not stack:
                        ans.append(word)
                    else:
                        new_ans.append(word)
                
                if not st:
                    ans.append("</p>")
            if st:
                ans.append("<blockquote>")
                ans += new_ans
                ans.append("</blockquote>")
                ans.append("</p>")
                st.remove(">")
                stack.pop()
            
            elif idx != len(s) - 1:
                ans.append("</br>")
        
        return ''.join(ans)


xy = Sol()
print (xy.md('''This is a paragraph with a soft
line break.   

This is another paragraph that has
> Some text that
> is in a
> block quote.

This is another paragraph with a ~~strikethrough~~ word.
'''))

md = Markdown()
# print (md.convert('''This is a paragraph with a soft
# line break.   

# This is another paragraph that has
# > Some text that
# > is in a
# > block quote.

# This is another paragraph with a ~~strikethrough~~ word.
# '''))

from collections import defaultdict
class Node():
    def __init__(self):
        self.children = defaultdict(list)
        self.is_last_word = False


class Tree():
    def __init__(self):
        self.root = Node()
    

    def add_data(self, data, is_tag=None):
        curr = self.root
        if is_tag and is_tag in curr.children:
            curr = curr.children[is_tag]
        else:
            new_node = Node()
            new_node.children[is_tag] = new_node
            curr = new_node
        
    


        