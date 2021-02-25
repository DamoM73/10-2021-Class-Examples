# while loop example
test_result = 0

# Set maximum and minimum to first test result
max_result = 0
min_result = 100

while test_result != -1:
    # get next result value
    test_result = int(input("Please enter test result (-1 to finish): "))
    
    # check for new maxand min
    if test_result > max_result:
        max_reult = test_result
    elif test_result < min_result:
        min_result = test_result
           
# print results
print("\nMaximum test result =", max_result)
print("Minimum test result =", min_result)