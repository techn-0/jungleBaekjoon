using System;

public class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sum = 0;
        foreach(int i in numbers)
        {
            sum +=i;
        }
        // Console.Write(sum);
        answer = (double)sum / numbers.Length;
        return answer;
    }
}