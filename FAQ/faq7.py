x=[1,5,3,7,4,5]
import random
def quicksort(x):
   if len(x) <= 1:
       return x
   else:
       q = random.choice(x)
   l_x = [n for n in x if n < q]
 
   e_x = [q] * x.count(q)
   b_x = [n for n in x if n > q]
   return quicksort(l_x) + e_nums + quicksort(b_x)
print(quicksort(x))
