using System;

public class Solution {
    public int solution(int n, int[,] computers) {
        
        bool[] visited = new bool[n];
        int cnt = 0;
        
        for(int i=0; i < n; i++){
            if(!visited[i]){
                DFS(i, computers, visited, n);
                cnt++;
            }
        }
        return cnt;
    }
    void DFS(int node, int[,] computers, bool[] visited, int n){
        visited[node] = true;
        for(int next = 0; next < n; next++){
            if(!visited[next] && computers[node, next] == 1){
                DFS(next, computers, visited, n);
            }
        }
    }
}