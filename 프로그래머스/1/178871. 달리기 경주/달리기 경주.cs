using System;
using System.Collections.Generic;

public class Solution {
    public string[] solution(string[] players, string[] callings) {

        Dictionary<string, int> rank = new Dictionary<string, int>();
        
        for(int i=0; i<players.Length; i++){
            rank[players[i]] = i;
        }
        
        foreach(string name in callings){
            int cur = rank[name];
            int next = cur-1;
            
            string nextName = players[next];
            
            players[next] = name;
            players[cur] = nextName;
            
            rank[name] = next;
            rank[nextName] = cur;
            
        }
        
        return players;
    }
}