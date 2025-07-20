"""
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. 
If two or more folders are identical, then mark the folders as well as all their subfolders.

For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z
However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.signature = ""  

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node("")
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Node(folder)
                node = node.children[folder]
        
        signature_count = defaultdict(int)

        def dfs(node):
            if not node.children:
                node.signature = ""
                return ""
            child_signatures = []
            for name, child in sorted(node.children.items()):
                child_signature = dfs(child)
                child_signatures.append(f"{name}({child_signature})")
            node.signature = "".join(child_signatures)
            signature_count[node.signature] += 1
            return node.signature
        
        dfs(root)

        result = []
        current_path = []
        
        def dfs2(node):
            if node.children and signature_count[node.signature] >= 2:
                return
            current_path.append(node.name)
            result.append(current_path.copy())
            for name, child in sorted(node.children.items()):
                dfs2(child)
            current_path.pop()
        
        for name, child in sorted(root.children.items()):
            dfs2(child)
        
        return result

"""

"""