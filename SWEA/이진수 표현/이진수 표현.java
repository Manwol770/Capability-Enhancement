import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testcase = Integer.parseInt(br.readLine());
		
		for (int i=1; i<=testcase; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int lastNBit = (1 << (N)) - 1;  // 111...1 (길이 N)
            if( lastNBit == (M & lastNBit)){
                System.out.println("#" + i + " " + "ON");
            }else{
                System.out.println("#" + i + " " + "OFF");
            }
		}
	}
}
