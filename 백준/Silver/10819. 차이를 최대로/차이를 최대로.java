import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {
	static int N, print_num;
	static int [] A;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		print_num = 0;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(st.nextToken());
		A = new int [N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		permutation(A, 0);
		bw.write(print_num + "\n");
		bw.flush();
		bw.close();
	}
	
	public static void permutation(int [] arr, int depth) {
		if (depth == N - 1) {
			int sum_num = 0;
			for (int i = 0; i < N - 1; i++) {
				sum_num += Math.abs(arr[i] - arr[i+1]);
			}
			if (print_num < sum_num) {
//				System.out.println(Arrays.toString(arr));
				print_num = sum_num;
			}
		}
		
		for (int i=depth; i<N; i++) {
			swap(arr, depth, i);
			permutation(arr, depth + 1);
			swap(arr, depth, i);
		}
	}
	
	public static void swap(int[] arr, int depth, int i) {
		int temp = arr[depth];
		arr[depth] = arr[i];
		arr[i] = temp;
	}
}