# Ternary-Search
This is a tool that can be used to search for strings in csv files of any size using a ternary search tree. This search method is 
faster than a simple loop or binary search tree, but slower than a standard trie search algorithm. The reason you might elect to
use a ternary algorithm over a trie is if memory usage is a concern, because each node in the tree will never have more than 3 
child nodes. Ternary search trees tend to work best when you have a large number of strings to search for in a large file.

This repository also includes a trie search algorithm and a CSV class for taking CSV data and turning it into different types of nested dictionary and list combinations to operate on. 
