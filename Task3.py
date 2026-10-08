import numpy as np

def task1():
    arr = np.array([3, 6, 9, 12, 15])
    print("Shape:", arr.shape)
    print("Number of dimensions (ndim):", arr.ndim)
    print("Size:", arr.size)
    print("Data type (dtype):", arr.dtype)

def task2():
    zeros_arr = np.zeros((3, 2))
    ones_arr = np.ones((2, 4), dtype=int)
    full_arr = np.full((2, 3), 7)
    print("Zero array:\n", zeros_arr)
    print("Ones array:\n", ones_arr)
    print("Full array:\n", full_arr)

def task3(): 
   #could not solve showing error 
   import numpy as np
rng = np.random.default_rng()
randf = rng.random((3, 3))
print("Random floats (3x3):\n", randf)
randint= rng.integers(0, 10, size=(2, 5))
print("for (2x5):\n", randint)
rand100 = np.random.randint(1, 101, size=(4, 4))
print("for (4x4):\n", rand100)


def task4():
     import numpy as np 
arr_int8 = np.arange(10, dtype=np.int8)
arr_int64 = np.arange(10, dtype=np.int64)
print("nbytes of int8 :", arr_int8.nbytes)
print("nbytes of int64:", arr_int64.nbytes)

def task5():
     import numpy as np
a = np.arange(1, 36).reshape(5, 7)
print("3rd row:", a[2])
print("4th column:", a[:, 3])
print("Last row:", a[-1])
print("Last column:", a[:, -1])

def task6():
     import numpy as np
a = np.arange(1, 36).reshape(5, 7)
print("Every 2nd element of 1st row:", a[0, ::2])
print("2x3 form:\n", a[1:3, 2:5])

def task7():
     import numpy as np
arr = np.arange(1, 13).reshape(2, 2, 3)
print("6:", arr[0, 1, 2])
print("1row of 2block:", arr[1, 0])
print("Last ele:", arr[-1, -1, -1])

def task8() :
     import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print("Val> 10:", arr[arr > 10])
print("Even values:", arr[arr % 2 == 0])
print("Values from 10 to 30:", arr[(arr >= 10) & (arr <= 30)])

def task9() :
     import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
nonzero = np.nonzero(arr > 15)
print("using np.nonzero:",nonzero)
where = np.where(arr > 15)
print("using np.where:",where)


def task10() :
     import numpy as np
marks = np.array([[45, 80, 67], [90, 55, 72], [38, 60, 85]])
print("Marks >= 60:", marks[marks >= 60])
print("Count >= 40:", np.sum(marks >= 40, axis=0))

def task11():
     import numpy as np
s = np.array([2, 5, 8, 11, 14])
pos9 = np.searchsorted(s, 9)
print("Insert at  9:", pos9)
multiple = np.searchsorted(s, [1, 12, 5])
print("Insert for [1, 12, 5]:",multiple)

def task12():
     import numpy as np
a = np.arange(1, 9)
b = a[2:6]
b[0] = 99
print("a after modifying view b:", a)
a = np.arange(1, 9)
b = a[2:6].copy()
b[0] = 99
print("a after modifying copy b:", a)

def task13():
     import numpy as np
x = np.array([[1, 2, 3],[4, 5, 6]])
f = x.flatten()
r = x.ravel()
f[0] = 100
r[1] = 200
print("x:\n", x)
print("f:", f)
print("r:", r)

def task14():
     import numpy as np
arr = np.arange(1, 13)
print(arr.reshape(3, 4).shape)
print(arr.reshape(2, 6).shape)
print(arr.reshape(2, 3, 2).shape)
print(arr.reshape(4, -1).shape) 

def task15():
     import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
row_na = a[np.newaxis, :]     
column_na = a[:, np.newaxis]   
row_ed = np.expand_dims(a, axis=0)  
column_ed = np.expand_dims(a, axis=1)   
print("Row vector :", row_na.shape)
print("Column vector :", column_na.shape)
print("Row vector ed", row_ed.shape)
print("Column vector ed:", column_ed.shape)

