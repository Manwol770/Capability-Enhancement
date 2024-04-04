import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static ArrayList<Node> [] graph;
	static int [] visited;
	
	static class Node implements Comparable<Node> {
		int dist;
		int node;
		
		Node(int node, int dist) {
			this.dist = dist;
			this.node = node;
		}
		
		public int getDist() {
			return this.dist;
		}
		
		public int getNode() {
			return this.node;
		}
		
		@Override
		public int compareTo(Node o) {
			return this.dist - o.dist;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new ArrayList [N+1];
		visited = new int [N+1];
		Arrays.fill(visited, Integer.MAX_VALUE);
		for (int i = 0; i < N + 1; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i =0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			Integer a = Integer.parseInt(st.nextToken());
			Integer b = Integer.parseInt(st.nextToken());
			Integer c = Integer.parseInt(st.nextToken());
			
			graph[a].add(new Node(b, c));
			graph[b].add(new Node(a, c));
		}
		
		st = new StringTokenizer(br.readLine());
		Integer start = Integer.parseInt(st.nextToken());
		Integer end = Integer.parseInt(st.nextToken());
		
		dik(start, end);
		System.out.println(visited[end]);
	}
	
	public static void dik(int start, int end) {
		visited[start] = 0;
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		
		while (!pq.isEmpty()) {
//			System.out.println(Arrays.toString(visited));
			Node cul = pq.poll();
			int cul_node = cul.node;
			int cul_dist = cul.dist;
			if (visited[cul_node] < cul.dist) continue;
			
			for (Node next : graph[cul_node]) {
				int next_node = next.node;
				int next_dist = visited[cul_node] + next.dist;
				
				if(visited[next_node] > visited[cul_node] + next.dist) {
					visited[next_node] = next_dist;
					pq.add(new Node(next_node, next_dist));
				}
			}
		}
	}
}
