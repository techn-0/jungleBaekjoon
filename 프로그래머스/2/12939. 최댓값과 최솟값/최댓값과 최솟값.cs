using System;
public class Solution {
    public string solution(string s) {
        string answer = "";
        int min = 9999 , max = -9999;
        
        
        string[] nums = (s.Split(' '));
        
        int[] arr = new int[nums.Length];
        
        for(int i = 0; i < nums.Length; i++)
        {
            int n = int.Parse(nums[i]);
            if(n < min) min = n;
            if(n > max) max = n;
        }

        answer = min.ToString() + " " + max.ToString();
        return answer;
    }
}