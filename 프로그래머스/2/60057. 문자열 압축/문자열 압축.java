import java.util.ArrayList;

class Solution {
    public int solution(String s) {
        String [] m_content = s.split("");
        int min_num = Integer.MAX_VALUE;
        String sumary_str;
        
        for (int i = 1; i <= s.length() / 2 + 1; i++) {
            sumary_str = my_string(m_content, i);
            // System.out.println(sumary_str);
            
            if (min_num > sumary_str.length()) {
                min_num = sumary_str.length();
            }
            
            // System.out.println(min_num);
        }
        int answer = min_num;
        return answer;
    }
    
    public static String my_string (String[] s, int i) {
        String cur_str;
        String next_str;
        String return_str;
        int count;
        int length;
        count = 1;
        cur_str = "";
        return_str = "";
        length = 0;
        for (int j = 0; j < i; j ++) {
            cur_str += s[j];
        }
        // System.out.println("**start : " + i + "**" + "s.length : " + s.length);
        
        for (int j = i; j <= s.length - i; j += i) {
            next_str = "";
            
            for (int z = 0; z < i; z++) {
                next_str = next_str + s[z + j];
            }
            
            // System.out.println("********************************");
            // System.out.println("count : " + count);
            // System.out.println("cur_str : " + cur_str);
            // System.out.println("next_str : " + next_str);
            // System.out.println("return_str : " + return_str);
            // System.out.println("length : " + length);
            // System.out.println("j : " + j);
            if (cur_str.equals(next_str)) {
                count += 1;
                length += i;
                // System.out.println("here?????");
                if (j + i > s.length - i) {
                    if (count != 1) {
                        // System.out.println("here??");
                        length += i;
                        return_str += count + cur_str;
                    } else {
                        // System.out.println("here?");
                        return_str += cur_str;
                        length += i;
                    }
                }
            } else {
                if (count != 1) {
                    // System.out.println("here???");
                    return_str += count + cur_str;
                    count = 1;
                    cur_str = next_str;
                    length += i;
                }
                else {
                    // System.out.println("here????");
                    return_str += cur_str;
                    cur_str = next_str;
                    length += i;
                }
            }
        }
        // System.out.println("r return_str : " + return_str);
        if (length < s.length) {
            for (int j = length; j < s.length; j++) {
                return_str += s[j];
            }
        }
        // System.out.println("rast return_str : " + return_str);
        return return_str;
    }
}