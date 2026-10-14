numdays=int(input("Enter number of days"))

sum=0

for i in range(numdays):
    days=int(input("enter number of day"))
    sum=sum+days
average=round(sum/numdays,2)

print(f"the average temprature in day is {average}")
