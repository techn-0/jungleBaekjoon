public class Solution {
    public int solution(string s) {
        bool N = false;
        int answer = 0;
        
        if(s[0] =='+')
        {
            answer = int.Parse(s.Substring(1));
        }
            
        else if(s[0] =='-')
        {
            answer = int.Parse(s.Substring(1));
            N = true;
        }
        else answer = int.Parse(s);
        
        if(N==true) answer = -answer;
            
        return answer;
    }
}