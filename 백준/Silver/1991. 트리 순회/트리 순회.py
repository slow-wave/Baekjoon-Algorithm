import sys

def preorderTraversal(root):
    if root != '.':
        sys.stdout.write(str(root))
        preorderTraversal(tree[root][0])
        preorderTraversal(tree[root][1])

def inorderTraversal(root):
    if root != '.':
        inorderTraversal(tree[root][0])
        sys.stdout.write(str(root))
        inorderTraversal(tree[root][1])

def postorderTraversal(root):
    if root != '.':
        postorderTraversal(tree[root][0])
        postorderTraversal(tree[root][1])
        sys.stdout.write(str(root))

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    tree = {}

    for n in range(N):
        root, left, right = sys.stdin.readline().strip().split()
        tree[root] = [left, right]

    preorderTraversal('A')
    sys.stdout.write("\n")
    inorderTraversal('A')
    sys.stdout.write("\n")
    postorderTraversal('A')