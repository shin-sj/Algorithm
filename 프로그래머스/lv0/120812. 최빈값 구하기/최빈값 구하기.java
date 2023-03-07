import java.util.*;
class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int max = 0;
        int frequent[] = new int[1000];
        for(int i = 0; i < array.length; i++) {
            frequent[array[i]] += 1;
            if(max < frequent[array[i]]) {
                max = frequent[array[i]]; //개수 
                answer = array[i];  
            }
        }
        
        int tmp = 0;
        for(int i = 0; i < 1000; i++) {
            if(frequent[i] == max)
                tmp += 1;
            if(tmp > 1) 
                return -1;
        }               
        return answer;
    }
}