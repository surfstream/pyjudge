"""
This module provide a class that can walk through the ast tree
and returns the nodes from ast tree as a list
"""

import ast

class PyNode(ast.NodeVisitor):
    """
    This class can walk through the ast tree and store nodes in a list"""
    def __init__(self, nodes_list):
        """initialize a list"""
        self.nodes_list = nodes_list

    def generic_visit(self, node):
        """
        redefine generic_visit function to walk through all nodes
        in ast tree and store all the nodes of ast tree in list
        """
        temp = []
        temp.append(str(type(node).__name__))
        self.nodes_list.append(temp)
        # recursive visit all the child nodes
        ast.NodeVisitor.generic_visit(self, node)
        return self.nodes_list

    def visit_name(self, node):
        """redefine the ast treenode name and store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        temp.append(str(node.id))
        self.nodes_list.append(temp)

    def visit_num(self, node):
        """redefine number that will be store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        temp.append(str(node.__dict__['n']))
        self.nodes_list.append(temp)

    def visit_str(self, node):
        """redefine string that will be store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        temp.append(str(node.s))
        self.nodes_list.append(temp)

    def visit_print(self, node):
        """redefine print function output and store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        self.nodes_list.append(temp)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_assign(self, node):
        """redefine output of assignment operator and store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        self.nodes_list.append(temp)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_expr(self, node):
        """redefine expression and store in list"""
        temp = []
        temp.append(str(type(node).__name__))
        self.nodes_list.append(temp)
        ast.NodeVisitor.generic_visit(self, node)
