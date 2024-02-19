import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_1 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testcase = Integer.parseInt(br.readLine());
		
		for (int i=1; i <= testcase; i++) {
			boolean [] check = new boolean[10];
			boolean flag = false;
			
			for (int j=0; j <= 9; j++) {
				check[j] = false;
			}
			int num = Integer.parseInt(br.readLine());
			
			for (int j=1;;j++) {
				String [] s = String.valueOf(num * j).split("");
//				System.out.println(Arrays.toString(s));
				for (int z=0; z < s.length; z++) {
					if (check[Integer.parseInt(s[z])]) {
						continue;
					}
					check[Integer.parseInt(s[z])] = true;
				}
				flag = true;
				for (int z=0; z<=9; z++) {
					if (check[z]) {
						continue;
					}
					flag = false;
				}
				if (flag) {
					System.out.println("#"+ i + " " + j * num);
					break;
				}
			}
		}
	}
}
