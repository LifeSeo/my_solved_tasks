from heapq import heappop, heappush  
   
def heapsort(list1):  
     heap = []  
     for ele in list1:  
         heappush(heap, ele)  
   
     sort = []  
<<<<<<< HEAD
     
=======
   
>>>>>>> e585649c1de5f07e615b5b9c092809861e53df01
     while heap:  
         sort.append(heappop(heap))  
   
     return sort  
   
list1 = [14335, 7608, -7599, 34, 95, 111, 56, 0, 99, 67, 53, 11]  
print(heapsort(list1))
