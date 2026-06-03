using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = new int[] {};
        
        int n = progresses.Length;
        // Console.Write(n);
        
        int start = 0;
        while(start < n){
            while(progresses[start]<100){
                for(int i = 0; i<n; i++){
                    progresses[i] += speeds[i];
                }
                
            }// 맨 앞 100퍼 이상 완료
            start++;
            // 다음것들도 100 이상인지 확인
            int cnt = 1;
            for(int j = start; j < n; j++){
                if(progresses[j] >= 100){
                    cnt++;
                    start++;
                }
                else   break;
            }
            answer = answer.Append(cnt).ToArray();
        }
        return answer;
    }
}