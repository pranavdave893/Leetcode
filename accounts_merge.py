from collections import defaultdict

class Account:
    def __init__(self, name):
        self.name = name
        self.email = set()
    
    def add_emails(self, emails):
        for email in emails:
            self.email.add(email)
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        name_accounts = defaultdict(list)
        
        def add_account(account):
            Ac = Account(account[0])
            Ac.add_emails(account[1:])
            name_accounts[account[0]].append(Ac)
            
        
        for account in accounts:
            account_name = account[0]
            emails = account[1:]
            
            not_found = True
            if account_name in name_accounts:
                for name_account in name_accounts[account_name]:
                    for email in account[1:]:
                        if email in name_account.email:
                            not_found = False
                            emails = account[1:]
                            name_account.add_emails(emails)
                
                if not_found:
                    add_account(account)
            
            else:
                add_account(account)
        
        ans = []
        
        for name in name_accounts:
            accounts = name_accounts[name]
            for account in accounts:
                new_ans = [account.name]
                emails = []
                for email in account.email:
                    emails.append(email)
                
                emails.sort()
                new_ans.extend(emails)

                ans.append(new_ans)
        
        print(ans)

abc = Solution()
abc.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])