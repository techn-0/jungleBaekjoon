using System;
using System.Linq;

public class Solution {
    public string solution(int[] numbers) {
        string answer = "";
        
        string[] strs = numbers.Select(x => x.ToString()).ToArray();
        Array.Sort(strs, (a, b) => (b+a).CompareTo(a+b));
        answer = string.Join("", strs);
        
        return answer[0] == '0' ? "0" : answer;
    }
}