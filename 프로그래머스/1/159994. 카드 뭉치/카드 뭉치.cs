using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {      
        Queue<string> q1 = new Queue<string>(cards1);
        Queue<string> q2 = new Queue<string>(cards2);
        
        foreach(string word in goal)
        {
            if(q1.Count >0 && q1.Peek() == word)
                q1.Dequeue();
            else if(q2.Count >0 && q2.Peek() == word)
                q2.Dequeue();
            else    return "No";
        }

        return "Yes";
    }
}