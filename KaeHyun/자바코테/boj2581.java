import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class boj2581 {
    public static void main(String[] args) throws IOException{
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int target1 = Integer.parseInt(br.readLine());
        int target2 = Integer.parseInt(br.readLine());

        ArrayList<Integer> prime_list = new ArrayList<>();

        for(int i=target1; i<target2+1; i++)
        {
            if(isPrime(i) && i != 1) //소수라면 
            {
                prime_list.add(i);
            }
        }

        int ans = 0;
        
        if(prime_list.size() == 0)
        {
            System.out.println(-1);
        }
        else
        {
            for(int i=0; i<prime_list.size(); i++)
            {
                ans += prime_list.get(i);
            }
            System.out.println(ans + " " + prime_list.get(0));
        }
    
   }

    private static boolean isPrime(int num)
        {
            for(int i =2; i<num; i++)
            {
                if(num % i == 0)
                {
                    return false;
                }
            }

            return true;
        }
}

