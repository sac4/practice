"""
   subroutine: bubble_sort(List1)
      Input: List1=[x_1,x_2,...,x_n] where x_i is integral.
      Output: List2 (sorted list from List1)
"""
def bubble_sort(List1=[1,2,3]):
   List2=List1
   size=len(List1)
   
   for i in range(size):
      for j in range(i+1,size):
         if List2[i] > List2[j]:
            work=List2[i]
            List2[i]=List2[j]
            List2[j]=work
   return List2

"""
   subroutine: find_key(key,List)
      Find 'key' out of a sorted list 'List'
"""
def find_key(key=2, List=[1,2,3]):
   
   # initialization
   size=len(List)
   L=0
   U=size-1
   flag=0

   while flag==0:
      if L>U:
         M=-1
         flag=1
      else:
         M=(U+L)/2
         if key==List[M]:
            flag=1
         elif key>List[M]:
            L=M+1
         else:
            U=M-1

   return M


"""
   Try bubble_sort(List) and find_key(key,List).
"""
List=[3,4,5,6,-1,-3,-5,2,9]
key=6

print(List)

List=bubble_sort(List)
print(List)

print "key value ",key," is found at ",find_key(key,List),".\n"




