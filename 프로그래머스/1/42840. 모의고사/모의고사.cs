using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] answers) {
        List<int> answer = new List<int>();
        
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] point = new int[3];
        
        int n = answers.Length;
        for(int i = 0; i < n; i++){
            if(answers[i] == p1[i%5]) point[0]++;
            if(answers[i] == p2[i%8]) point[1]++;
            if(answers[i] == p3[i%10]) point[2]++;
        }
        
        int max = point.Max();
        
        for(int j = 0; j<3; j++){
            if(point[j] == max) answer.Add(j+1);  
        }

        return answer.ToArray();
    }
}