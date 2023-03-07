import java.util.*;
class Solution {
    int[] dx = {0, 0, 1, -1};
    int[] dy = {1, -1, 0, 0};
    
    public int solution(int[][] maps) {
        int answer = 0;
        int[][] visited = new int[maps.length][maps[0].length];
        // System.out.println(visited);
        bfs(maps, visited);
        answer = visited[maps.length-1][maps[0].length-1];
        
        if(answer == 0)
            return -1;
        else
            return answer;
    }
    
    public void bfs(int[][] maps, int[][] visited) {
        int x = 0;
        int y = 0;
        visited[x][y] = 1;
        Queue<int[]> queue  = new LinkedList<>();
        queue .add(new int[]{x, y});
        
        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int cx = current[0];
            int cy = current[1];
            
            for(int i = 0; i < 4; i++) {
                int xx = cx + dx[i];
                int yy = cy + dy[i];
                
                if(xx < 0 || xx >= maps.length || yy < 0 || yy >= maps[0].length)
                    continue;
                if(visited[xx][yy] == 0 && maps[xx][yy] == 1) {
                    visited[xx][yy] = visited[cx][cy] + 1;
                    queue.add(new int[]{xx, yy});
                }
            }
        }
    }
    
}