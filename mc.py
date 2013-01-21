import time; 
import os; 
from random import randrange ; 

# Settings 
# -------------------------------------
# Generate a list of hackers that will be doing lighting talks. 	
hackers = ['one', 'two', 'three']  
# How many seconds each talk will last 
length_of_talk = 120  

# http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
def TimeWords ( timeLeft ) :
	return {
		120: "Start", 
		113: "30th prime number",
		108: "108 (or nine dozen) is an 'abundant' number and a 'semiperfect' number and a 'tetranacci' number.",
		 90: "1/4 done, 90 is divisible by the sum of its base 10 digits, thus it is a Harshad number", 
		 83: "83 is the sum of three consecutive primes (23 + 29 + 31) as well as the sum of five consecutive primes (11 + 13 + 17 + 19 + 23).",
		 73: "73 is the atomic number of tantalum (Ta)", 
		 60: "1/2 done, Being three times twenty, 60 is called 'three score' in some older literature.", 
		 53: "53 can not be expressed as the sum of any integer and its base 10 digits, making 53 a self number.",
		 42: "Answer to the Ultimate Question of Life, the Universe, and Everything", 
		 30: "Start finishing up your talk", 
		 13: "Its lucky for me.", 
		  4: "Count with me!", 
		  3: "So close!", 
		  2: "Get ready to clap!", 
		  1: "The last second!", 
		  0: "Time is UP ! ", 
	}.get( timeLeft, '' ) 


def StartTalk( name, timeout=120 ):
	print ( name + "'s turn to do a lighting talk. " )
	print ( name + " Will have " + str( timeout ) + " seconds to do his/her lighting talk" )
	
	# wait on user input to start the talk. 
	input("Press Enter to start the talk")	
	
	# start the talk 
	while( timeout >= 0 ) :
		print ( str( timeout ) + " Seconds left " , end='' ) 
		print ( TimeWords( timeout ) ) 
		timeout -= 1 
		time.sleep( 1 ) ;
	 
	print ("Thank you " + name + " for doing your talk!" ) 
	
	# Put some space at the end of the sequence 
	print ("\n\n")
	

# Run talks until we are out of hackers 
while( len(hackers) > 0 ) : 
	# pick a random hacker 
	random_index = randrange(0,len(hackers))

	# start the talk 
	StartTalk( hackers[ random_index ], length_of_talk ) 

	# Remove the hacker from the list. 
	del hackers[ random_index ] 
	
	
	
	
