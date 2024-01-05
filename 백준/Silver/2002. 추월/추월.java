import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		ArrayList<String> carlist_enter = new ArrayList<String>();
		ArrayList<String> carlist_exit = new ArrayList<String>();
		
		for(int i = 0; i < n; i++) {
			carlist_enter.add(sc.next());
		}
		
		for(int i = 0; i < n; i++) {
			carlist_exit.add(sc.next());
		}
		
//		System.out.println(carlist_enter);
//		System.out.println(carlist_exit);
		
		String cur = "";
		int cur_num = 0;
		int cnt = 0;
		
		for(int i = 0; i < n; i++) {
			cur = carlist_enter.get(i);
			for(int j = 0; j < n; j++) {
//				System.out.println(cur);
//				System.out.println(carlist_exit.get(j));
//				System.out.println(cur.equals(carlist_exit.get(j)));
				if(cur.equals(carlist_exit.get(j))) {
					if(cur_num <= j) {
						cnt += 1;
						cur_num = j;
						break;
					}
					else {
						break;
					}
				}
			}
		}
		System.out.println(n - cnt);
	}
}