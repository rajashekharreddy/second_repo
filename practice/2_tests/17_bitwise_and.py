"""
Write a function that returns the bitwise AND of all integers between M and N, inclusive.
int rangeBitwiseAnd(int m, int n) {
    int a = 0;
    while(m != n) {
        m >>= 1;
        n >>= 1;
        a++;
    }
    return m<<a; 
}

"""

def bitwise_and(m, n):
	val = 0
	while(m != n):

		m >>= 1
		n >>= 1
		val += 1
	print(m << val)



bitwise_and(2, 12)