"""
This module calculate the edit treee distance of two python codes
and returns the distance of two python codes
"""

import ast
import nodeVisit
from zss import simple_distance, Node

# astList function accepts a python code and returns a list parsing from
# ast tree


def astList(file_input):
    f = open(file_input)
    astTree = ast.parse(f.read())     # parse the code to an ast tree
    # print()
    # print('astTree: ', astTree)
    L = []
    v = nodeVisit.PyNode(L)           # use nodeVisit module
    # print()
    # walk through ast tree and store all nodes in list
    v.visit(astTree)
    return L

# editTree function accepts a list of nodes and returns a edit distance tree


def editTree(L):
    eTree = Node(L[0])                   # create the root from first node
    for x in L[1:]:                      # loop create the edti distance tree
        temp = Node(x[0])
        for xx in x[1:]:
            temp.addkid(Node(xx))
        eTree.addkid(temp)
    return eTree

# editTreeDistance function accepts two python codes and return the
# distance of two codes


def editTreeDistance(file1, file2):
    L1 = astList(file1)
    L2 = astList(file2)
    eTree1 = editTree(L1)
    eTree2 = editTree(L2)
    # print(eTree1)
    # print(eTree2)
    # print(simple_distance(eTree1, eTree2))
    return simple_distance(eTree1, eTree2)

"""
if __name__=='__main__':
    editTreeDistance('test1.py', 'test2.py')
"""

