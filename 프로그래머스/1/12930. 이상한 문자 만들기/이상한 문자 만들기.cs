public class Solution {
    public string solution(string s) {
        char[] words = s.ToCharArray();
        int cnt = 0;
        
        for(int i = 0; i < words.Length; i++)
        {
            if(words[i] == ' ' ) cnt = 0;
            else
            {
                if (cnt % 2 == 0)   words[i] = char.ToUpper(words[i]);
                else    words[i] = char.ToLower(words[i]);
                cnt++;
            }
        }
        
        return new string(words);
    }
}