using System;
using System.Linq;

public class Solution {
    public bool solution(int x) {
        char[] chars = (x.ToString()).ToCharArray();
        int[] nums = chars.Select(n => n - '0').ToArray();
        int sum = nums.Sum();
        return x % sum == 0 ? true : false;
    }
}