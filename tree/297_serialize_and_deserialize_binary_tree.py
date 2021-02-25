"""
297. Serialize and Deserialize Binary Tree
Hard
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        
        if root is not None:
            queue = deque()
            queue.append((root, 1))
            index_to_el_dict = {}
            while queue:
                node, index = queue.popleft()
                if node:
                    index_to_el_dict[index] = node.val
                    queue.append((node.left, 2*index))
                    queue.append((node.right, 2*index + 1))
            res = "|".join([f"{key} {value}" for key, value in index_to_el_dict.items()])
            # res = json.dumps(index_to_el_dict)
            
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data:
            # index_to_el_dict = {int(key):int(value) for key, value in json.loads(data).items()}
            
            index_to_el_pairs = data.split("|")
            index_to_el_dict = {}
            for pair in index_to_el_pairs:
                key, value = pair.split()
                index_to_el_dict[int(key)] = int(value)
            
            cur_index = 1
            root = TreeNode(index_to_el_dict[str(cur_index)])
            queue = deque()
            queue.append((root, cur_index))
            
            while index_to_el_dict:
                parent_node, node_index = queue.popleft()
                del index_to_el_dict[str(node_index)]
                
                for index, child in [(2*node_index, 'left'), (2*node_index + 1, 'right')]:
                    value = index_to_el_dict.get(str(index), None)
                    if value is not None:
                        child_node = TreeNode(value)
                        setattr(parent_node, child, child_node)
                        queue.append((child_node, index))
            return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))