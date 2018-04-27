class TreeNode:
	def __init__(self, val, parent, left, rigth):
		self.val = val
		self.parent = parent
		self.left = left
		self.rigth = rigth


# given a ordered list, generate a balanced binary search tree

def genBalance(a):
	return _genBalance(a, None)

def _genBalance(a, parent):
	n = len(a)

	if n == 0:
		return None
	else:
		l = a[:n//2]
		r = a[n//2+1:]
		
		root = TreeNode(None, parent, None, None)
		root.val = a[n//2]
		root.left = _genBalance(l, root) 
		root.rigth = _genBalance(r, root)
	
		return root

def printTreeInOrder(root):
	if root == None:
		return
	else:		
		printTreeInOrder(root.left)
		print(root.val)
		printTreeInOrder(root.rigth)


def printLevelOrderTraversal(root):
	q = [root]
	while q:
		n = q.pop(0)
		print(n.val)
		if n.left is not None:
			q.append(n.left)
		if n.rigth is not None:
			q.append(n.rigth)


def insert(root, value):
	if value <= root.val and root.left is None:
		root.left = TreeNode(value, root, None, None)
	elif value > root.val and root.rigth is None:
		root.rigth = TreeNode(value, root, None, None)
	elif value <= root.val:
		insert(root.left, value)
	else:
		insert(root.rigth, value)




def main():
	node = genBalance([1,2,3,4,12,30,80,90])
	printTreeInOrder(node)
	insert(node, 31)
	print()
	printTreeInOrder(node)
	#printLevelOrderTraversal(node)
if __name__ == '__main__':
	main()