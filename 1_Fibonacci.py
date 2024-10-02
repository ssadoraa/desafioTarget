def fibonacci(n):
    sequencia = [0, 1]
    
    while sequencia[-1] < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
        
    return sequencia

num = int(input("Informe um número: "))
sequencia = fibonacci(num)
    
if num in sequencia:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
    
print(sequencia)
