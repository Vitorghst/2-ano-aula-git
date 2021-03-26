animais = ['Tubarao','Jacare','Morcego','Coruja','Canguru','Tigre']
#----------------------------^
print("pilha Original", animais)
print("=====================================================================")

pilhaAux = []
tirar = "Morcego"

##percorre a pilha retirando do ultimo para o primeiro
for index in range((len(animais)-1),-1,-1):
  #se o valor do livro for = ao valor solicitado para retirar ## Retira o livro
  if animais[index] == tirar:
    animais.pop()
    break
  #senao coloca o ultimo libra tirado na nova pilha e retira ela da pilha antiga
  else:
    pilhaAux.append(animais[index])
    animais.pop()

#imprimo a duas pilhas
print("Pilha Auxiliar ",pilhaAux)
print("Pilha de animais ",animais)
print("=====================================================================")
##percorrer a pilha auxiliar para emprilhar novamente o pilha atiga
for index in range((len(pilhaAux)-1),-1,-1):
  animais.append(pilhaAux[index])
  pilhaAux.pop()

#imprime a pilha sem o Livro solicitado
print("Pilha Auxiliar ",pilhaAux)
print("Pilha de animais ",animais)
