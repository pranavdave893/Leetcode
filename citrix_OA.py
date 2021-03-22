import requests

class CitrixOA(object):
    def get_article_titles(self, author):
        
        url = "https://jsonmock.hackerrank.com/api/articles?author={0}&page={1}".format(author, "")
        title_ans = []
        response = requests.get(url)
        response_json = response.json()
        total_pages = response_json.get('total_pages')
    
        for x in range(1, total_pages+1):
            response = requests.get(url + str(x))
            response_json = response.json()
            data_json = response_json.get("data")
            for data in data_json:

                # We can also decode the unicode characters in the title string by using 
                # regular expression. But if we print it. The title string would print in it's
                # original form.
                if data.get("title"):
                    title_ans.append(data.get("title"))
                elif data.get("story_titlex"):
                    title_ans.append(data.get("story_title"))
        
        print (title_ans)
    
    
    def counting_pairs(self, numbers, k):
        
        numbers = set(numbers)
        ans = 0
        for x in numbers:
            if (x + k) in numbers:
                ans += 1
        
        return ans

abc = CitrixOA()
abc.get_article_titles("epaga")
print (abc.counting_pairs([1,2, 2, 2, 3, 4, 4, 5, 6], 1))




