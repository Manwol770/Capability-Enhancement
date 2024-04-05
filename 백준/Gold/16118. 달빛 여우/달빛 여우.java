import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int [][] visited;
	static ArrayList<Fox> [] graph;
	
	static class Fox implements Comparable<Fox> {
		int dist;
		int node;
		
		Fox(int node, int dist) {
			this.node = node;
			this.dist = dist;
		}
		
		@Override
		public int compareTo(Fox o) {
			return this.dist - o.dist;
		}
	}
	
	static class Wolf implements Comparable<Wolf> {
		int dist;
		int node;
		int fast;
		
		Wolf (int node, int dist, int fast) {
			this.node = node;
			this.dist = dist;
			this.fast = fast;
		}
		@Override
		public int compareTo(Wolf o) {
			return this.dist - o.dist;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new ArrayList [N+1];
		visited = new int[3][N+1];
		
		for (int i = 0; i < 3; i++) {
			Arrays.fill(visited[i], Integer.MAX_VALUE);
		}
		
		for (int i = 0; i < N + 1; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			graph[a].add(new Fox(b, c * 2));
			graph[b].add(new Fox(a, c * 2));
		}
		fox_dik(1);
		wolf_dik(1);
		
		int print_num = 0;
		
		for (int i = 2; i < N+1; i++) {
			if (visited[0][i] < visited[1][i] && visited[0][i] < visited[2][i]) {
				print_num += 1;
			}
		}
//		System.out.println(Arrays.deepToString(visited));
		System.out.println(print_num);
	}
	
	public static void fox_dik(int start) {
		PriorityQueue<Fox> pq = new PriorityQueue<>();
		visited[0][start] = 0;
		pq.add(new Fox(start, 0));
		
		while (!pq.isEmpty()) {
			Fox cul = pq.poll();
			int cul_node = cul.node;
			int cul_dist = cul.dist;
			
			if (cul_dist > visited[0][cul_node]) continue;
			
			for (Fox next : graph[cul_node]) {
				int next_node = next.node;
				int next_dist = visited[0][cul_node] + next.dist;
				
				if (visited[0][next_node] > next_dist) {
					visited[0][next_node] = next_dist;
					pq.add(new Fox(next_node, next_dist));
				}
			}
		}
	}
	
	public static void wolf_dik(int start) {
		PriorityQueue<Wolf> pq = new PriorityQueue<>();
		pq.add(new Wolf(start, 0, 1));
		visited[1][1] = 0;
		
		while (!pq.isEmpty()) {
			Wolf cul = pq.poll();
			int cul_node = cul.node;
			int cul_dist = cul.dist;
			int cul_fast = cul.fast;
			int next_fast;
			
			if(visited[cul_fast][cul_node] < cul_dist) continue;
			
			for (Fox next : graph[cul_node]) {
				int next_node = next.node;
				int next_dist;
				if (cul_fast == 1) {
					next_dist = cul_dist + next.dist / 2;
					next_fast = 2;
				} else {
					next_dist = cul_dist + next.dist * 2;
					next_fast = 1;
				}
				
				if (visited[next_fast][next_node] > next_dist) {
					visited[next_fast][next_node] = next_dist;
					pq.add(new Wolf(next_node, next_dist, next_fast));
				};
			}
		}
	}
}
