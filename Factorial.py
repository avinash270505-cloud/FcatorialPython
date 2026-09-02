
number = 5


factorial = 1


if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
 
    for i in range(1, number + 1):
        factorial = factorial * i

   
    print("======================================")
    print("          FACTORIAL CALCULATOR")
    print("======================================")
    print("Given Number :", number)
    print("Factorial    :", factorial)
    print("======================================")
