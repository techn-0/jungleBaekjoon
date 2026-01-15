using System;

public class Solution {
    public int solution(string t, string p) {
        int answer = 0;
        int pLen = p.Length;
        long pNum = long.Parse(p); 

        for (int i = 0; i <= t.Length - pLen; i++) {
            string sub = t.Substring(i, pLen);
            long subNum = long.Parse(sub);
            
            if (subNum <= pNum)
                answer++;
        }
        return answer;
    }
}