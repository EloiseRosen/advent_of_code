import math
import json
lst = [json.loads(row) for row in open('input.txt').read().split('\n')]


# Represent snailfish number as a binary tree. (Only the leaf nodes will hold numbers).
class Node:
    def __init__(self, val=None, left_child=None, right_child=None, parent=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent


def create_binary_tree(el):
    if isinstance(el, int): 
        return Node(val=el)
    else:
        node = Node(val=None)
        node.left_child = create_binary_tree(el[0])
        node.right_child = create_binary_tree(el[1])
        node.left_child.parent = node
        node.right_child.parent = node
        return node


def snailfish_add(num1, num2):
    new_root = Node(val=None)
    new_root.left_child = num1
    new_root.right_child = num2
    num1.parent = new_root
    num2.parent = new_root
    return new_root


def split(node):
    stack = [node]
    while len(stack):
        node = stack.pop()
        if node.val is not None and  node.val > 9:
                node.left_child = Node(val=node.val//2)
                node.right_child = Node(val=math.ceil(node.val/2))
                node.val = None
                node.left_child.parent = node
                node.right_child.parent = node
                return True

        if node.right_child is not None:
            stack.append(node.right_child)
        if node.left_child is not None:
            stack.append(node.left_child)

    return False


# got stuck here and got help from William Feng
# an important part: must append right child first!
def explode(node):
    # Do a DFS looking for first case from left that is nested 4 deep
    stack = [(node, 0)]  # node, depth
    while stack:
        node, depth = stack.pop()

        if (depth >= 4 and node.val == None and 
        ((node.right_child is None and node.left_child is None) 
        or 
        (node.right_child.val is not None and node.left_child.val is not None))
        ):
            # Go up the stack to find right node
            prev_node = node.right_child
            curr_node = node
            node.val = 0
            while (curr_node is not None and 
            (curr_node.right_child == prev_node or curr_node.right_child is None)):
                prev_node = curr_node
                curr_node = curr_node.parent

            # Right node must exist
            if curr_node is not None:
                curr_node = curr_node.right_child
                while curr_node.val is None:
                    if curr_node.left_child is not None:
                        curr_node = curr_node.left_child
                    else:
                        curr_node = curr_node.right_child
                curr_node.val = curr_node.val + node.right_child.val
            node.right_child = None

            # repeat for left
            prev_node = node.left_child
            curr_node = node
            node.val = 0
            while (curr_node is not None and 
            (curr_node.left_child == prev_node or curr_node.left_child is None)):
                prev_node = curr_node
                curr_node = curr_node.parent
            if curr_node is not None:
                curr_node = curr_node.left_child
                while curr_node.val is None:
                    if curr_node.right_child is not None:
                        curr_node = curr_node.right_child
                    else:
                        curr_node = curr_node.left_child
                curr_node.val = curr_node.val + node.left_child.val
            node.left_child = None
            
            return True

        # must append right child first!!
        if node.right_child:
            stack.append((node.right_child, depth+1))
        if node.left_child:
            stack.append((node.left_child, depth+1))
    return False


def get_magnitude(node):
    if node.left_child is None and node.right_child is None:  # leaf
        return node.val
    else:
        return 3*get_magnitude(node.left_child) + 2*get_magnitude(node.right_child)


max_magnitude = 0
for idx1 in range(0, len(lst)):
    for idx2 in range(0, len(lst)):
        if idx1 != idx2:
            root_of_num_1 = create_binary_tree(lst[idx1])
            root_of_num_2 = create_binary_tree(lst[idx2])
            root_of_new_num = snailfish_add(root_of_num_1, root_of_num_2)

            while True:
                # If any pair is nested inside four pairs, the leftmost such pair explodes.
                changed = explode(root_of_new_num)
                if changed:
                    continue

                # If any regular number is 10 or greater, the leftmost such regular number splits.
                changed = split(root_of_new_num)
                if changed:
                    continue

                break

            max_magnitude = max(max_magnitude, get_magnitude(root_of_new_num))
print(max_magnitude)
