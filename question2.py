def find_palindromes(str):
	    
	    palindromes = []
	    
	    if str:
	        str = str.lower()
	        for i in range(len(str)):
	            for j in range(0, i):
	                chunk = str [j:i + 1]
	                if chunk == chunk[::-1]:
	                    palindromes.append(chunk)
	
	    print "->", len(palindromes), palindromes
	    
	    if palindromes:
	        return max(palindromes, key=len)
	    else:
	        return None
	
	# main
	def question2(a):
	    return find_palindromes(a)
	
	# testcases
	print "\nAnswer 2:"