"""
Test code for the pyjudge featrues
The codd accepts a target file name and a list of file names 
"""


import find_similar

L = ["example/test2.py", "example/test3.py"]

target = "example/test1.py"

res = find_similar.find_similar(target, L)
print()
print(res)
