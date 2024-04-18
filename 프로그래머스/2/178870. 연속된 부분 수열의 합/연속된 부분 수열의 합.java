class Solution {
    public int[] solution(int[] sequence, int k) {
        int num = 0;
        int start = 0;
        int[] answer = {0, 0};
        int min_num = 1000000;
        
        for (int i = 0; i < sequence.length; i++) {
            num += sequence[i];
            while (num > k) {
                num -= sequence[start];
                start += 1;
            }
            
            if (num == k) {
                if (min_num > i - start) {
                    min_num = i - start;
                    answer[0] = start;
                    answer[1] = i;
                }
            }
        }
        return answer;
    }
}