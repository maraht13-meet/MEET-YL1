def divisors(n):
    n = int(n)
    for number in xrange(n) : 
    	if n%(number+1) == 0:
		print number+1


if __name__ == '__main__':
	n = raw_input("give me a number ")
	divisors(n)


  


