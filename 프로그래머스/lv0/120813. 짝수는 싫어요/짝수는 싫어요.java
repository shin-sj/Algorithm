import java.util.*;
class Solution {
    public ArrayList solution(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for(int i = 1; i <= n; i+=2) 
                list.add(i);
        return list;
    }
}