"""
This module finds the most similar code from a list to the target code
by using the compareFile module
"""

import compare_file

def find_similar(target, all_file):
    """return a file from all_file list which is closest to target"""
    i = all_file[0]
    diff = 10000000
    for every_file in all_file:
        if compare_file.edit_tree_distance(target, every_file) < diff:
            diff = compare_file.edit_tree_distance(target, every_file)
            i = every_file
    return i
