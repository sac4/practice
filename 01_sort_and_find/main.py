import sort_and_find as sf

"""
   Try bubble_sort(List) and find_key(key,List).
"""
List=[3,4,5,6,-1,-3,-5,2,9]
key=10

print "Original list:\n",List,"\n"

List=sf.bubble_sort(List)
print "Sorted list:\n",List,"\n"

print "Key value ",key," is found at ",sf.find_key(key,List),".\n"

