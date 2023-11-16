import java.util.StringTokenizer;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;;



public class boj2501{
    public static void main(String[] args) throws IOException{

        /* 입출력 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine()); // 읽은 라인을 ""으로 자른다 

        /*String Tokenizer*/
        int N = Integer.parseInt(stk.nextToken());
        int M = Integer.parseInt(stk.nextToken());
        
        ArrayList<Integer> number = new ArrayList<>();

        for(int i=1; i<=N;i++)
        {
            if(N % i == 0)
            {
                number.add(i);
            }
        }

        int num_size = number.size();
        if(num_size < M)
        {
            System.out.println(0);
        }
        else{
            System.out.println(number.get(M-1));
        }
    }
}   