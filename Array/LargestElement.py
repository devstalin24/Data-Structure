# My solution Solition 1 
# assume first element of array is largest and  store in variable(largest)
#  start comparing the value from list[1] ----list[n] if  element is  larger then largest change 
#largest value and continue comapring till list[n]
O(n)
latgest = 0
Test_cases = int(input("Enter the number of test cases"))
for i in range(0,Test_cases):
    Total_numbers_count = input("Enter the number's cout")
    Numbers  = input("Enter the number with space seperated")
    number_ist = Numbers.split(" ")
    if len(number_ist) == 0:
        print("Empty list")
    elif len(number_ist) ==1:
        print(number_ist[0])
    else:
        for k in range(0,len(number_ist)):
            number_ist[k] = int(number_ist[k])
        largest = number_ist[0]
        for j in range(1,len(number_ist)):
            print(f"{number_ist[j]}   {largest} ")
            print(type(number_ist[0]))
            if largest <number_ist[j]:
                largest = number_ist[j]
                #print(largest)
        print(largest)





