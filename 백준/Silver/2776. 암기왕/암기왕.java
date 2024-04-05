import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
	
	static int T;
	static int N;
	static int M;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   //할당된 버퍼에 값 넣어주기
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		T = Integer.parseInt(st.nextToken());
		for (int test_case = 0; test_case < T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			String [] yeon = br.readLine().split(" ");
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			String [] min = br.readLine().split(" ");
			TreeMap<String, String> yeon_map = new TreeMap<>();
			for (String k : yeon) {
				yeon_map.put(k, k);
			}
			for (String k : min) {
				if (yeon_map.containsKey(k)) {
					bw.write(1+"\n");   //버퍼에 있는 값 전부 출력
				} else {
					bw.write(0+"\n");
				}
			}
		}
		bw.flush();   //남아있는 데이터를 모두 출력시킴
		bw.close();   //스트림을 닫음
	}
}
