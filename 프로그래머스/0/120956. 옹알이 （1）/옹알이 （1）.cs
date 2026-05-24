using System;

public class Solution {
    public int solution(string[] babbling) {
        string[] sounds = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        
         foreach (string word in babbling)
         {
             string temp = word;
              foreach (string sound in sounds)
                  temp = temp.Replace(sound, " ");
             
             if(temp.Trim().Length == 0)
                 answer++;
         }
        
        return answer;
    }
}