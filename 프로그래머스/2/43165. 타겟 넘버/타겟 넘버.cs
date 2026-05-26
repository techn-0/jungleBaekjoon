using System;

public class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    
    int dfs(int[] numbers, int target, int idx, int sum){
        if(idx == numbers.Length)   return sum == target ? 1 : 0;
        
        return dfs(numbers, target, idx+1, sum + numbers[idx]) +
            dfs(numbers, target, idx+1, sum - numbers[idx]);
        
    }
}