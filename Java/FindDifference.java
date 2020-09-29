class Solution {
    public char findTheDifference(String s, String t) {
        
        int ch[] = new int[26];
        
        for(char c : s.toCharArray())
        {
            ch[c - 'a']++;
        }

        for(char ct : t.toCharArray())
        {
            ch[ct - 'a']--;
            
            if(ch[ct - 'a']<0)
                return ct;
        }
        
        return ' ';
        
    }
}