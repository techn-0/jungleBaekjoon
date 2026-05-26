using System;
using System.Collections.Generic;

class Solution {
    public int solution(int[,] maps) {
        int rows = maps.GetLength(0);
        int cols = maps.GetLength(1);
        
        Queue<(int x, int y)> que = new Queue<(int x, int y)>();
        int[,] disit = new int[rows, cols];
        
        que.Enqueue((0,0));
        disit[0, 0] = 1;
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        while(que.Count > 0){
            var (x,y) = que.Dequeue();
            
            for(int i = 0; i<4; i++)
            {
                int nx = x+dx[i];
                int ny = y+dy[i];
                
                if(nx<0 || ny<0 || nx>=rows || ny>=cols)  continue;
                if(disit[nx, ny] != 0)    continue;
                if(maps[nx, ny] == 0)   continue;
                
                disit[nx, ny] = disit[x,y] + 1;
                que.Enqueue((nx, ny));
                
            }
        }
        int goal = disit[rows - 1, cols - 1];
        return goal == 0? -1:goal;
    }
}