import collections

class treeNode:
	def __init__(self, val=0, left=None, right=None):
		self.left = left
		self.right = right
		self.val = val

def preorder(root):
	if not root:
		return []
	ret = []
	stk = [root]
	while stk:
		cur = stk.pop()
		ret.append(cur.val)
		if cur.right:
			stk.append(cur.right)
		if cur.left:
			stk.append(cur.left)
	return ret


def inorder(root):
	if not root:
		return []
	ret = []
	stk = []
	
	while root:
		stk.append(root)
		root = root.left

	while root or stk:
		while root:
			stk.append(root)
			root = root.left
		root = stk.pop()
		ret.append(root.val)	
		root = root.right
		
	return ret


def postorder(root):
	if not root:
		return []
	ret = []
	stk = [root, root]

	while stk:
		cur = stk.pop()
		if stk and cur.val == stk[-1].val:
			if cur.right:
				stk.append(cur.right)
				stk.append(cur.right)
			if cur.left:
				stk.append(cur.left)
				stk.append(cur.left)
		else:
			ret.append(cur.val)
	return ret

def levelorder(root):
	if not root:
		return []

	ret = []
	queue = collections.deque([root])
	level = 0
	while queue:
		for i in range(len(queue)):
			node = queue.popleft()
			ret.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		level += 1		

	return ret




def main():
	root = treeNode(5)
	root.left = treeNode(3)
	root.right = treeNode(15)
	root.right.left = treeNode(9)
	root.right.right = treeNode(20)
	
	print(preorder(root))
	print(inorder(root))
	print(postorder(root))
	print(levelorder(root))


if __name__ == "__main__":
	main()