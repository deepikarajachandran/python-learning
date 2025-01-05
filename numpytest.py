import numpy as np
print(np.__version__)

#create 1D
n1 = np.array([[1,2,5],[3,4,8]])
print(n1)

#create 2D
n2 = np.zeros([4,4],dtype=float)
# print(n2)

#create 3D
n3 = np.ones([8,2,3], dtype=int) #print 8 times 2*3 arrays
# print(n3)

#create empty array
n4 = np.empty([1,2])
# print(n4)

#create array with range of values
n5 = np.arange(1,8,2) #start value, stop value, step up value
print(n5)

#linearly spaced entries
n6 = np.linspace(2, 30, num=15, dtype=int) #print values bw 2 and 30 with total of 15
# print(n6)

#full and fill
n7 = np.full((3,4), 23) #full of 3*4 array with 23
# print(n7)

n2.fill(3) # with existing zeros array, it doesn't store on new array
# print(n2)

#access the elements
# print(n5[2])
# print(n1[1][2])
# print(n1[1,:])

#sort
ntest = np.array([3,2,3,75,56,32,324,8])
print(np.sort(ntest))
# descend sort
print(np.sort(ntest)[::-1])

