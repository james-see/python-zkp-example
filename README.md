## snarf snarf merkle trees snarf

### HOW

1. Do `pipenv shell`
2. Do `python3 src/merk.py "ablacklistedimsi"` to validate that that number or string is not in the tree
   1. Note that the double quotes are important, no funny business
   2. ablacklistedimsi string data will validate True as a member, change to something else to get False
3. Do `python3 src/treegen.py to show the example tree as a tree diagram using tkinter and matplotlib`

### THE REST

Who knows. The dude abides.

### Warning

This is an example repo. It uses the merkle-tools library in python that is a port from [this](https://github.com/tierion/merkle-tools) repo for python

This is not meant to be production code, but is an easy way to prove the concept and could turn into production code with some time and effort.