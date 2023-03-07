import java.util.*;
import java.util.Map;
import java.util.Map.Entry;
class Solution {
    public String solution(String s) {
        String answer = "";
        char[] tmp = s.toCharArray();
        HashMap<Character, Integer> hm = new HashMap<>();
        
        for(char key1 : tmp) {
            hm.put(key1, hm.getOrDefault(key1, 0) + 1);
        }
        
        // System.out.print(hm);
        for(Entry<Character, Integer> entry: hm.entrySet()) {
            // System.out.println(entry.getKey() + entry.getValue());
            if(entry.getValue() == 1) {
                System.out.println(entry.getKey());
                answer += entry.getKey();
            }
        }
        char[] array = answer.toCharArray();
        Arrays.sort(array);
        answer = new String(array);
        return answer;
    }
}