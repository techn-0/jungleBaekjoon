using System;
public class Solution {
    public bool solution(string s) {
        bool answer = true;
        int len = s.Length;
        
        if(len != 4 && len != 6)
            return false;
        for(int i = 0; i < len; i++)
        {
            char n = s[i];
            if(n < '0' || '9' < n)
                return false;
        }
        return true;
    }
}