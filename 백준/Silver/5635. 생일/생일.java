import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
import java.util.StringTokenizer;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
 
        String max = "";
        String min = "";
        int maxBirth = Integer.MAX_VALUE;
        int minBirth = Integer.MIN_VALUE;
 
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();
            int tempBirth = 0;
            tempBirth += Integer.parseInt(st.nextToken());
            tempBirth += Integer.parseInt(st.nextToken()) * 100;
            tempBirth += Integer.parseInt(st.nextToken()) * 10000;
 
            if(maxBirth > tempBirth) {
                maxBirth = tempBirth;
                max = temp;
            }
            if(minBirth < tempBirth) {
                minBirth = tempBirth;
                min = temp;
            }
        }
        System.out.println(min);
        System.out.println(max);
    }
}