using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int l = n.ToString().Length;
        
        if(l==1)
        {
            return n;
        }
        
        for (int i = 1; i<=l; i++)
        {
            int div = (int)Math.Pow(10,i);
            int tmp = (n % div) / (int)Math.Pow(10, i-1);
            answer += tmp;
        }
        
        return answer;
    }
}