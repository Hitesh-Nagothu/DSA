# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    
	depth_descendantOne=find_depth(topAncestor,descendantOne)
	depth_descendantTwo=find_depth(topAncestor,descendantTwo)
	
	if depth_descendantOne > depth_descendantTwo:	
		while depth_descendantOne!=depth_descendantTwo:
			descendantOne=descendantOne.ancestor
			depth_descendantOne-=1
			
	elif depth_descendantOne < depth_descendantTwo:
		while depth_descendantOne!=depth_descendantTwo:
			descendantTwo=descendantTwo.ancestor
			depth_descendantTwo-=1
			
	#At this point, both descendant are at equal heights
	while descendantOne.ancestor !=descendantTwo.ancestor:
		descendantOne=descendantOne.ancestor
		descendantTwo=descendantTwo.ancestor
		
	return descendantOne.ancestor

def find_depth(topAncestor,descendant):
	
	depth=0
	while descendant!=topAncestor:
		descendant=descendant.ancestor
		depth+=1
		
	return depth


	
		
	
		
		
