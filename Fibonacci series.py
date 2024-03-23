def fibonacci_series(n):
    if(n<=0):
        return ''
    elif(n==1):
        return '0'
    else:
        series=[0,1]
        while len(series)<n:
          next_digit=series[-1]+series[-2]
          series.append(next_digit)
        return series
n=int(input("Enter the range of the series:\n"))
output=fibonacci_series(n)
print(*output,sep=',')