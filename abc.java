public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[] str = {'z','z','c','b','z','c','h','f','i','h','i'};
		String strr = new String(str);
		System.out.println("string " + strr);
		List<Character> arr = new ArrayList(Arrays.asList(str));
		int[] dp = new int[str.length];
		
		int[] bit = new int[26];
		
		int m = 0;
		int n = 0;
		int last = 0;

		ArrayList<Integer> ans = new ArrayList();
		for(int i = 0; i < str.length; i++) {

			int ind = strr.substring(i + 1).indexOf(str[i]);
			if(ind >= 0) {
				ind += i + 1;
			}
			
			if(ind> 0) {
				
				if(i > n) {
					m = i;
					if(last > 0) {
						ans.add(last);
					}
					last = 0;
				}				
				n = ind;
				if(n - m + 1> last) {
					last = n - m + 1;
					System.out.println("ans " + last);
				}
			} else {

			}			
			if(i >= str.length - 1) {		

				n = i;
				if(n - m + 1 >= last) {
					last = n - m + 1;
					ans.add(last);
				}
			}						
		}
		System.out.println("asns");
		for(int num : ans) {
			System.out.println(num);
		}
		return ans;
		
	}