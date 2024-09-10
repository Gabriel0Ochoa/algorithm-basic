resultados = [] 
import math
def calculadora():
  while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /, pi*): ")

    if operacion == '+':
      resultado = num1 + num2
    elif operacion == '-':
      resultado = num1 - num2
    elif operacion == '*':
      resultado = num1 * num2
    elif operacion == '/':
      if num2 == 0:
        print("Error: División por cero")
        continue
      else:
        resultado = num1 / num2
    elif operacion == 'pi*':
      resultado = (f"{num1} * pi {num1 * math.pi}  y {num2} * pi {num2 * math.pi}")
    else:
      print("Operación inválida")
      continue
    resultados.append(resultado)
    print("El resultado es:", resultado)

    if len(resultados) > 1:
        print("\nComparación de resultados:")
        for i in range(len(resultados) - 1):
            if resultados[i] > resultados[i+1]:
                print(f"El resultado {i+1} es mayor que el resultado {i+2}")
            elif resultados[i] < resultados[i+1]:
                print(f"El resultado {i+1} es menor que el resultado {i+2}")
            else:
                print(f"El resultado {i+1} es igual al resultado {i+2}")

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
      break

  print("Resultados de todas las operaciones:")
  for resultado in resultados:
    print(resultado)

calculadora()