# Example1: Various assignment and Print 
list1 = [0.5 * x for x in range(0, 4)]
print(list1)
list1.insert(3,5)
print(list1)

PyList=["Big Data", "Hadoop", "Spark", "IoT"]
print(PyList)
PyList.reverse()
print(PyList)
"Welcome to Python".split()

def f(values):
 values[0] = 44
v = [1, 2, 3]
f(v)
print(v)


names1 = ['Amir', 'Bala', 'Chales']
if 'amir' in names1:
    print(1)
else:
   print(2)

####
m = [[x, x + 1, x + 2] for x in range(0, 3)]
print(m)
#####
m1 = [[x, y] for x in range(0, 4) for y in range(0, 4)]
print(m1)

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(data[1][0][0])


###Example: Nested List:Sorting on First Value default
PyList=[[1,2],[2,4],[4,5],[3,1]]
print(PyList)
PyList.sort()
print(PyList)

##########
points = [[1, 2], [3, 1.5], [0.5, 0.5]]
print(points)
points.sort()
print(points)

####### question number 14-Doubt
a=[10,23,56,[78]]
b=list(a)
print(b)

a[3][0]=95
a[1]=34
print(b)

lst=[3,4,6,1,2]
lst[1:2]=[7,8]
print(lst)
######
a=["Apple","Ball","Cobra"]
a.sort(key=len)
print(a)
######## Question no 17 -Doubt
print(list(map(lambda x: x**-1, [1, 2, 3])))

###### Tuple
t = (1, 2, 4, 3)
print(t[3])
#t[3] = 45
print(max(t))
print(len(t))


a=(1,2)
b=(3,4)
c=a+b
print(c)
#######
a=[(2,4),(1,2),(3,9)]
a.sort()
print(a)
#####

a={4,5,6}
b={2,8,6}
#print(a+b)

#######
a={5,6,7,8}
b={7,8,10,11}
print(a^b)

a={5,6,7,8}
b={7,5,6,8}
print(a==b)
#######
#a={3,4,{7,5}}
#print(a[2][0])

a={1,2,3}
b=a.copy()
print(b)
b.add(4)
print(a)

###########
a={1,2,3}
b={1,2,3}
c=a.issubset(b)
print(c)
######

#for x in set('pqr'):
 #     print(x*2,end=””)
#####
s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}
print(s1.difference(s2))
print(s2.difference(s1))


x=1
y=x<<2
print(y)
print(bin(29))
print(int('1111',2))
print(bin(0x8))

#Output
"C:\Users\sivakumar Panda\PycharmProjects\pythonProject\venv\Scripts\python.exe" "C:\Users\sivakumar Panda\PycharmProjects\pythonProject\1_assignment.py" 
[0.0, 0.5, 1.0, 1.5]
[0.0, 0.5, 1.0, 5, 1.5]
['Big Data', 'Hadoop', 'Spark', 'IoT']
['IoT', 'Spark', 'Hadoop', 'Big Data']
[44, 2, 3]
2
[[0, 1, 2], [1, 2, 3], [2, 3, 4]]
[[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
5
[[1, 2], [2, 4], [4, 5], [3, 1]]
[[1, 2], [2, 4], [3, 1], [4, 5]]
[[1, 2], [3, 1.5], [0.5, 0.5]]
[[0.5, 0.5], [1, 2], [3, 1.5]]
[10, 23, 56, [78]]
[10, 23, 56, [95]]
[3, 7, 8, 6, 1, 2]
['Ball', 'Apple', 'Cobra']
[1.0, 0.5, 0.3333333333333333]
3
4
4
(1, 2, 3, 4)
[(1, 2), (2, 4), (3, 9)]
{5, 6, 10, 11}
True
{1, 2, 3}
{1, 2, 3}
True
{1, 2}
{4, 5, 6}
4
0b11101
15
0b1000
Process finished with exit code 0
