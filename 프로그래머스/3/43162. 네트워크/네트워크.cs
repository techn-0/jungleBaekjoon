using System;

public class Solution {
    public int solution(int n, int[,] computers) {
        int cnt = 0;
        bool[] visited = new bool[n];
        
        for(int i=0; i<n; i++){
            if(!visited[i]){
                DFS(i, n, computers, visited);
                cnt++;
            }
            
        }
        
        return cnt;
    }
    void DFS(int node, int n, int[,] computers, bool[] visited){
        visited[node] = true;
        for(int i = 0; i<n; i++){
            if(!visited[i] && computers[node, i] == 1){
                DFS(i, n, computers, visited);
        }
    }
}
}