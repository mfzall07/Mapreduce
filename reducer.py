import sys
k = 2
# def knn_reducer(k):
num_neighbours = {}
counter = 0
for line in sys.stdin:
 if counter < k:
 #         print(num_neighbours)
     # remove leading and trailing whitespace
     line = line.strip()
     
     # parse the input we got from mapper.py
     class_, count = line.split('\t', 1)
     if class_ in num_neighbours:
         num_neighbours[class_]+=1
     else:
         num_neighbours[class_]=1
 else:
   break
 counter+=1
         
print(num_neighbours)