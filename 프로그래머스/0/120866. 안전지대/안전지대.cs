using System;

public class Solution {
    public int solution(int[,] board) {
        int answer = 0;
        
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        int rows = board.GetLength(0);
        int cols = board.GetLength(1);
        
        for(int i= 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                if(board[i,j] == 1)
                {
                    for(int k = 0; k < 8; k++)
                    {
                        int nx = i+dx[k];
                        int ny = j+dy[k];
                        if(isInside(nx, ny, rows, cols))
                            if(board[nx,ny] !=1) board[nx,ny] = 2;
                    }
                }
            }
        }
        
        for(int i= 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                if(board[i,j] == 0) answer++;
            }
        }
        
        return answer;
    }
    bool isInside(int x, int y, int rows, int cols){
        return 0<=x && x<rows && 0<=y && y<cols;
    }
}