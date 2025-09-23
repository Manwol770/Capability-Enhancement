import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static ArrayList<Node> [] lis;
	static int INF = Integer.MAX_VALUE;
	
	static class Node implements Comparable<Node>{
		private int node;
		private int distance;
		
		public Node(int node, int distance) {
			this.node = node;
			this.distance = distance;
		}
		
		public int getNode() {
			return node;
		}
		
		public int getDistance() {
			return distance;
		}

		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return this.distance - o.distance;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		lis = new ArrayList [N + 1];
		
		for (int i = 0; i < lis.length; i++) {
			lis[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int dis = Integer.parseInt(st.nextToken());
			Node node1 = new Node(a, dis);
			Node node2 = new Node(b, dis);
			
			lis[a].add(node2);
			lis[b].add(node1);
//			System.out.println(a + " " + b + " " + dis);
		}
		
		Dijkstra(1, N);
	}
	
	public static void Dijkstra (int start, int end) {
		int [] dist = new int [N + 1];
		PriorityQueue<Node> pq = new PriorityQueue<>();
		
		for (int i = 0; i < N + 1; i++) {
			dist[i] = INF;
		}

		dist[start] = 0;
		Node start_node = new Node(start, 0);
		pq.add(start_node);
		
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int cur_dist = node.distance;
			int cur_node = node.node;
			if (dist[cur_node] < cur_dist) continue;
//			System.out.println(cur_dist + " " + cur_node);
//			System.out.println(dist[cur_node]);
//			System.out.println(lis[cur_node]);
			
			for (Node next : lis[cur_node]) {
				int next_node = next.node;
				int next_dist = next.distance + cur_dist;
//				System.out.println(cur_node + " " + next_node + " " + cur_dist + " " + next_dist);
				
				if (dist[next_node] > next_dist) {
					dist[next_node] = next_dist;
					pq.add(new Node(next_node, next_dist));
//					System.out.println(cur_node + " " + next_dist + " " + next_node + " ");
//					System.out.println(Arrays.toString(dist));
				}
			}
		}
		System.out.println(dist[N]);
	}
}
