# simple calculator basic arthimetic operation such as ( + - / * )
# starting with the operator we have to input those ( + - / * )

operator = input("Enter an operator(+ - / *):").strip()
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter thr 2nd number:"))

# now using condition statement or operator we can say
if operator == "+":
    result = num1 + num2
    print(round(result,3)) # here 3 indicates 3 decimal places
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")



