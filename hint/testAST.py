import ast
expr = """
def add(arg1,arg2):
    return arg1 + arg2
"""
expr_ast = ast.parse(expr)
expr_ast
print("hello, world")
print(ast.dump(expr_ast))
print("hello, earth")
