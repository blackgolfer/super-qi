from __future__ import annotations
from typing import TypeVar, Callable

C = TypeVar("C")
T = TypeVar("T")

# 二叉树的节点


class btn:
    """
    Binary tree node

    Attributes:
    -----------
    content: content of the node, can be any object
    left: left child node, btn object
    right: right child node, btn object
    tag: tag of current node, Any
    """

    def __init__(self, content:C,left:btn,right:btn,tag:T=None):
        self.content = content
        self.left = left
        self.right = right
        self.tag = tag

# 产生`level`层的二叉树


def makebtnt(level:int,content:C,lp:Callable[[C],C],rp:Callable[[C],C]) -> btn:
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
    root = btn(content, None, None, None)  # type: ignore
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
    if level == 0 or root == None:
        node = root
    else:
        if (block % 2) == 0:
            node = btnt2btn(root.left, level-1, block/2)
        else:
            node = btnt2btn(root.right, level-1, (block-1)/2)
    return node

# 提取以节点`(level,block)`为根的子树


def btn2branch(self, level:int, block:int)->btn:
    if level > 0:
        if (block % 2) == 0:
            if self.left == None:
                self.left = btn(None, None, None, None)  # type: ignore
            self = btn2branch(self.left, level-1, block/2)
        else:
            if self.right == None:
                self.right = btn(None, None, None, None)  # type: ignore
            self = btn2branch(self.right, level-1, int((block-1)/2))
    return self


def height(node: btn):
    if (node == None):
        return 0
    else:
        # compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # use the larger one
        if (lheight > rheight):
            return (lheight + 1)
        else:
            return (rheight + 1)

# Function to  print level order traversal of tree


def print_level_order(root: btn):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)
        print("\n")


# Print nodes at a current level
def print_current_level(root: btn, level: int):
    if root is None:
        return
    if level == 1:
        print(root.content, end=" ")
    elif level > 1:
        print_current_level(root.left, level-1)
        print_current_level(root.right, level-1)
