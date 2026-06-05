using System;
using System.Collections.Generic;

class Solution {
    public int solution(int[,] maps) {
        int row = maps.GetLength(0);
        int col = maps.GetLength(1);
        int[,] dis = new int[row, col];
        Queue<(int x, int y)> que = new Queue<(int, int)>();
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        dis[0,0] = 1;
        que.Enqueue((0,0));
        
        while(que.Count>0){
            var(x,y) = que.Dequeue();
            
            for(int i = 0; i<4; i++){
                int nx = x +dx[i];
                int ny = y +dy[i];
                //맵 밖인가?
                if(nx < 0 || nx>= row || ny < 0 || ny >= col) continue;
                // 벽인가?
                if(maps[nx, ny] == 0) continue;
                // 이미 방문 했나?
                if(dis[nx, ny] != 0) continue;
                
                dis[nx, ny] = dis[x,y] + 1;
                que.Enqueue((nx, ny));
            }
        }
        int answer = dis[row-1, col-1];
        return answer == 0 ? -1 : answer;
    }
}