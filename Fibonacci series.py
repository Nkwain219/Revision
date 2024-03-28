num1=int(input("Enter the first number of the series:"))
num2=int(input("Enter the second number of the series:"))
def fibonacci_series(n):
    if(n<=0):
        return ''
    elif(n==1):
        return f"{num1}"
    else:
        series=[num1,num2]
        while len(series)<n:
          next_digit=series[-1]+series[-2]
          series.append(next_digit)
        return series
n=int(input("Enter the range of the series:\n"))
output=fibonacci_series(n)
print(*output,sep=',')