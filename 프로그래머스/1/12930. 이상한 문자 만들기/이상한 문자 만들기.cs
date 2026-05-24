public class Solution {
    public string solution(string s) {
        char[] word = s.ToCharArray();
        int cnt = 0;
        
        for(int i = 0; i < word.Length;i++)
        {
            if(word[i] == ' ')   cnt = 0;
            
            else
            {
                if(cnt%2 == 0)  word[i] = char.ToUpper(word[i]);
                else    word[i] = char.ToLower(word[i]);
                cnt++;
            }
        }
        return new string(word);
    }
}