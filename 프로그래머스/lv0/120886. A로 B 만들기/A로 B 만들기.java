import java.util.*;

class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        char[] tmp1 = before.toCharArray();
        char[] tmp2 = after.toCharArray();
        Arrays.sort(tmp1);
        Arrays.sort(tmp2);
        
        String bString = new String(tmp1);
        String aString = new String(tmp2);
        if(bString.equals(aString)) {
            return 1;
        }
        
        
        return 0;
    }
}