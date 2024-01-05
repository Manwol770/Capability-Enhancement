import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	static ArrayList<Integer> right = new ArrayList<Integer>();
	static ArrayList<Integer> left = new ArrayList<Integer>();
	static int S;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		
		arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		sumarray(0, N/2, 0, left);
		sumarray(N/2, N, 0, right);
		
		Collections.sort(left);
		Collections.sort(right);
		
//		System.out.println(left);
//		System.out.println(right);
		
		long print_num = getCnt();
		
		if (S == 0 && print_num != 0) {
			System.out.println(print_num - 1);
		}
		else {
			System.out.println(print_num);
		}
	}
	
	public static void sumarray(int idx, int end, int sum, ArrayList<Integer> list) {
		
		if(idx == end) {
			list.add(sum);
			return;
		}
		
		sumarray(idx+1, end, sum + arr[idx], list);
		sumarray(idx+1, end, sum, list);
	}
	
	public static long getCnt() {
		
		int pl = 0;
		int pr = right.size() - 1;
		long cnt = 0;
		
		while(pl < left.size() && pr >= 0) {
			int sum = left.get(pl) + right.get(pr);
			
			if (sum == S) {
				
				int l = left.get(pl);
				int r = right.get(pr);
				
				long cnt1 = 0;
				while(pl < left.size() && left.get(pl) == l) {
					pl++;
					cnt1++;
				}
				
				long cnt2 = 0;
				while(pr >= 0 && right.get(pr) == r) {
					pr--;
					cnt2++;
				}
				
				cnt += cnt1 * cnt2;
			}
			else if (sum < S) {
				pl++;
			}
			else {
				pr--;
			}
		}
		
		return cnt;
	}
}
