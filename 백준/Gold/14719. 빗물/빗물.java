import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
	static int  H, W, Max_H, Max_W;
	static int [] graph;
	static int [] water;
	static int print_num;
	
	static class Node implements Comparable<Node> {
		int height, node;
		
		Node(int heigh, int node){
			this.height = heigh;
			this.node = node;
		}
		
		@Override
		public int compareTo(Node o) {
			return o.height - this.height;
		}
	}
	
	public static void main(String[] args)  throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st  = new StringTokenizer(br.readLine());
		H = Integer.parseInt(st.nextToken());
		W = Integer.parseInt(st.nextToken());
		water =  new int [W];
		print_num = 0;
		Arrays.fill(water, -1);
		
//		graph  =  new int [W];
//		st = new StringTokenizer(br.readLine());
//		
//		for(int i = 0; i < W; i++) {
//			graph[i] =  Integer.parseInt(br.readLine());
//		}
		graph = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		
		PriorityQueue<Node>  pq = new PriorityQueue<>();
		for(int i = 0; i < W; i++) {
			pq.add(new Node(graph[i], i));
		}
		
		Node max_node = pq.poll();
		Max_H  = max_node.height;
		Max_W  = max_node.node;
		water[Max_W] = Max_H;
		
//		System.out.println(Arrays.toString(water));
		
		for(int i = 0; i < W - 1; i++) {
			Node cul_node = pq.poll();
			if (Max_W > cul_node.node) {
				for (int j = cul_node.node; j < Max_W; j++) {
					if (water[j] != -1) {
						break;
					} else {
						water[j] = cul_node.height;
						print_num += cul_node.height - graph[j];
					}
				}
			} else {
				for (int j = cul_node.node; j > Max_W; j--) {
					if (water[j] != -1) {
						break;
					} else {
						water[j] = cul_node.height;
						print_num += cul_node.height - graph[j];
					}
				}
			}
		}
//		System.out.println(Arrays.toString(water));
		bw.write(print_num + "\n");
		bw.flush();
		bw.close();
	}
}
