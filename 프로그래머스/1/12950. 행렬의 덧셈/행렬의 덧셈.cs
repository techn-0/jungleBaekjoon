using System;

public class Solution {
    public int[,] solution(int[,] arr1, int[,] arr2) {
        int n = arr1.GetLength(0);
        int m = arr2.GetLength(1);
        
        int[,] answer = new int[n,m];
        
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                answer[i, j] = arr1[i, j] + arr2[i, j];
            }
        }
        return answer;
    }
}