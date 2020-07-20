def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average of 1s student is", cal_average([18,25,3,41,5]))
print("The average of 2nd student is", cal_average([8,5,3,4,9]))
