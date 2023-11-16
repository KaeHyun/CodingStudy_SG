import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class boj3460 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        for(int i=0; i < tc; i++)
        {
            int target = Integer.parseInt(br.readLine());

            int index = 0;

            while(target>0)
            {
                if(target % 2 == 1)
                {
                    System.out.print(index + " ");
                }
                target /= 2;
                index ++;
            }
            System.out.println(); //줄바꿈
        }

    }
    
}
