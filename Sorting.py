import numpy as np
 
>>> a
array([[ 2,  7,  4,  2],
       [35,  9,  1,  5],
       [22, 12,  3,  2]])
 
按最后一列顺序排序
>>> a[np.lexsort(a.T)]
array([[22, 12,  3,  2],
       [ 2,  7,  4,  2],
       [35,  9,  1,  5]])
 
按最后一列逆序排序
>>>a[np.lexsort(-a.T)]
array([[35,  9,  1,  5],
       [ 2,  7,  4,  2],
       [22, 12,  3,  2]])
 
按第一列顺序排序
>>> a[np.lexsort(a[:,::-1].T)]
array([[ 2,  7,  4,  2],
       [22, 12,  3,  2],
       [35,  9,  1,  5]])
 
按最后一行顺序排序
>>> a.T[np.lexsort(a)].T
array([[ 2,  4,  7,  2],
       [ 5,  1,  9, 35],
       [ 2,  3, 12, 22]])
 
按第一行顺序排序
>>> a.T[np.lexsort(a[::-1,:])].T
array([[ 2,  2,  4,  7],
       [ 5, 35,  1,  9],
       [ 2, 22,  3, 12]])
