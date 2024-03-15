import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
//	static pq_node [][] dist_list ;
	static ArrayList<Node> [] matrix;
	
	static class Node implements Comparable<Node> {
		
		int number;
		int distance;
		
		Node(int number, int distance) {
			this.number = number;
			this.distance = distance;
		}
		
		int getDistance() {
			return this.distance;
		}
		
		int getNumber() {
			return this.number;
		}
		
		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return this.distance - o.distance;
		}
	}
	
	static class pq_node implements Comparable<pq_node> {
		ArrayList<Integer> route;
		int dist;
		int node;
		
		pq_node(ArrayList<Integer> route, int dist) {
			this.route = route;
			this.dist = dist;
		}
		
		pq_node(ArrayList<Integer> route, int dist, int node) {
			this.route = route;
			this.dist = dist;
			this.node = node;
		}
		
		public ArrayList<Integer> getRoute () {
			return this.route;
		}

		@Override
		public int compareTo(pq_node o) {
			// TODO Auto-generated method stub
			return 0;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		matrix = new ArrayList [N + 1];
//		dist_list = new pq_node [N + 1][N + 1];
		for (int i = 0; i < N + 1; i++) {
			for (int j = 0; j < N + 1; j++) {
				ArrayList<Integer> route = new ArrayList<>();
//				pq_node max_pq = new pq_node(route, Integer.MAX_VALUE);
//				dist_list[i][j] = max_pq;
			}
		}
		
		for (int i = 0; i < N + 1; i++) {
			matrix[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());;
			int b = Integer.parseInt(st.nextToken());;
			int dist = Integer.parseInt(st.nextToken());;
			
			matrix[a].add(new Node(b, dist));
			matrix[b].add(new Node(a, dist));
		}
		
		for (int i = 1; i < N + 1; i++) {
			dijkstra(i);
		}
	}

	private static void dijkstra(int i) {
		PriorityQueue<pq_node> pq = new PriorityQueue<>();
		ArrayList<Integer> route = new ArrayList<>();
		pq.add(new pq_node(route, 0, i));
		pq_node [] dist_list = new pq_node [N + 1];
		for (int j = 0; j < N + 1; j++) {
			pq_node max_pq = new pq_node(route, Integer.MAX_VALUE);
			dist_list[j] = max_pq;
		}
		dist_list[i] = new pq_node(route, 0, i);
		
		while (!pq.isEmpty()) {
			int cur_dist;
			int cur_node;
			pq_node cur_pq = pq.poll();
			cur_dist = cur_pq.dist;
			cur_node = cur_pq.node;
			
			if (dist_list[cur_node].dist < cur_dist) continue;
			
			for (Node next_pq : matrix[cur_node]) {
				int next_node = next_pq.number;
				int next_dist = next_pq.distance + cur_dist;
				
				if (dist_list[next_node].dist > next_dist) {
					dist_list[next_node].dist = next_dist;
					ArrayList<Integer> next_route = (ArrayList<Integer>) cur_pq.route.clone();
					next_route.add(next_node);
					dist_list[next_node].route = next_route;
					pq.add(new pq_node(next_route, next_dist, next_node));
				}
			}
		}
		
		for (int j = 1; j < N + 1; j++) {
			pq_node print = dist_list[j];
//			System.out.print(Arrays.toString(print.route.toArray()) + ", ");
			if (print.route.isEmpty()) {
				System.out.print("-" + " ");
			} else {
				System.out.print(print.route.get(0) + " ");
			}
		}
		System.out.println("");
	}
}
