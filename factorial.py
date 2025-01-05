# givenNumber = int(input("Enter number for factorial"))
# factorialNum = 1
# for num in range(givenNumber, 1, -1):
#     factorialNum = (factorialNum * num)
#     print(f"the result of {givenNumber - num +1} is {factorialNum}")
# print(f"the final value is {factorialNum}")
# -------------------------------------------------------------------------------
# givenNumber = int(input("Enter a number: "))
#
# if givenNumber <= 1:
#     print(f"The given number {givenNumber} is not a prime number.")
# else:
#     isPrime = True
#     for i in range(2, int(givenNumber ** 0.5) + 1):  # Check divisors up to the square root of the number
#         if givenNumber % i == 0:
#             isPrime = False
#             break
#
#     if isPrime:
#         print(f"The given number {givenNumber} is a prime number.")
#     else:
#         print(f"The given number {givenNumber} is not a prime number.")
# --------------------------------------------------------------------------------------

givenString = "string"
print(givenString[::-1])
