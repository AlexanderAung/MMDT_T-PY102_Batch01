from pathlib import Path


# -------------------------
# Do not change the below Code
# -------------------------
class TreeNode:
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root):
    if not root:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


# -------------------------


# -------------------------
# Q1 — Build Submission Tree for submissions folder
# Visit our class homework submission repo.
# Look inside the "submissions" folder.
# Pick TWO folders: your folder and your friend's folder (choose with files).
#
# Notes:
# - Ignore any subfolders inside the chosen folders.
# - Only consider FILES inside each chosen folder (each filename becomes a node).
# - Tree structure should be:
#     submissions
#     ├── folder1
#     │   ├── fileA
#     │   └── fileB
#     └── folder2
#         ├── fileC
#         └── fileD
# -------------------------

"""
class NormalTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

"""


def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions
    folder2: name of your friend's folder inside submissions
    returns: root TreeNode
    """
    """
    base = Path(base_path)
    root = NormalTreeNode(base_path.name)

    for folder in [folder1, folder2]:
        f_node = NormalTreeNode(folder.name)
        f_path = base / folder

        files = [f for f in f_path.iterdir() if f.is_file()]

        for file in files:
            f_node.children.append(NormalTreeNode(file.name))

        root.children.append(f_node)

    def encode_to_binary(node: NormalTreeNode) -> TreeNode:
        if not node:
            return None

        b_node = TreeNode(node.value)

        if node.children:
            # first child to left

            b_node.left = encode_to_binary(node.children[0])

            # remaining children → right sibling chain
            current = b_node.left
            for child in node.children[1:]:
                current.right = encode_to_binary(child)
                current = current.right

        return b_node

    # print(encode_to_binary(root))

    r = encode_to_binary(root)
    print(f"Value   : {r.value}")
    print(f"Left    : {r.left}")
    print(f"Right   : {r.right}")

    return encode_to_binary(root)



    def to_BTree(normal_node: NormalTreeNode) -> TreeNode:
        if not normal_node:
            return None

        b_tree = TreeNode(normal_node.value)
        if normal_node.children:
            b_tree.left = normal_node.children[0]
            b_tree.right = normal_node.children[1:]
   
    # -------- folder1 chain --------

    # l1 = TreeNode("lab01.py")
    # l2 = TreeNode("lab02.py")
    # l3 = TreeNode("lab03.py")
    # l0 = TreeNode("lab00.py")
    # ag = TreeNode("autograder_results.json")

    # l0.r = l1
    # l1.r = l2
    # l2.r = l3
    # l3.r = ag

    l0 = TreeNode(".gitkeep")
    f1 = TreeNode(folder1)
    f1.l = l0

    # -------- folder2 chain --------
    x0 = TreeNode("lab00.py")
    x1 = TreeNode("lab01.py")
    x2 = TreeNode("lab02.py")
    x3 = TreeNode("lab03.py")
    xg = TreeNode("autograder_results.json")

    x0.r = x1
    x1.r = x2
    x2.r = x3
    x3.r = xg

    f2 = TreeNode(folder2)
    f2.l = x0

    # -------- root --------
    rt = TreeNode(base_path)
    rt.l = f1
    rt.r = f2

    return rt 
    """
    # folder1 — only .gitkeep

    base = Path("submissions")
    root = TreeNode(base.name)

    f1_name = "PY1020010013"
    f2_name = "PY1020010014"

    left_folder = TreeNode(f1_name)
    right_folder = TreeNode(f2_name)

    root.left = left_folder
    root.right = right_folder

    def chain_files(folder_node: TreeNode, folder_path: Path):
        prev = None
        for file_path in sorted(folder_path.iterdir(), key=lambda f: f.name):
            if file_path.is_file():
                new_node = TreeNode(file_path.name)
                if folder_node.left is None:
                    folder_node.left = new_node
                else:
                    prev.right = new_node
                prev = new_node

    # Build chains
    chain_files(left_folder, base / f1_name)
    chain_files(right_folder, base / f2_name)

    return root


# -------------------------
# Q2 — Visit All Nodes Using Tree Traversal (Print Everything)
#
# Use the provided traversal function to visit ALL nodes in the tree,
# including:
#   1) the root node: "submissions"
#   2) the two folder nodes
#   3) all file nodes under each folder
#
# Notes:
# - The printing order depends on the traversal you use (preorder, BFS, etc.).
# - You must use the provided traversal function (do not manually recurse).
# - Print exactly the node.value for each visited node.
# -------------------------


def print_all_nodes(root: TreeNode) -> None:
    """
    Traverse the tree and print the value stored in EVERY node.
    root: the TreeNode returned from build_submission_tree
    """
    # return [root.value] + preorder(root.left) + preorder(root.right)

    for f_name in preorder(root):
        print(f_name)


# -------------------------
# Q3 — Find All Python Files (.py)
#
# Write a function that traverses the tree and returns
# a list of all files ending with ".py".
#
# Notes:
# - Use traversal (do not manually access children).
# - Return a list of strings.
# - The function should NOT print — it should return the list.
# - Example return:
#     ["folderA/file1.py", "folderB/main.py"]
# -------------------------


def find_py_files(root: TreeNode) -> list[str]:
    """
    Traverse the tree and return a list of all '.py' files.
    root: the TreeNode returned from build_submission_tree
    """
    py_files = []
    for f_name in preorder(root):
        print(f_name[-3:])
        if f_name[-3:] == ".py":
            py_files.append(f_name)

    # print(py_files)
    return py_files


"""

SUBMISSION_PATH = Path(__file__).resolve().parent.parent

F1 = SUBMISSION_PATH / "PY102001013"
F2 = SUBMISSION_PATH / "PY102001014"
root = build_submission_tree(SUBMISSION_PATH, F1, F2)
# print(inorder(root))
# print(preorder(root))
# print_all_nodes(root)
find_py_files(root)



SUBMISSION_PATH = Path(__file__).resolve().parent.parent

F1 = SUBMISSION_PATH / "PY102001013"
F2 = SUBMISSION_PATH / "PY102001014"
build_submission_tree(SUBMISSION_PATH, F1, F2)
"""
