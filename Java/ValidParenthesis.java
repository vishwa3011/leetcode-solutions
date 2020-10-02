class Solution {
    private HashMap<Character,Character> map;
    
    public Solution()
    {
        this.map=new HashMap<Character,Character>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
    }
    public boolean isValid(String s) {
        Stack1 stack = new Stack1();
        
       for(int i=0;i<s.length();i++)
       {
           char c=s.charAt(i);
           
           if(this.map.containsKey(c))
           {
               char element = stack.isEmpty()?'#':stack.pop();
               System.out.println(element);
               if(element != this.map.get(c))
                   return false;
           }
           else
           {
               stack.push(c);//opening brackets
           }
       }
        
        return stack.isEmpty();
      
    }
    
}

class Stack1 {
    final static int MAX_STACK=10000;
    char[] stack=new char[MAX_STACK];
    int top=-1;
    public void push(char element)
    {
        stack[++top]=element;
    }
    public char pop()
    {
        char temp;
        
        if(top==-1)
        {
            System.out.println("Stack Underflow");
            return 0;
        }
        temp=stack[top--];
        
        return temp;
    }
    public boolean isEmpty()
    {
        if(top==-1)
            return true;
        else
            return false;
    }
   
}