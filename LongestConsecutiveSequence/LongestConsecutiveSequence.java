import java.util.*;



class LongestConsecutiveSequence{

	static int LCS(int[] arr)
	{

		int result = 1;
		HashMap<Integer,Integer> check = new HashMap<Integer,Integer>();

		for(int i : arr)
		{

			int tempres = 1;

			if (check.get(i+1) != null && check.get(i+1) >= tempres)
			{
				tempres = check.get(i+1) + 1;
				check.put(i+1,tempres);
				if (check.get(i-1) != null)
					check.put(i-1,tempres);

			}


			if (check.get(i-1) != null && check.get(i-1) >= tempres)
			{
				tempres = check.get(i-1) +  1;
				check.put(i-1,tempres);
				if (check.get(i+1) != null)
					check.put(i+1,tempres);

			}

			check.put(i,tempres);

			if(tempres > result)
				result = tempres;
		}

		return result;
	}





	public static void main(String[] args) {

		int[] ip = {100, 4, 200, 1, 3, 2,0,5};

		System.out.println(LCS(ip));
		
	}
}