def is_anagram(s1,t1):

	S1 = list(s1)
	# Sort a string and then compare with each other
	S1.sort()   # Quick sort O(n*log(n))
	return s1 == t1

	# Find out sorted(possible substring of s) and compare with sorted(t).
	# @param {string, string} input strings

	def question1(s, t):
	    global debug
	    match_length = len(t)
	    pattern_length = len(s)
	    sorted_t = list(t)
	    sorted_t.sort()     # Quick sort O(n*log(n))
	
	for i in range(pattern_length - match_length + 1):
	       if debug:
	           print (s[i: i+match_length], t)
	       if is_anagram(s[i: i+match_length], sorted_t):
	           return True
	return False
	
	# Main program
	def main():
	    print question1("udacity", "ad")
	
	    if __name__ == '__main__':
	    main()
