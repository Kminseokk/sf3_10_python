import numpy as np

arr_ = [1, 1, 2, 3, 4, 5, 5, 5,5, 7, 8, 9, 10, 11, 24 ,100]

# 1 중복 제거
unique_arr, indexs, counts = np.unique(arr_ , return_counts= True, return_index= True)

print("#1 : \n", unique_arr) #, counts, indexs

# 1 결과의 최대 최소 평균
print("#2 : \n")
print("최대", np.max(unique_arr))
print("최소", np.min(unique_arr))
print("평균", np.mean(unique_arr))

# 1 결과의 모든 합
print("#3 : \n")
print("총합", np.sum(unique_arr))

# 중복 제거안한 배열의 중간값
print("#4 : \n")
print("중간", np.median(arr_))