import java.util.Arrays;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int count_1 = 0;
        int count_2 = 0;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        String [] arr = s.split("");
        // System.out.println(Arrays.toString(arr));
        for (String str : arr) {
            if( str.equals("(") ) {
                count_1 += 1;
            } else {
                count_2 += 1;
                if ( count_2 > count_1 ) {
                    return false;
                }
            }
        }
        
        if ( count_1 != count_2 ) {
            // System.out.println(count_1 + " " + count_2);
            answer = false;
        }

        return answer;
    }
}