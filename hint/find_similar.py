"""
This module finds the most similar code from a list to the target code by using the compareFile module
"""

import compareFile

def find_similar(target, all_file):
    i = all_file[0]
    diff = 10000000
    for every_file in all_file:
        if compareFile.editTreeDistance(target, every_file) < diff:
            diff = compareFile.editTreeDistance(target, every_file)
            i = every_file
    return i

'''
if __name__ == '__main__':
    find_similar(target, all_file)
'''
