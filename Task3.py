import numpy as np

def task1():
    arr = np.array([3, 6, 9, 12, 15])
    print("--- Task 1 Output ---")
    print("Shape:", arr.shape)
    print("Number of dimensions (ndim):", arr.ndim)
    print("Size:", arr.size)
    print("Data type (dtype):", arr.dtype)

def task2():
    zeros_arr = np.zeros((3, 2))
    ones_arr = np.ones((2, 4), dtype=int)
    full_arr = np.full((2, 3), 7)
    
    print("\n--- Task 2 Output ---")
    print("Zero array:\n", zeros_arr)
    print("Ones array:\n", ones_arr)
    print("Full array:\n", full_arr)

def task3(): 
    import numpy as np 
rng = np.random.default_rng()
random_float = rng.random((3, 3))
print("\n--- Task 3 Output ---")
print("3x3 array of float:\n", random_float)
random_int = rng.int(0, 10, size=(2, 5))
print("\n2x5 array of int 0 to 9:\n", random_int)
randint_arr = np.random.randint(1, 101, size=(4, 4))
print("\n4x4 array of int from 1 to 100:\n", randint_arr)

def task4():
     import numpy as np 
arr_int8 = np.arange(10, dtype=np.int8)
arr_int64 = np.arange(10, dtype=np.int64)
print("\n--- Task 4 Output ---")
print("nbytes of int8 :", arr_int8.nbytes)
print("nbytes of int64:", arr_int64.nbytes)



if __name__ == "__main__":
      task1()
      task2()
      task3()
      task4()

