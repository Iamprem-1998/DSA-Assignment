# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse(alist):

   left = 0
   right = len(alist)-1

   while left<right:

       temp = alist[left]
       alist[left] = alist[right]
       alist[right] = temp

       left += 1
       right -= 1

   return alist

print(reverse(list(map(int, input("Type number with space: ").split()))))