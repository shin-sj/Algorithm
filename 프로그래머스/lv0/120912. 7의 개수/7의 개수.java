class Solution {
    public int solution(int[] array) {
        int answer = 0;

        for (int i=0; i < array.length; i++) {
            String tmp = String.valueOf(array[i]);
            if(tmp.contains("7")) {
                String[] array1 = tmp.split("");
                for(String a : array1) {
                    if(a.equals("7")) 
                        answer += 1;
                }
                
            }
            
        }
        return answer;
    }
}