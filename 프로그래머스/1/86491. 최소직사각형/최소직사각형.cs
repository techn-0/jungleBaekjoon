using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[,] sizes) {
        int maxX = 0;
        int maxY = 0;
        
        int n = sizes.GetLength(0);
        Console.Write(n);
        
        for(int i = 0; i<n; i++){
            int a = sizes[i,0];
            int b = sizes[i,1];
            if( b > a){
                sizes[i,0] = b;
                sizes[i,1] = a;
            }
            if(sizes[i,0] > maxX) maxX = sizes[i,0];
            if(sizes[i,1] > maxY) maxY = sizes[i,1];
        }
        
        return maxX*maxY;
    }
}