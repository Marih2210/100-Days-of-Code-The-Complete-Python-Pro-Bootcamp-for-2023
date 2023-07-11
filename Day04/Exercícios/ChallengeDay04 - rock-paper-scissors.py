import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Bem vindo ao jogo de pedra, papel e tesoura!")
 
lista_jogo = [pedra, papel, tesoura]
lista_jogo_tamanho = len(lista_jogo)

escolha_pc = random.randint(0, lista_jogo_tamanho - 1)
escolha_user = int(input("Digite 0 para pedra, 1 para papel e 2 para tesoura:\n")) 

print(f"\nSua escolha: {lista_jogo[escolha_user]}")
print(f"Escolha do computador: {lista_jogo[escolha_pc]}")

if (escolha_user == escolha_pc):
    print("Empate!")
else:
    if (escolha_user == 0 and escolha_pc == 2):
        print("Você ganhou!")
    elif (escolha_user == 1 and escolha_pc == 0):
        print("Você ganhou!")
    elif (escolha_user == 2 and escolha_pc == 1):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
