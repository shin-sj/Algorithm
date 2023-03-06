import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        
        String filter = "";
        
        char[] arr = my_string.toCharArray();
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] >=48 && arr[i] <= 57) {
				filter += arr[i];
			}
        }
        // System.out.println(filter);
        String[] transfer = new String [filter.length()];
        int[] answer = new int [filter.length()]; 
        for(int i = 0; i < filter.length(); i++) {
            transfer[i] = filter.charAt(i) + "";
            answer[i] = Integer.parseInt(transfer[i]);
        }
        Arrays.sort(answer);

        return answer;
    }
}