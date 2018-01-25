class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


	class LinkedList(object):
	    def __init__(self, head=None):
	        self.head = head
	        
	    def append(self, new_node):
	        current = self.head
	        if self.head:
	            while current.next:
	                current = current.next
	            current.next = new_node
	        else:
	            self.head = new_node
	

	    def nNodeFromLast(self, m):
	        main_ptr = self.head
	        ref_ptr = self.head 
	     
	        c = 0
	        if(self.head is not None):
	            while(c < m):
	                if(ref_ptr is None):
	                    print "ERROR: %d is greater than the no. of nodes in list" % (m)
	     return
	
	          ref_ptr = ref_ptr.next
	          c += 1
	        while(ref_ptr is not None):
	            main_ptr = main_ptr.next
	            ref_ptr = ref_ptr.next
	        
	        return main_ptr
	    
	# main
	def question5(ll, m):
	    if ll:
	        return ll.nNodeFromLast(m)
	# testcases
	print "\nAnswer 5:"
	

