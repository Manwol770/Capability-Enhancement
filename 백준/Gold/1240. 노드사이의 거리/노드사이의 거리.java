import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static ArrayList<Integer []> [] adlist;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		adlist = new ArrayList [N + 1];
		
		for (int i = 0; i < N + 1; i++) {
			adlist[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < N - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			Integer [] addlist1 = {b, c};
			adlist[a].add(addlist1);
			Integer [] addlist2 = {a, c};
			adlist[b].add(addlist2);
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			djikstra(start, end);
		}
	}
	
	static class Node implements Comparable<Node> {
		int node;
		int distance;
		
		Node(int node, int distance) {
			this.node = node;
			this.distance = distance;
		}
		
		public int getDistance() {
			return this.distance;
		}
		
		public int getNode() {
			return this.node;
		}

		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return this.distance - o.distance;
		}
	}
	
	public static void djikstra(int start, int end) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		int [] dist = new int [N + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		
		Node start_node = new Node(start, 0);
		dist[start] = 0;
		pq.add(start_node);
		
		while (!pq.isEmpty()) {
			Node cul = pq.poll();
			int cul_node = cul.node;
			int cul_dist = cul.distance;
			
			if (cul_dist > dist[cul_node]) continue;
			
//			System.out.println(cul_node);
//			System.out.println(cul_dist);
			for (Integer[] next : adlist[cul_node]) {
				int next_node = next[0];
				int next_distance = next[1] + dist[cul_node];
				
				if (dist[next_node] > next_distance) {
					pq.add(new Node(next_node, next_distance));
					dist[next_node] = next_distance;
				}
			}
		}
		
		System.out.println(dist[end]);
	}
}
