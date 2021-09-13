import os
import distutils.dir_util

src = r"C:\path\to\source"
dest = r"C:\path\to\destination"

# Built in python library that will copy an entire directory recursivly 
distutils.dir_util.copy_tree(src,dest)