def task16():
     import numpy as np
arr = np.arange(1, 13).reshape(3, 4)
print(" no axis:\n", np.flip(arr))
print("axis=0:\n", np.flip(arr, axis=0))
print(" axis=1:\n", np.flip(arr, axis=1))

def task17():
     import numpy as np

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
vstack = np.vstack((a1, a2))
hstack = np.hstack((a1, a2))
concat = np.concatenate((a1, a2), axis=1)
print("vstack result:\n", vstack)
print("hstack result:\n", hstack)
print("concatenate axis=1:\n", concat)

def task18():
     import numpy as np
x = np.arange(1, 25).reshape(2, 12)
equal = np.array_split(x, 3, axis=1)
columns = np.hsplit(x, [3, 4])
arr = np.arange(1, 7)
split_arr6 = np.array_split(arr, 4)
print("3 equal parts:", [s.shape for s in equal])
print(" after 3rd and 4th columns:", [s.shape for s in columns])
print("Split np.arange(1, 7) into 4 parts:", split_arr6)

def task19():
     #could not solve 
     import numpy as np
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_vals, counts, first_indices = np.unique(a, return_counts=True, return_index=True)
print("Unique values:", unique_vals)
print("Counts:", counts)        
print("First indices:", first_indices)

def task20():
     import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])
union = np.union1d(a, b)             
intersection = np.intersect1d(a, b)  
diff_res = np.setdiff1d(a, b)            
sym_diff = np.setxor1d(a, b)         
print("Union:", union)
print("Intersection:", intersection)
print("Difference (a - b):", diff_res)
print("Symmetric Difference:", sym_diff)


def task21():
     import numpy as np
m = np.arange(1, 10).reshape(3, 3)
row = m + np.array([10, 20, 30])
col = m + np.array([[100], [200], [300]])
print("Row added:\n",row)
print("Column added:\n",col)

def task22():
     #could not solve 
     import numpy as np
shapes = [((4, 3), (3,)), ((4, 3), (4,)), ((4, 3), (4, 1)), ((2, 3, 4), (3, 1))]
for s1, s2 in shapes:
    try:
        res = np.ones(s1) + np.ones(s2)
        print(f"Shapes {s1} + {s2} -> Success, result shape: {res.shape}")
    except Exception as e:
        print(f"Shapes {s1} + {s2} -> Error: {e}")


def task23():
     import numpy as np
rng = np.random.default_rng(42)
arr = rng.random((3, 4))
print("Overall sum:", np.sum(arr))
print("Overall mean:", np.mean(arr))
print("Overall min:", np.min(arr))
print("Overall max:", np.max(arr))
print("Overall std:", np.std(arr))
print("Overall prod:", np.prod(arr))
print("Column sums (axis=0):", np.sum(arr, axis=0))
print("Row maxima (axis=1):", np.max(arr, axis=1))
print("Index of overall maximum:", np.argmax(arr))

def task24():
     #could not solve 
     import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
element_wise = A * B
matrix_prod = np.matmul(A, B)
det_a = np.linalg.det(A)
print("Element-wise product:\n", element_wise)
print("Matrix product:\n", matrix_prod)
print("Determinant of A:", det_a)

def task25():
     import numpy as np
predictions = np.array([2.5, 0.0, 2.1, 7.8])
labels = np.array([3.0, -0.5, 2.0, 8.0])
mse = np.mean((predictions - labels) ** 2)
print("Mean Squared Error:", mse)  


if __name__ == "__main__":
      task1()
      task2()
      task3()
      task4()
      task5()
      task6()
      task7()
      task8()
      task9()
      task10()
      task11()
      task12()
      task13()
      task14()
      task15()
      task16()
      task17()
      task18()
      task19()
      task20()
      task21()
      task22()
      task23()
      task24()
      task25()


