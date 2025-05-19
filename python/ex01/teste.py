n = int(input())  
valores = list(map(int, input().split()))  

maior_sequencia = 1  
sequencia_atual = 1  

for i in range(1, n):
    if valores[i] == valores[i - 1]:  
        sequencia_atual += 1
    else:
        maior_sequencia = max(maior_sequencia, sequencia_atual)  
        sequencia_atual = 1  

maior_sequencia = max(maior_sequencia, sequencia_atual)  
print(maior_sequencia)