import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int n;
		int w;
		int L;
		int sum;
		int cnt = 0;
		int plus_num = 0;
		
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> car = new ArrayList<>();
		
		n = sc.nextInt();
		w = sc.nextInt();
		L = sc.nextInt();
		
		int[] bridge = new int[w];
		
		for(int i = 0; i < n; i++) {
			car.add(sc.nextInt());
		}
		
		for(int i = 0; i < n; i++) {
			plus_num = car.get(i);
			sum = L + 1;
			while (sum > L) {
				sum = plus_num;
				int store = bridge[0];
				for(int j = w-1; j > 0; j--) {
					bridge[j] = bridge[j-1];
				}
				bridge[0] = 0;
				
				for(int j = 0; j < w; j++) {
					sum += bridge[j];
				}
				cnt += 1;
			}
			bridge[0] = plus_num;
		}
		System.out.println(cnt+w);
	}
}
