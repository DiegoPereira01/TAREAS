def ejercicio2(num): #espar
  if num%2==0:
    result = "verdadero"
  else:
    result="falso"
  return result
if __name__== "__main__":
  number = input("numero: ")
  par = ejercicio2(int (number))
  print(par)