from __future__ import annotations
from typing import TypeVar, Callable, TypeAlias, Type

A = TypeVar("A")
B = TypeVar("B")

# 二叉树的节点

LeafType:TypeAlias = None # for python 3.12 we can use `type Leaf=None`
Leaf = None # Leaf object
class btn():
    """
    Binary tree node

    Attributes:
    -----------
    content: content of the node, can be any object
    left: left child node, btn object
    right: right child node, btn object
    tag: tag of current node, Any
    """
    def __init__(self, content:A,left:btn|LeafType,right:btn|LeafType,tag:B=None):
        self.content:A|None = content
        self.left:btn|LeafType = left
        self.right:btn|LeafType = right
        self.tag:B|None = tag

Node:TypeAlias = btn|LeafType

# 产生`level`层的二叉树
def makebtnt(level:int,content:A,lp:Callable[[A],A],rp:Callable[[A],A]) -> Node:
    """
    Generate btn tree

    Inputs:
    -------
    level: number of level in the tree
    content: content for root
    lp: operator takes the current content and generating the left child content, content=>content
    rp: operator takes the current content and generating the right child content, content=>content

    Output:
    -------
    root: the root of btnt, a btn object
    """
    if not isinstance(level, int) or level < 0:
        raise ValueError('invalid input in makebtnt')
    root = btn(content, Leaf, Leaf, None) 
    if level > 0:
        if lp != None:
            root.left = makebtnt(level-1, lp(content), lp, rp)
        else:
            root.left = makebtnt(level-1, None, lp, rp)
        if rp != None:
            root.right = makebtnt(level-1, rp(content), lp, rp)
        else:
            root.right = makebtnt(level-1, None, lp, rp)
    return root

# 提取`(level,block)`节点
def btnt2btn(root, level, block):
    if level == 0 or root == Leaf:
        node = root
    else:
        if (block % 2) == 0:
            node = btnt2btn(root.left, level-1, block>>1)
        else:
            node = btnt2btn(root.right, level-1, (block-1)>>1)
    return node

# 提取以节点`(level,block)`为根的子树
def btn2branch(self, level:int, block:int)->Node:
    if level > 0:
        if (block % 2) == 0:
            if self.left == Leaf:
                self.left = btn(None, Leaf, Leaf, None)
            self = btn2branch(self.left, level-1, block>>1)
        else:
            if self.right == Leaf:
                self.right = btn(None, Leaf, Leaf, None)
            self = btn2branch(self.right, level-1, (block-1)>>1)
    return self


def height(node: Node)->int:
    if (node == Leaf):
        return 0
    elif (node!=None):
        # compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # use the larger one
        if (lheight > rheight):
            return (lheight + 1)
        else:
            return (rheight + 1)
    else: return 0

# Function to  print level order traversal of tree
def print_level_order(root: Node):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)
        print("\n")


# Print nodes at a current level
def print_current_level(root: Node, level: int):
    if root is None:
        return
    if level == 1:
        print(root.content, end=" ")
    elif level > 1:
        print_current_level(root.left, level-1)
        print_current_level(root.right, level-1)
