import math
Ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
Median = 0

def getMean(arr):
    summation = sum(arr)
    Mean = summation/len(arr)
    return Mean
    
def getMedian(arr):
    middle = 0
    #if the length of array is odd 
    if (len(arr) %2 !=0):
        middle = arr[math.ceil((len(arr) -1)/2)]
    #if the length of array is even 
    else:
        middle = (arr[math.floor((len(arr) -1)/2)]+arr[math.ceil((len(arr)-1)/2)])/2
    return middle
    
def getStandardDeviation(arr):
    sd = 0.0;
    sd_arr = []
    for item in arr:
       sd = float((item - getMean(arr))**2)
       sd_arr.append(sd)
    sd_sum = float(sum(sd_arr))
    return (float(sd_sum/len(arr))**.5)

Mean = getMean(Ages)
print(Mean)#Mean Val (29.9)

Median = getMedian(Ages)
print(Median)#Median Val (25)

standard_Deviation = getStandardDeviation(Ages)
print(standard_Deviation)#standard_Deviation Val (12.7)