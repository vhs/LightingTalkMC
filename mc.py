"""
Lighting talk script used for Vancouver Hackspace (VHS)
Super Happy Hacker House (SHHH)
"""
import time
from random import randrange
import sys

# Settings
# -------------------------------------
# Generate a list of HACKERS that will be doing lighting talks.
if len(sys.argv) > 1:
    HACKERS=sys.argv[1:]
else:
    HACKERS = ['one', 'two', 'three']
# How many seconds each talk will last
LENGTH_OF_TALK = 120

# http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
def time_words ( time_left ) :
    """Get a neat factoid about each time interval"""
    return {
            120: "Start",
            113: "30th prime number",
            108: "108 (or nine dozen) is an 'abundant' number and a "
                "'semiperfect' number and a 'tetranacci' number.",
            90: "1/4 done, 90 is divisible by the sum of its base 10 digits, "
                "thus it is a Harshad number",
            83: "83 is the sum of three consecutive primes (23 + 29 + 31) as "
                "well as the sum of five consecutive primes "
                "(11 + 13 + 17 + 19 + 23).",
            73: "73 is the atomic number of tantalum (Ta)",
            60: "1/2 done, Being three times twenty, 60 is called "
                "'three score' in some older literature.",
            53: "53 can not be expressed as the sum of any integer and its "
                "base 10 digits, making 53 a self number.",
            42: "Answer to the Ultimate Question of Life"
                ", the Universe, and Everything",
            30: "Start finishing up your talk",
            13: "Its lucky for me.",
            4: "Count with me!",
            3: "So close!",
            2: "Get ready to clap!",
            1: "The last second!",
            0: "Time is UP ! ",
            }.get( time_left, '' )


def start_talk( name, timeout=120 ):
    """Actually run a talk"""
    print ( name + "'s turn to do a lighting talk. " )
    print ( name + " Will have %d seconds to do his/her lighting talk"
            % timeout)

    # wait on user input to start the talk.
    #SECURITY HOLE FIXED: Input is eval(read(stdin))
    raw_input("Press Enter to start the talk.")

    # start the talk
    while timeout >= 0:
        print ("%d Seconds left" % timeout)
        print ( time_words( timeout ) )
        timeout -= 1
        time.sleep( 1 )

    print ("Thank you " + name + " for doing your talk!" )

    # Put some space at the end of the sequence
    print ("\n\n")


def main():
    """Use __main__ to do magic and avoid pep8 issues."""
    # Run talks until we are out of hackers
    while( len(HACKERS) > 0 ) :
        # pick a random hacker
        random_index = randrange(0, len(HACKERS))

        # start the talk
        start_talk( HACKERS[ random_index ], LENGTH_OF_TALK )

        # Remove the hacker from the list.
        del HACKERS[ random_index ]



if __name__ == '__main__':
    main()
