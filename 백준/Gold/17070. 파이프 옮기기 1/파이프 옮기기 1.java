import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
	static int N;
	static int [][] matrix;
	static int [][][] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		matrix = new int [N][];
		visited = new int[N][N][3];
		
		for (int i = 0; i < N; i++) {
			String [] cul_row = br.readLine().split(" ");
			matrix[i] = Stream.of(cul_row).mapToInt(Integer::parseInt).toArray();
			for (int j = 0; j < N; j++) {
				Arrays.fill(visited[i][j], -1);
			}
		}
		
		System.out.println(dfs(0,1,0));
	}
	
	public static int dfs(int x, int y, int dr) {
		int tmp = 0;
		
		if (x == N - 1 && y == N -1) {
			visited[x][y][dr] = 1;
			return 1;
		}
		
		if (visited[x][y][dr] != -1) {
			return visited[x][y][dr];
		}
		
		if ((dr == 0 || dr == 1) && y < N - 1 && matrix[x][y+1] != 1) {
			tmp += dfs(x, y+1, 0);
		}
		
		if (x < N - 1 && y < N - 1 && matrix[x][y+1] != 1 && matrix[x+1][y] != 1 && matrix[x+1][y+1] != 1) {
			tmp += dfs(x+1, y+1, 1);
		}
		
		if ((dr == 1 || dr == 2) && x < N - 1 && matrix[x+1][y] != 1) {
			tmp += dfs(x+1, y, 2);
		}
		
		visited[x][y][dr] = tmp;
		return tmp;
	}
}
