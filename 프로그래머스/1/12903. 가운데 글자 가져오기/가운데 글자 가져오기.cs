using System;
public class Solution {
    public string solution(string s) {
        string mid = "";
        int len = s.Length;
        int midIndex = len / 2;
        Console.Write(len);
        Console.Write(midIndex);
        
        if(len % 2 == 1)
            mid = s.Substring(midIndex, 1);
        else
            mid = s.Substring(midIndex-1, 2);
        return mid;
    }
}