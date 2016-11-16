class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def preOrder(root):
    if root	!= None:
        print root.val, " ",
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
	if root!=None:
		inOrder(root.left)
		print root.val," ",
		inOrder(root.right)

def generateTrees(start, end):
	l = []
	if start>end:
		l.append(None)
		return l
	for i in range(start, end+1):
		left_subtrees = generateTrees(start, i-1)
		right_subtrees = generateTrees(i+1,end)
		for j in range(len(left_subtrees)):
			left = left_subtrees[j]
			for k in range(len(right_subtrees)):
				right = right_subtrees[k]
				root = TreeNode(i)
				root.left = left
				root.right = right
				l.append(root)
	return l

def addNodeBinaryTree(root,n):
	node = TreeNode(n)
	if root==None:
		root = node
		return root
	else:
		ptr = root
		while True:
			if n>=ptr.val:
				if ptr.right==None:
					ptr.right = node
					return root
				else:
					ptr = ptr.right
			else:
				if ptr.left == None:
					ptr.left = node
					return root
				else:
					ptr = ptr.left





n = [2,3,4,5,2,3,4,1,2,3,4,5]

root = None
for i in n:
	print ""
	inOrder(root)
	root = addNodeBinaryTree(root,i)
print ""
inOrder(root)
