import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj1292
{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());

        int start = Integer.parseInt(stk.nextToken());
        int end = Integer.parseInt(stk.nextToken());

        ArrayList<Integer> list = new ArrayList<>();
        
        int cnt = 1; 

        for(int i=1; i<1001; i++)
        {
            for(int j=1; j<i+1; j++)
            {
                list.add(cnt);
            }
            cnt ++;
        }

        int ans = 0;

        for(int i=start-1; i<end; i++)
        {
            ans += list.get(i);
            //System.out.println(list.get(i));
        }
        System.out.println(ans);

    }
}
