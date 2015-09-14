import java.util.*;



class LongestConsecutiveSequence{

	static int LCS(int[] arr)
	{

		if (arr.length == 0)
			return 0;


		int result = 1;
		Set<Integer> check = new HashSet<Integer>();

		for (int i : arr)
		{
			check.add(i);
		}

		for(int i : arr)
		{

			int lower = i - 1;
			int higher = i + 1;
			int count = 1;

			while(check.contains(lower))
			{
				count++;
				check.remove(lower);
				lower--;
			}

			while(check.contains(higher))
			{
				count++;
				check.remove(higher);
				higher++;
			}

			result = Math.max(count,result);
		
		}

	return result;
	}





	public static void main(String[] args) {

		int[] ip = {100, 4, 200, 1, 3, 2,0,5};

		System.out.println(LCS(ip));
		
	}
}