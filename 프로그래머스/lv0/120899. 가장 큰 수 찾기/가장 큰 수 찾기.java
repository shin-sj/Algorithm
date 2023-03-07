class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int maxNum = -1;
        int idx = -1;
        for(int i = 0; i < array.length; i++) {
            if (array[i] > maxNum) {
                maxNum = array[i];
                idx = i;
            }
        }
        answer[0] = maxNum;
        answer[1] = idx;
        return answer;
    }
}