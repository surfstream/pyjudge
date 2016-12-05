"""
This module calculate the edit treee distance of two python codes
and returns the distance of two python codes.

It will first convert a file into a ast tree.
Then it will save all the ast nodes in a list.
From the list, it will convert the nodes into a edit distance tree
and finally calculate the distance of two files
"""

import ast
import node_visit
from zss import simple_distance, Node

def ast_list(file_input):
    """This finction accepts a file and convert it to a list from ast tree"""
    f_open = open(file_input)
    ast_tree = ast.parse(f_open.read())
    nodes_list = []
    node = node_visit.PyNode(nodes_list)
    node.visit(ast_tree)
    return nodes_list

def edit_tree(nodes_list):
    """This function create a edit distance tree from a list of nodes"""
    e_tree = Node(nodes_list[0])
    for node in nodes_list[1:]:
        temp = Node(node[0])
        for child in node[1:]:
            temp.addkid(Node(child))
        e_tree.addkid(temp)
    return e_tree

def edit_tree_distance(file1, file2):
    """This function accepts two python codes and return the distance"""
    list1 = ast_list(file1)
    list2 = ast_list(file2)
    e_tree1 = edit_tree(list1)
    e_tree2 = edit_tree(list2)
    return simple_distance(e_tree1, e_tree2)
