using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<int> answer = new List<int> {};
        
        int n = progresses.Length;
        int[] days = new int[n];
        
        for(int i = 0; i < n; i++){
            days[i] = (int)Math.Ceiling((100.0-progresses[i]) / speeds[i]);
            Console.WriteLine(days[i]);
        }
        int day = days[0];
        int cnt = 1;
        for(int j = 1; j < n; j++){
            if(day >= days[j]){
                cnt++;
            }
            else{
                answer.Add(cnt);
                day = days[j];
                cnt = 1;
            }
        }
        answer.Add(cnt);
        return answer.ToArray();
    }
}