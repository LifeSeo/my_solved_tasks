from heapq import heappop, heappush  
   
def heapsort(list1):  
     heap = []  
     for ele in list1:  
         heappush(heap, ele)  
   
     sort = []  
   
     while heap:  
         sort.append(heappop(heap))  
   
     return sort  
   
list1 = [14335, 7608, -7599, 34, 95, 111, 56, 0, 99, 67, 53, 11]  
print(heapsort(list1))
