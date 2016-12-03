"""
This module provide a class that can walk through the ast tree and returns the 
nodes from ast tree as a list
"""

import ast

class PyNode(ast.NodeVisitor):

    # initialize a list that can store all the nodes from ast tree
    def __init__(self, L):
        self.L = L

    # redefine generic_visit function to walk through all the nodes in ast tree
    # store all the nodes of ast tree in the list initialized above
    def generic_visit(self, node):
        # print(type(node).__name__)
        l = []
        l.append(str(type(node).__name__))
        self.L.append(l)
        ast.NodeVisitor.generic_visit(self, node)  # recursive visit all the child nodes
        return self.L

    # redifine the ast treenode name and store in list
    def visit_Name(self, node):
        # print('Name :', node.id)
        l = []
        l.append(str(type(node).__name__))
        l.append(str(node.id))
        self.L.append(l)

    # redefine number that will be store in list
    def visit_Num(self, node):
        # print('Num :', node.__dict__['n'])
        l = []
        l.append(str(type(node).__name__))
        l.append(str(node.__dict__['n']))
        self.L.append(l)

    # redefine string that will be store in list
    def visit_Str(self, node):
        # print('Str :', node.s)
        l = []
        l.append(str(type(node).__name__))
        l.append(str(node.s))
        self.L.append(l)

    # redefine print function output and store in list
    def visit_Print(self, node):
        # print('Print :')
        l = []
        l.append(str(type(node).__name__))
        self.L.append(l)
        ast.NodeVisitor.generic_visit(self, node)

    # redefine output of assignment operator and store in list
    def visit_Assign(self, node):
        # print('Assign :')
        l = []
        l.append(str(type(node).__name__))
        self.L.append(l)
        ast.NodeVisitor.generic_visit(self, node)
        
    # redefine expression and store in list
    def visit_Expr(self, node):
        # print('Expr :')
        l = []
        l.append(str(type(node).__name__))
        self.L.append(l)
        ast.NodeVisitor.generic_visit(self, node)

if __name__ == '__main__':
    node = ast.parse('a = 1 + 2')
    # print(ast.dump(node))
    v = PyNode()
    v.visit(node)
