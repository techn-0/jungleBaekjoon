using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        List<int> losts = new List<int>(lost);
        List<int> reserves = new List<int>(reserve);
        losts.Sort();
        
        // 가지고 있는 본인이 도난당한 경우 reserves 에서 제거
        int m = losts.Count;
        for(int i = 0; i < m; i++){
            if(reserves.Contains(losts[i])){
                reserves.Remove(losts[i]);
                losts[i] = 0;
            }
        }
        
        foreach(int j in losts){
            // Console.WriteLine(j);
            if(j == 0)   continue;
            
            if(reserves.Contains(j-1)){
                reserves.Remove(j-1);
            }
            else if(reserves.Contains(j+1)){
                reserves.Remove(j+1);
            }
            else answer--;
                
        }

        return answer;
    }
}