import java.util.*;


public class Solution {
    public String convertToTitle(int n) {
       
        char[] check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
        String result = "";
        
        String sol = recurse(result,n,check);

        return sol;

    }

    public static String recurse(String result,int n,char[] check)
    {

        String sol = result;

        if (n <= 0)
            return sol;
        if (n <= 26){
            sol += check[n-1];
            return sol ;
        }
        else
            {
                int rem = n%26;
                if (rem > 0)
                    sol += check[n%26-1];
                else
                    sol += check[25];
                n = n - 26;
                return recurse(sol,n,check);
            }
     }       

     public static void main(String[] args)
     {

        Solution obj = new Solution();

        System.out.println(obj.convertToTitle(26));
        System.out.println(obj.convertToTitle(52));
        System.out.println(obj.convertToTitle(27));
        System.out.println(obj.convertToTitle(54));
        System.out.println(obj.convertToTitle(58));
        System.out.println(obj.convertToTitle(53));


     }
        
}