# numpy
- array size is fix,changing the size creates new one.
- each element in array has same size in memroy even for strings. 
- the numpy indexing and broadcasting concepts are the defacto standards of array computing today.
- can do fourier tranformations.
- it plays well with GPU and distributed sytems.

- numpy exists because we often deal with matrices and arrays.
- lists are 10x to 100x slower than numpy
- arrays are homogenous.
- hardware level support of numpy
- numpy uses SIMD processor and utilizes cache.
- numpy is written in c
- %% time is a magic command to record execution time.
- one billion squares in 198 seconds.
- inbuilt functions are always fast.
- list comprehention is fast.and map etc are even faster.
- with arrow up you can move cells up in colab
- type of most expessive element is the type of whole array.
- (10,1) is not same as (10,) , shapes can cause error.
- we can have array of booleans,or even strings.
- arr=np.array(string_array,dtype="float")
- 1/0 gives inf
- np.isinf(arr[0,0]) or np.isinf(arr)
- always generalize your code to varialbe no. number of dimetions.
- columns is always last dimesion.
- arrays are mutable,with shallow copying
- matrices are 2 orders faster than loops.



## creating the numpy.ndarray
```python
    import numpy as np
    arr=np.array([
        [1,2,3],
        [4,5,6]
    ])
    arr=np.asarray([
        [1,2,3],
        [4,5,6]
    ])

    "the difference between asarray and array is that array by default will make a copy whereas asarray will not unless necesary. although you can use copy keyword argument and set it to True or False in array and asarray basically returns array with copy=False "
```

## reading from file 
```python
arr=np.genfromtxt(""data.txt",delimiter=",",skip_header=3,usecols=[x for x in range(1,10)],dtype="float32",comments="#")

'skip_header is the number of lines to skip.and skip_footer is from the bottom.skiprows is no longer allowed,usecols starts from 0 as columns'

```
## adding rows and columns
```python
arr=np.vstack([arr1,arr2])
arr=np.hstack([arr1,arr2])
```

## removing rows and columns
```python
    np.delete(arr,row/column,axis)
    it returns new one.
```

## to find the properties of an array
- arr.shape (3,) means those columns as there were multiple rows there shape would have two elements.
- arr.dtype
- arr.ndim
- arr.size  //no of elements
- arr.itemsize  //bytes
## indexing
- arr[2,3]
- arr[2,2:4]=5   // start index: end index: step 
- arr[:,:]
- arr%2==0 we get a boolean array.
- arr[arr%2==0] gives 1d array
- arr[condition1 & condition2]  | for or and ~ for not.
- slicing doesn't do deep copy.
- if you change a slice,original also changes.
- arr2=np.copy(slice)
- arr[tuple of tuples] gives array as output

## inbuild ways to create arrays
- np.zeros((4,5))
- np.eye(4,5)
- np.ones((3,4))
- np.full((2,2),99) np.full_like(a,99)
- np.random.seed(42)
- np.random.random((4,5))
- np.random.randn(2,3) mean 0 std 1 normal distribution.
- np.random.randint(0,100,(3,3))
- X.T for transpose
- y=x.reshape(20,1)
- z=np.arange(1,5,2) array range
- k=np.linspace(7,70,10) 10 points [7,10] array of floats.
- arr=np.copy(arr2[:,1])
- c=a+b
- b=a-d
- A+=1
- np.floort(np.random.random((2,3)))
- arr.sum(axis=0)
- arr.max()
- np.log,np.exp,np.sin,np.cos,np.sqrt,1/arr
- np.sum(arr,axis=1)
- count=np.sum(arr>1) true is one and false is zero.
- broadcasting is cool. for broadcasting the value should either be 1 or missing or same
- np.isnan(arr) gives boolean array.
- arr2=arr.nan_to_num(arr,nan=-1)
- arr.sort()
- a= a.astype('float32')
- np.any(arr>1),np.all(arr<1)

## linear algebra
```python
np.linalg.matrix_rank(arr)
np.trace(arr)
np.linalg.det(arr)
np.linalg.inv(arr)
np.linalg.matrix_power(A,3)
np.linalg.eigh(arr)
np.linalg.solve(a,b)
np.linalg.matmul(a,b)
```
## file system
- genfromtxt works even if some values are missing.
- np.savetxt("abc.txt",arr,delimiter=",")
- np.save("first",arr) saves in internal format .npy which is efficient.
- .npy files are 3 times smaller.
- np.savez("abc",arr1,arr2,arr3) will save many arrays 
- arr=load('abc.npz') arr.files  and a1=arr["arr_0"]
- np.savez_compressed(same) for compressed

## statisitics
- np.amin(arr) can use axis with all of them
- np.amax(arr)
- np.mean(arr)
- np.var(arr)
- np.std(arr)
- np.mediam(arr)
- np.percentile(arr,50)
- np.histogram(arr,bins) tells you count in each.where bins = [0,6,10] from 0 to  and 6 to ten left inclusion. if you want right inclusion instead use np.digitize(,,right=True)
- np.digitize(arr,bins=5) it shows to which bin each element belongs.

- iqr= percetile for 75 - percentile for 25
- zscore= (arr-np.mean(arr))/np.std(arr)
- np.cumsum(arr) sum of first then first two and so on.if some of conscative 25 needed you can reshape it.
- np.append(arr,[1,2,3])
- np.argmax(arr) returns index of max
- a= arr[:,[1,2,3]] first second and third column
- b=np.where(arr%2==0,1,arr) replace by 1 wherever satisfies.
- & | ~ ^

# from documentation
```python
    import numpy as np
    a=np.arange(6)
    a2=a[np.newaxis,:] go  create (1,6)

```
- indexes in numpy cannot be negative.
-  np.zeros(3) for a list like array with no rows.
- dtype=np.int64 or "int64"
- np.sort(arr)
- np.concatenate((arr1,arr2),axis=0/1)
- arr.dtype="float32" is wrong it would just now start representing int as a float now.
- arr.fill(-1) replace all by -1
- arr2=arr.copy
- boolean mask is a boolean array of same size and array and is cool to filter
- np.linalg.matmul(arr,arr2)
- np.min()
