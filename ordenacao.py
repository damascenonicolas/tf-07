def quick_sort(valores):
    
    if len(valores) <= 1:
        return valores

    pivo = valores[len(valores) // 2]

    menores = [item for item in valores if item < pivo]
  
    iguais = [item for item in valores if item == pivo]
   
    maiores = [item for item in valores if item > pivo]

   
    return quick_sort(menores) + iguais + quick_sort(maiores)

print(quick_sort([7, 3, 9, 1, 5]))
