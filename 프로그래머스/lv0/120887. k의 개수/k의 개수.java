class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String check = String.valueOf(k);
        
        for(int p = i; p <= j; p++){
            String tmp = String.valueOf(p);
            if(tmp.contains(check)) {
                String[] array = tmp.split("");
                for(String a : array) {
                    if (a.equals(check)) 
                        answer += 1;
                }
                              
            }
        }
        return answer;
    }
}