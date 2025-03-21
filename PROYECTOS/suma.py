def ejercicio1(a, b, c):
  result = a + b + c
  return result
if __name__== "__main__":
  number1 = input("number1: ")
  number2 = input("number2: ")
  number3 = input("number3: ")
  num = ejercicio1(int(number1),int(number2),int(number3))
  print(num)