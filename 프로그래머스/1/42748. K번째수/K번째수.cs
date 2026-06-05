using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int n = commands.GetLength(0);
        // Console.WriteLine(n);
        int[] answer = new int[n];
        
        for(int i=0; i<n; i++){
            int start = commands[i, 0] - 1;
            int end = commands[i, 1] - 1;
            int target = commands[i, 2] -1;
            int len = end - start + 1;
            int[] arr = new int[len];
            
            Array.Copy(array, start, arr, 0, len);
            Array.Sort(arr);
            answer[i] = arr[target];
            
        }
        
        return answer;
    }
}