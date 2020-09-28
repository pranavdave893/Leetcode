class HelloWorld {
    static void Main() {
        System.Console.WriteLine(Crush("aaabbbc"));
         System.Console.WriteLine(Crush("aabbbacd"));
         System.Console.WriteLine(Crush("aaabbbacd"));
        System.Console.WriteLine(Crush("baaabbbabbccccd"));
                                  System.Console.WriteLine(Crush("baaabbbabbccccdbaaabbbabbdccccdaaabbbbaaabbbabbccccdbaaadbbbabbccccdaaabbb"));
    }
    
    static string Crush(string str)
    {
        if(str.Length <3) return str;
        Stack<CandyNode> st = new Stack<CandyNode>();
       
        for(int i=str.Length-1;i>=0;i--)
        {
            if(st.Count == 0)
            {
                 st.Push(new CandyNode(){Character = str[i], Count =1});
            }
            else
            {
                CandyNode cn = st.Peek();
                
                if(cn.Character != str[i] )
                {
                    
                    if(cn.Count >=3)
                    {
                        
                        char topChar = cn.Character;
                        while(st.Count >0 && st.Peek().Character == topChar)
                        {
                            st.Pop();
                        }
                    }
                    
                    if(st.Count >0 && st.Peek().Character == str[i])
                        st.Push(new CandyNode(){Character = str[i], Count =st.Peek().Count+1});
                    else
                        st.Push(new CandyNode(){Character = str[i], Count =1});
                    
                }
                else
                {
                    st.Push(new CandyNode(){Character = str[i], Count =cn.Count+1});
                }
            }
        }
        
        if(st.Count > 0 && st.Peek().Count >=3)
        {
            char top = st.Peek().Character;
             while(st.Count > 0 && st.Peek().Character == top)
            {
                st.Pop();
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        while(st.Count > 0)
        {
            sb.Append(st.Pop().Character);
        }
        return sb.ToString();
    }
}

public class CandyNode
{
    public char Character {get;set;}
    public int Count{get;set;}
}