using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int n, int w, int num) {
        int hight = n%w == 0? n/w: n/w + 1;
        // Console.Write(hight);
        int[,] arr = new int[hight+1,w+1];
        
        int cnt = 1;
        for(int i = 0; i < hight; i++)
        {
            for(int j = 0; j < w; j++)
            {
                if(cnt >n) break;
                if((i+1/w)%2 != 0) // 나누기 값이 홀수면 역행
                {
                    arr[i, w-j-1] = cnt;
                }
                else
                {
                    arr[i,j] = cnt;
                }
                cnt++;
            }
        }
        
        int idxX = 0, idxY = 0;
        for(int x = 0; x  < hight; x++){
            for(int y = 0; y < w; y++){
                // Console.WriteLine(arr[x, y]);
                if(arr[x,y] == num)
                {
                    idxX= x;
                    idxY= y;
                    break;
                }
            }
        }
        
        // if(idxX == hight) return 1;
        cnt = 0;
        while(idxX < hight)
        {
            if(arr[idxX, idxY] == 0) break;
            Console.WriteLine(idxX);
            Console.WriteLine(hight);
            idxX++;
            cnt++;
        }
        return cnt;
    }
}

// 2차원 맵으로 만들필요 없이 박스가 늘어나는 리스트를 만들고 w개 마다 층이 올라가게 하면 안되려나?
