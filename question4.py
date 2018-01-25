Class MyClass:
	 
	    def __init__(self, value):
	        self.value = value
	        self.left = None
	        self.right = None
	        
	    def children(self):
	        return [self.left, self.right]
	    
	    def show(self):
	        l = self.left.value if (self.left) else None
	        r = self.right.value if (self.right) else None
	        print "{} -> {}, {}".format(self.value, l, r)
	        
	# binary search tree
	class BST(object):
	    def __init__(self, root):
	        self.root = Element(root)
	        
	    # insert new node
	    def insert(self, new_value):
	        self.insert_helper(self.root, new_value)
	        
	    # find the correct location for the new node in the tree
	    def insert_helper(self, current, new_value):
	        if current.value < new_value:
	            if current.right:
	                self.insert_helper(current.right, new_value)
	            else:
	                current.right = MyClass(new_value)
	        else:
	            if current.left:
	                self.insert_helper(current.left, new_value)
	            else:
	                current.left = MyClass (new_value)
	

	    def show(self):
	        self.root.show()
	        children = self.root.children()
	        while(len(children) > 0):
	            child = children.pop(0)
	            if child:
	                child.show()
	                children = children + child.children()
	                
	
	def buildTree(t, n): 
	    if T and n in T:
	        children = T[node]
	        for index, child in enumerate(children):
	            if child == 1:
	                t.insert(index)
	                buildTree(t, index)

	def lca(root, n1, n2):
	    if root is None:
	        return None
	    if(root.value > n1 and root.value > n2):
	        return lca(root.left, n1, n2)
	    if(root.value < n1 and root.value < n2):
	        return lca(root.right, n1, n2)
	 
	    return root
	
	# main
	def question4(T, r, n1, n2):
	    t = BST(r)
	    buildTree(t, r)
	    return lca(t.root, n1, n2)
