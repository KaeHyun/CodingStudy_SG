import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class boj2309
{
    /* 난쟁이의 키 합이 100이 됨 */
    public static void main(String[] args) throws IOException{
        BufferedReader rb = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> dwarfs = new ArrayList<>(); //가짜 난쟁이 저장 정보
        int sum = 0;

        for(int i=0; i <9; i++)
        {
            int dwarf = Integer.parseInt(rb.readLine());
            sum += dwarf;
            dwarfs.add(dwarf);
        }
        
        Collections.sort(dwarfs); // 오름차순 정렬
        //System.out.println(dwarfs);

        for(int i=0; i<8; i++)
        {
            for (int j=1; j<9; j++)
            {
                if(sum-dwarfs.get(i)-dwarfs.get(j) == 100)
                {
                    /*그냥 단순제거해버리면 arrayList에 변화를 주기 때문에 index 에러 발생 */
                    dwarfs.set(i, 0);
                    dwarfs.set(j, 0);
                    
                    Collections.sort(dwarfs); // 재정렬
                    for(int idx=2; idx<9; idx++)
                    {
                        System.out.println(dwarfs.get(idx));
                    }
                    return;
                }
            }
        }
    }
}