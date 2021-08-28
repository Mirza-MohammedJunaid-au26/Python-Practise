start = int(input("Enter Starting Point : "))
end = int(input("Enter Ending Point : "))

for i in range(start,end):
    if(i%3==0 and i%5==0):
        print(f"Number is {i} FIZZ_FUZZ")
    elif(i%3==0):
        print(f"Number is {i} Fizz")
    elif(i%5==0):
        print(f"Number is {i} FUZZ")
    else:
        print(i)