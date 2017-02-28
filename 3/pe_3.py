# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?



x = 600851475143
small_prime = 2

while (x > small_prime): 
	if(x%small_prime==0):
		x = x/small_prime
		small_prime = 2
	else:
		small_prime+=1;
print ("Largest prime factor %d" % small_prime)