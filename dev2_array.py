import numpy as np 
a = 45.7
##
## Membuat array
print("===Array 1D===")
# 1. Membuat array array
arr_1 = np.array([1,5,10,15,20,25,30])
print("Fungsi Array")
print(arr_1)


# 2. Membuat array dari  numpy - arange
arr_2 = np.arange(float(1),float(11))
arr_2b = np.arange(2, 10, dtype=float)
arr_2rev = arr_2*a
print("Fungsi Arange")
print(arr_2b)
print(arr_2rev)

# 3. Membuat array dari linspace
arr_3 = np.linspace(0,10,10)
print("Fungsi linspace")
print(arr_3)

# 4. Menggunakan template zeros dan ones
arr_4 = np.zeros(5)
print(arr_4)

arr_4a = np.ones(5)
print(arr_4a)


print("===Array 2D etc===")
# menggunakan seluruh metode diatas
#---f array
arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)
#---f template
arr_2e = np.indices((3,3))
print(arr_2e)



## Akses array
print(arr_1[2])

## Operasi aritmatika array