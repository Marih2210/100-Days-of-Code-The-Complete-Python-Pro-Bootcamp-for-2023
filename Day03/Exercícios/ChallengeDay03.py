print('''
*******************************************************************************
                                      --====|====--
                                            |  

                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                          `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`
*******************************************************************************
''')
print("Bem vindo ao Vellplane.")
print("Sua missão é encontrar o caminho certo que te leva até o avião.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

caminho1 = input("\nPasso 1 --> A frente se encontram 3 caminhos:\nEsquerda: Floresta calma e escura\nFrente: Caminho enevoado\nDireita: Um rio\nDigite E, F ou D para prosseguir: ").upper() 

if caminho1 == 'E' or caminho1 == 'D':
  print("\nParabéns prossiga para o próximo caminho!")
  caminho2 = input("\nPasso 2 --> Escolha entre as 2 possibilidades seguintes:\nEntrar na casa\nEntrar no edifício\nDigite C ou E para prosseguir: ").upper()
  
  if caminho2 == 'C':
    print("\nFim do jogo! Você invadiu uma propriedade particular e foi preso!")

  elif caminho2 == 'E':
    print("\nParabéns prossiga para o próximo passo!")
    caminho3 = input("\nPasso 3 --> Escolha entre as 2 opções a seguir:\nIr pelo elevador\nIr pelas escadas\nDigite Escadas ou Elevador para prosseguir: ").upper()
    if caminho3 == 'ESCADAS':
      print("\nFim do jogo! Você caiu da escada e se machucou!")
    elif caminho3 == 'ELEVADOR':
      print("\nParabéns prossiga para o último passo!")
      caminho4 = input("\nPasso 3 --> Escolha dentre os 6 andares a seguir e descubra se é nele que o avião está:\nAndar 1\nAndar 2\nAndar 3\nAndar 4\nAndar 5\nAndar 6\nDigite 1, 2, 3, 4, 5 ou 6 para prosseguir: ")
      if caminho4 == '5':
        print("\nVocê encontrou o avião e pode embarcar no Vellplane, Parabéns!")
      elif caminho4 == '1' or caminho4 == '2' or caminho4 == '3' or caminho4 == '4' or caminho4 == '6':
        print("\nFim do jogo! O avião não está nesse andar!")
elif caminho1 == 'F':
  print("\nFim do jogo! Você foi capturado por bandidos escondidos dentro da neblina!")
else:
  print("\nInformação inválida para prosseguir!")
