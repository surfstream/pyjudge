"""
Test code for the pyjudge featrues
The codd accepts a target file name and a list of file names
"""

import find_similar

def closest():
    """this function tests the find_similar module"""
    list_file = ["example/test2.py", "example/test3.py"]
    target = "example/test1.py"
    res = find_similar.find_similar(target, list_file)
    print(res)

if __name__ == "__main__":
    closest()
