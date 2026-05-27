using System;
using System.Linq;

public class Solution {
    public string solution(int[] numbers) {
        string answer = "";
        
        string[] strs = numbers.Select(n => n.ToString()).ToArray();
        
        Array.Sort(strs, (a, b) => (b+a).CompareTo(a+b));
        
        answer = string.Join("",strs);
        if(answer[0] == '0') return "0";
        
        return answer;
    }
}