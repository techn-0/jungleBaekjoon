using System;

public class Solution {
    public string solution(string my_string, int s, int e) {
        string answer = "";
        answer += my_string.Substring(0,s);
        
        string strTarget = my_string.Substring(s, e-s+1);
        char[] arrTarget = strTarget.ToCharArray();
        Array.Reverse(arrTarget);
        strTarget = new string (arrTarget);
        
        answer += strTarget + my_string.Substring(e+1);
            
        return answer;
    }
}