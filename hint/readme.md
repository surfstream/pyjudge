The following paragraphs explain how to use the code.

In module find_similar.py, you can call a function find_similar(target, all_file). target is the target python code from the user input and all_file is list of files in the backend server. This function will return a file from the list which is the closest to the target file.

```python
find_similar(<target_file>, <file_list>)
```
During the execution, it will call functions from several other modules, including compare_file.py and node_visit.py. This has already been implemented. The only thing that you need to do is to call the find_similar(target, all_file) function in the find_similar.py module.

Some other functions can also be called if you need some specific feature.

The following usage in compare_file.py module returns a distance of two files.

```python
edit_tree_distance(<target_file1>, <target_file2>)
```