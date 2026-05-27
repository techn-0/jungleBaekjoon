using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int n = commands.GetLength(0);
        int[] answer = new int[n];
        
        for(int i = 0; i < n; i ++){
            int str = commands[i, 0];
            int end = commands[i, 1];
            int num = commands[i, 2];
            
            if(end == str){
                answer[i] = array[str-1];
            }
            
            int[] newArr = new int[end - str + 1];
            int k = 0;
            
            for(int j = str-1; j<=end-1; j++){
                newArr[k] = array[j];
                k++;
            }
            Array.Sort(newArr);
            answer[i] = newArr[num-1];
        }
        
        return answer;
    }
}