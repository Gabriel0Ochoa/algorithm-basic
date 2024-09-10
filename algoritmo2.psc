Algoritmo Calculadora
	
    Definir num1, num2, resultado Como Real
    Definir operacion, continuar Como Caracter
	
    Repetir
        Escribir "Ingrese el primer número:"
        Leer num1
        Escribir "Ingrese el segundo número:"
        Leer num2
        Escribir "Ingrese la operación (+, -, *, /):"
        Leer operacion
		
        Segun operacion Hacer
            "+":
                resultado <- num1 + num2
            "-":
                resultado <- num1 - num2
            "*":
                resultado <- num1 * num2
            "/":
                Si num2 = 0 Entonces
                    Escribir "Error: División por cero"
                SiNo
                    resultado <- num1 / num2
                FinSi
            De Otro Modo:
                Escribir "Operación inválida"
        FinSegun
		
        Escribir "El resultado es:", resultado
		
        Escribir "¿Desea continuar? (s/n):"
        Leer continuar
    Hasta Que Mayusculas(continuar) <> "S"
	
FinAlgoritmo