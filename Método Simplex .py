def buscarMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i and nr > 0:
            i = nr
    return i

continuar = 0

while continuar != "n" and continuar != "nao":
    
    print("=====================================================================================================================================================")
    print("|                                                      INSTRUÇÕES PARA O USO DO PROGRAMA                                                             |")
    print("|                                                                                                                                                    |")
    print("|  -ATENÇÃO AO INSERIR OS VALORES                                                                                                                    |")
    print("|  -CASO O VALOR DE X1 OU X2 SEJA 0, INSERIR 0.001 SE NÃO DARÁ ERRO                                                                                  |")
    print("|  -CASO QUERIA FAZER APENAS COM 2 RETRIÇÕES, INSERIR 0.001  NOS VALORES DA 3 RESTRIÇÃO E IGNORAR A ULTIMA LINHA DO PRINT                            |")
    print("|                                                                                                                                                    |")
    print("|                                                                                                                                                    |")
    print("======================================================================================================================================================")
        
    #Função Objetivo

    z = float(input("Defina o valor de z: "))
    x1 = float(input("Defina o valor de x1:"))
    x2 = float(input("Defina o valor de x2:"))
    xf1 = float(input("Diga o valor de xf1: "))
    xf2 = float(input("Diga o valor de xf2: "))
    xf3 = float(input("Diga o valor de xf3: "))
    b = float(input("Defina o valor final de B: "))

    #Restrições

    #1 Restrição
    r1x1 = float(input("Valor de x1 da 1º Restrição: "))
    r1x2 = float(input("Valor de x2 da 1º Restrição: "))
    r1xf1 = float(input("Diga o valor de xf1 da 1º restrição: "))
    r1xf2 = float(input("Diga o valor de xf2 da 1º restrição: "))
    r1xf3 = float(input("Diga o valor de xf3 da 1º restrição: "))
    r1b = float(input("Valor Final de B da 1º restrição : "))

    #2  Restrição
    r2x1 = float(input("Valor de x1 da 2º Restrição: "))
    r2x2 = float(input("Valor de x2 da 2º Restrição: "))
    r2xf1 = float(input("Diga o valor de xf1 da 2º restrição: "))
    r2xf2 = float(input("Diga o valor de xf2 da 2º restrição: "))
    r2xf3 = float(input("Diga o valor de xf3 da 2º restrição: "))
    r2b = float(input("Valor Final de B da 2º restrição : "))

    #3 Restrição

    r3x1 = float(input("Valor de x1 da 3º Restrição: "))
    r3x2 = float(input("Valor de x2 da 3º Restrição: "))
    r3xf1 = float(input("Diga o valor de xf1 da 3º restrição: "))
    r3xf2 = float(input("Diga o valor de xf2 da 3º restrição: "))
    r3xf3 = float(input("Diga o valor de xf3 da 3º restrição: "))
    r3b = float(input("Valor Final de B da 3º restrição : "))

    #1 tabela

    print("=====================================================================================================================================================")
    print("|                                                      PRIMEIRA TABELA                                                                               |")
    print("|                                                                                                                                                    |")
    print("|    Z     |    X1      |    X2      |      XF1     |    XF2     |      XF3    |      B                                                              |")                                                                                                           
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------|") 
    print("|    ",z,"  |    ",x1,"  |    ",x2,"  |  ",   xf1,"  |    ",xf2,"  |    ",xf3,"  |  ",b,"                                                            |")
    print("|    ",0,"  |   ",r1x1," |   ",r1x2," |    ",r1xf1," |   ",r1xf2," | ",r1xf3,"   | ",r1b,"                                                           |")
    print("|    ",0,"  |   ",r2x1," |   ",r2x2," |   ",r2xf1,"  |   ",r2xf2," | ",r2xf3,"   | ",r2b,"                                                           |")
    print("|    ",0,"  |   ",r3x1," |   ",r3x2," |   ",r3xf1,"  |   ",r3xf2," | ",r3xf3,"   | ",r3b,"                                                           |")                                                                                                                                                 
    print("======================================================================================================================================================")

    #1º Passo: identificar a variavel que entra (Vertical)(Função Objetivo com maior número negativo)
    
    print("\n 1º Passo: \n")
    
    if x1 > x2:
        v1 = x2
    else:
        v1 = x1
    print("\n Váriavel de entrada: ",v1)

    #2º Passo: identificar a variavel que sai(Horizontal)(Resultado com menor positivo)
    print("\n 2º Passo:")
    if v1 == x1:
        mp1 = r1b / r1x1 
        mp2 = r2b / r2x1 
        mp3 = r3b / r3x1 
        
        listaDecimais = [mp1, mp2, mp3]
        menor = buscarMenor(listaDecimais)
        print(r1b," / ",r1x1," = ", mp1 )
        print(r2b," / ",r2x1," = ", mp2 )
        print(r3b," / ",r3x1," = ", mp3 )
        print("\n Várivaveel de saida:", menor)
    elif v1 == x2:
        mp1 = r1b / r1x2 
        mp2 = r2b / r2x2 
        mp3 = r3b / r3x2 

        listaDecimais = [mp1, mp2, mp3]
        menor = buscarMenor(listaDecimais)
        print(r1b," / ",r1x2," = ", mp1 )
        print(r2b," / ",r2x2," = ", mp2 )
        print(r3b," / ",r3x2," = ", mp3 )
        print("\n Várivaveel de saida:", menor)

    #3º Passo: identificar o elemento pivo(Onde as linhas se cruzam)
    print("\n 3º Passo:")

    
    if r1b / r1x2 == menor:
        pivo = r1x2
    elif r2b / r2x2 == menor:
        pivo = r2x2
    elif r3b / r3x2 == menor:
        pivo = r3x2
    elif r1b / r1x1 == menor:
        pivo = r1x1
    elif r2b / r2x1 == menor:
        pivo = r2x1
    elif r3b / r3x1 == menor:
        pivo = r3x1

    print("\n Pivo: ", pivo)

    #4 Passo: Calcular a nova linha pivo
    print("\n 4º Passo: \n")

    if pivo == r1x1:
        nlx1 = r1x1 / pivo
        nlx2 = r1x2 / pivo
        nlxf1 = r1xf1 / pivo
        nlxf2 = r1xf2 / pivo
        nlxf3 = r1xf3 / pivo
        nlb = r1b / pivo
        print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha pivo")

    elif pivo == r1x2:
        nlx1 = r1x1 / pivo
        nlx2 = r1x2 / pivo
        nlxf1 = r1xf1 / pivo
        nlxf2 = r1xf2 / pivo
        nlxf3 = r1xf3 / pivo
        nlb = r1b / pivo
        print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha pivo")

    elif pivo == r2x1:
        nlx1 = r2x1 / pivo
        nlx2 = r2x2 / pivo
        nlxf1 = r2xf1 / pivo
        nlxf2 = r2xf2 / pivo
        nlxf3 = r2xf3 / pivo
        nlb = r2b / pivo
        print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha Pivo")

    elif pivo == r2x2:  
        nlx1 = r2x1 / pivo
        nlx2 = r2x2 / pivo
        nlxf1 = r2xf1 / pivo
        nlxf2 = r2xf2 / pivo
        nlxf3 = r2xf3 / pivo
        nlb = r2b / pivo
        print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha Pivo")
        
    elif pivo == r3x1:
        nlx1 = r3x1 / pivo
        nlx2 = r3x2 / pivo
        nlxf1 = r3xf1 / pivo
        nlxf2 = r3xf2 / pivo
        nlxf3 = r3xf3 / pivo
        nlb = r3b / pivo
        print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha Pivo")

    elif pivo == r3x2:
        nlx1 = r3x1 / pivo
        nlx2 = r3x2 / pivo
        nlxf1 = r3xf1 / pivo
        nlxf2 = r3xf2 / pivo
        nlxf3 = r3xf3 / pivo
        nlb = r3b / pivo
        print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
        print("Dividir pelo pivo: /", pivo)
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb," = Nova linha Pivo")
        
    #5 Passo: Calcular novas linhas com base

    print("\n 5º Passo: \n")

    #multiplicar pela entrada

    if v1 < 0:
        positivov1 = abs(v1) #positivar a entrada
        novalinhaz =  0 * positivov1
        novalinhax1 = nlx1 * positivov1
        novalinhax2 = nlx2 * positivov1
        novalinhaxf1 = nlxf1 * positivov1
        novalinhaxf2 = nlxf2 * positivov1
        novalinhaxf3 = nlxf3 * positivov1
        novalinhab = nlb * positivov1

        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb) #linha pivo
        print("Multiplicar pela entrada: X", positivov1)
        print(0," | ",novalinhax1," | ",novalinhax2," | ",novalinhaxf1," | ",novalinhaxf2," | ",novalinhaxf3," | ",novalinhab, "")
    elif v1 > 0:
        negativo = v1 * -1
        novalinhaz =  0 * negativo #negativar a entrada
        novalinhax1 = nlx1 * negativo
        novalinhax2 = nlx2 * negativo
        novalinhaxf1 = nlxf1 * negativo
        novalinhaxf2 = nlxf2 * negativo
        novalinhaxf3 = nlxf3 * negativo
        novalinhab = nlb * negativo
        print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb) #linha pivo
        print("Multiplicar pela entrada: X", negativo)
        print(0," | ",novalinhax1," | ",novalinhax2," | ",novalinhaxf1," | ",novalinhaxf2," | ",novalinhaxf3," | ",novalinhab, "")
        

    #somar com a primeira linha:
    print("Somar com a 1 linha: ")
    print(z," | ",x1," | ",x2," | ",xf1," | ",xf2," | ",xf3," | ",b)

    nlpz = 0 + z
    nlpx1 = novalinhax1 + x1
    nlpx2 =  novalinhax2 + x2
    nlpxf1 =  novalinhaxf1 + xf1
    nlpxf2 =  novalinhaxf2 + xf2
    nlpxf3 = novalinhaxf3 + xf3
    nlpb = novalinhab + b

    print(nlpz," | ",nlpx1," | ",nlpx2," | ",nlpxf1," | ",nlpxf2," | ",nlpxf3," | ",nlpb," = nova primeira linha \n")

    #repetição com a nova linha pivo

    if pivo == r1x1:
        if r2x1 > 0:
            r1x1negativo = r2x1 * -1
            linhax1 = nlx1 * r1x1negativo
            linhax2 = nlx2 * r1x1negativo
            linhaxf1 =  nlxf1 * r1x1negativo
            linhaxf2 = nlxf2 * r1x1negativo
            linhaxf3 = nlxf3 * r1x1negativo
            linhab = nlb * r1x1negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Mulitplicado por: X", r1x1negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl3x1 = linhax1 + r2x1
            nl3x2 = linhax2 + r2x2
            nl3xf1 = linhaxf1 + r2xf1
            nl3xf2 = linhaxf2 + r2xf2
            nl3xf3 = linhaxf3 + r2xf3
            nl3b = linhab +  r2b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova terceira linha \n")
        else: 
            r1x1positivo = abs(r2x1)
            linhax1 = nlx1 * r1x1positivo
            linhax2 = nlx2 * r1x1positivo
            linhaxf1 =  nlxf1 * r1x1positivo
            linhaxf2 = nlxf2 * r1x1positivo
            linhaxf3 = nlxf3 * r1x1positivo
            linhab = nlb * r1x1positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Mulitplicado por: X", r1x1positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl3x1 = linhax1 + r2x1
            nl3x2 = linhax2 + r2x2
            nl3xf1 = linhaxf1 + r2xf1
            nl3xf2 = linhaxf2 + r2xf2
            nl3xf3 = linhaxf3 + r2xf3
            nl3b = linhab +  r2b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova terceira linha \n") 
    elif pivo == r1x2:
        if r2x2 > 0:
            r1x2negativo = r2x2 - r2x2 * 2
            linhax1 = nlx1 * r1x2negativo
            linhax2 = nlx2 * r1x2negativo
            linhaxf1 =  nlxf1 * r1x2negativo
            linhaxf2 = nlxf2 * r1x2negativo
            linhaxf3 = nlxf3 * r1x2negativo
            linhab = nlb * r1x2negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r1x2negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl3x1 = linhax1 + r2x1
            nl3x2 = linhax2 + r2x2
            nl3xf1 = linhaxf1 + r2xf1
            nl3xf2 = linhaxf2 + r2xf2
            nl3xf3 = linhaxf3 + r2xf3
            nl3b = linhab +  r2b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova terceira linha \n")
        else:
            r2x1positivo = abs(r2x2)
            linhax1 = nlx1 * r2x1positivo
            linhax2 = nlx2 * r2x1positivo
            linhaxf1 =  nlxf1 * r2x1positivo
            linhaxf2 = nlxf2 * r2x1positivo
            linhaxf3 = nlxf3 * r2x1positivo
            linhab = nlb * r2x1positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r2x1positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl3x1 = linhax1 + r2x1
            nl3x2 = linhax2 + r2x2
            nl3xf1 = linhaxf1 + r2xf1
            nl3xf2 = linhaxf2 + r2xf2
            nl3xf3 = linhaxf3 + r2xf3
            nl3b = linhab +  r2b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova terceira linha \n")

    elif pivo == r2x1:
        if r1x1 > 0:
            r2x1negativo = r1x1 * -1
            linhax1 = nlx1 * r2x1negativo
            linhax2 = nlx2 * r2x1negativo
            linhaxf1 =  nlxf1 * r2x1negativo
            linhaxf2 = nlxf2 * r2x1negativo
            linhaxf3 = nlxf3 * r2x1negativo
            linhab = nlb * r2x1negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r2x1negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")
        else:
            r2x1positivo = abs(r1x1)
            linhax1 = nlx1 * r2x1positivo
            linhax2 = nlx2 * r2x1positivo
            linhaxf1 =  nlxf1 * r2x1positivo
            linhaxf2 = nlxf2 * r2x1positivo
            linhaxf3 = nlxf3 * r2x1positivo
            linhab = nlb * r2x1positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r2x1positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")
    elif pivo == r2x2:
        if r1x2 > 0:
            r2x2negativo = r1x2 * -1
            linhax1 = nlx1 * r2x2negativo
            linhax2 = nlx2 * r2x2negativo
            linhaxf1 =  nlxf1 * r2x2negativo
            linhaxf2 = nlxf2 * r2x2negativo
            linhaxf3 = nlxf3 * r2x2negativo
            linhab = nlb * r2x2negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r2x2negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")
        else:
            r2x2positivo = abs(r2x2)
            linhax1 = nlx1 * r2x2positivo
            linhax2 = nlx2 * r2x2positivo
            linhaxf1 =  nlxf1 * r2x2positivo
            linhaxf2 = nlxf2 * r2x2positivo
            linhaxf3 = nlxf3 * r2x2positivo
            linhab = nlb * r2x2positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r2x2positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab) 
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")    

    elif pivo == r3x1:
        if r3x1 > 0:
            r3x1negativo = r1x1 * -1
            linhax1 = nlx1 * r3x1negativo
            linhax2 = nlx2 * r3x1negativo
            linhaxf1 =  nlxf1 * r3x1negativo
            linhaxf2 = nlxf2 * r3x1negativo
            linhaxf3 = nlxf3 * r3x1negativo
            linhab = nlb * r3x1negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r3x1negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")
        else: 
            r3x1positivo = abs(r1x1)
            linhax1 = nlx1 * r3x1positivo
            linhax2 = nlx2 * r3x1positivo
            linhaxf1 =  nlxf1 * r3x1positivo
            linhaxf2 = nlxf2 * r3x1positivo
            linhaxf3 = nlxf3 * r3x1positivo
            linhab = nlb * r3x1positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r3x1positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")   
    elif pivo == r3x2:       
        if r1x2 > 0:
            r3x2negativo = r1x2 * -1
            linhax1 = nlx1 * r3x2negativo
            linhax2 = nlx2 * r3x2negativo
            linhaxf1 =  nlxf1 * r3x2negativo
            linhaxf2 = nlxf2 * r3x2negativo
            linhaxf3 = nlxf3 * r3x2negativo
            linhab = nlb * r3x2negativo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r3x2negativo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")
        else:
            r3x2positivo = abs(r1x2)
            linhax1 = nlx1 * r3x2positivo
            linhax2 = nlx2 * r3x2positivo
            linhaxf1 =  nlxf1 * r3x2positivo
            linhaxf2 = nlxf2 * r3x2positivo
            linhaxf3 = nlxf3 * r3x2positivo
            linhab = nlb * r3x2positivo
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = Linha pivo") #linha pivo
            print("Mulitplicado por: X", r3x2positivo)
            print(0," | ",linhax1," | ",linhax2," | ",linhaxf1," | ",linhaxf2," | ",linhaxf3," | ",linhab)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl3x1 = linhax1 + r1x1
            nl3x2 = linhax2 + r1x2
            nl3xf1 = linhaxf1 + r1xf1
            nl3xf2 = linhaxf2 + r1xf2
            nl3xf3 = linhaxf3 + r1xf3
            nl3b = linhab +  r1b
            print(0," | ",nl3x1," | ",nl3x2," | ",nl3xf1," | ",nl3xf2," | ",nl3xf3," | ",nl3b," = nova segunda linha \n")

    #segunda repetição com linha pivo

    if pivo == r1x1:
        if r3x1 > 0:
            negativo4 = r3x1 * -1
            ultimonegativox1 =  nlx1 * negativo4
            ultimonegativox2 =  nlx2 * negativo4
            ultimonegativoxf1 =  nlxf1 * negativo4
            ultimonegativoxf2 =  nlxf2 * negativo4
            ultimonegativoxf3 =  nlxf3 * negativo4
            ultimonegativob =  nlb * negativo4

            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", negativo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 4 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  4 linha \n") 
        else:
            positivo4 = abs(r3x1)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4

            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 4 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  4 linha \n") 
    elif pivo == r1x2:
        if r3x2 > 0:
            positivo4 = r3x2 * -1
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4

            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 4 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  4 linha \n") 
        else:
            positivo4 = abs(r3x2)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4

            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 4 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  4 linha \n") 

    elif pivo == r2x1:
        if r3x1 > 0:
            positivo4 = r3x1 * -1
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 2 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  2 linha \n") 
        else: 
            positivo4 = abs(r1x1)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 2 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  2 linha \n") 
    elif pivo == r2x2:
        if r3x2 > 0:
            positivo4 = r3x2 * -1
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 2 linha:")
            print(0," | ",r3x1," | ",r3x2," | ",r3xf1," | ",r3xf2," | ",r3xf3," | ",r3b)
            nl4x1 = ultimonegativox1 + r3x1
            nl4x2 = ultimonegativox2 + r3x2
            nl4xf1 = ultimonegativoxf1 + r3xf1
            nl4xf2 = ultimonegativoxf2 + r3xf2
            nl4xf3 = ultimonegativoxf3 + r3xf3
            nl4b = ultimonegativob +  r3b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  2 linha \n") 
        else:
            positivo4 = abs(r1x2)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 2 linha:")
            print(0," | ",r1x1," | ",r1x2," | ",r1xf1," | ",r1xf2," | ",r1xf3," | ",r1b)
            nl4x1 = ultimonegativox1 + r1x1
            nl4x2 = ultimonegativox2 + r1x2
            nl4xf1 = ultimonegativoxf1 + r1xf1
            nl4xf2 = ultimonegativoxf2 + r1xf2
            nl4xf3 = ultimonegativoxf3 + r1xf3
            nl4b = ultimonegativob +  r1b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  2 linha \n") 

    elif pivo == r3x1:
        if r2x1 > 0:
            positivo4 = r2x1 * -1
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl4x1 = ultimonegativox1 + r2x1
            nl4x2 = ultimonegativox2 + r2x2
            nl4xf1 = ultimonegativoxf1 + r2xf1
            nl4xf2 = ultimonegativoxf2 + r2xf2
            nl4xf3 = ultimonegativoxf3 + r2xf3
            nl4b = ultimonegativob +  r2b
            print(0," | ",nl4x1," | ",nl4x2," | ",nl4xf1," | ",nl4xf2," | ",nl4xf3," | ",nl4b," = nova  3 linha \n") 
        else:
            positivo4 = abs(r2x1)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",ultimonegativox1," | ",ultimonegativox2," | ",ultimonegativoxf1," | ",ultimonegativoxf2," | ",ultimonegativoxf3," | ", ultimonegativob)
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl4x1 = ultimonegativox1 + r2x1
            nl4x2 = ultimonegativox2 + r2x2
            nl4xf1 = ultimonegativoxf1 + r2xf1
            nl4xf2 = ultimonegativoxf2 + r2xf2
            nl4xf3 = ultimonegativoxf3 + r2xf3
            nl4b = ultimonegativob +  r2b
            print(0," | ",round(nl4x1,3)," | ",round(nl4x2,3)," | ",round(nl4xf1,3)," | ",round(nl4xf2,3)," | ",round(nl4xf3,3)," | ",round(nl4b,3)," = nova  3 linha \n") 
    elif pivo == r3x2:
        if r2x2 > 0:
            positivo4 = r2x2 * -1
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",round(ultimonegativox1,3)," | ",round(ultimonegativox2,3)," | ",round(ultimonegativoxf1,3)," | ",round(ultimonegativoxf2,3)," | ",round(ultimonegativoxf3,3)," | ", round(ultimonegativob,3))
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl4x1 = ultimonegativox1 + r2x1
            nl4x2 = ultimonegativox2 + r2x2
            nl4xf1 = ultimonegativoxf1 + r2xf1
            nl4xf2 = ultimonegativoxf2 + r2xf2
            nl4xf3 = ultimonegativoxf3 + r2xf3
            nl4b = ultimonegativob +  r2b
            print(0," | ",round(nl4x1,3)," | ",round(nl4x2,3)," | ",round(nl4xf1,3)," | ",round(nl4xf2,3)," | ",round(nl4xf3,3)," | ",round(nl4b,3)," = nova  3 linha \n")
        else:
            positivo4 = abs(r2x2)
            ultimonegativox1 =  nlx1 * positivo4
            ultimonegativox2 =  nlx2 * positivo4
            ultimonegativoxf1 =  nlxf1 * positivo4
            ultimonegativoxf2 =  nlxf2 * positivo4
            ultimonegativoxf3 =  nlxf3 * positivo4
            ultimonegativob =  nlb * positivo4
            print(0," | ",nlx1," | ",nlx2," | ",nlxf1," | ",nlxf2," | ",nlxf3," | ",nlb, " = nova Linha pivo") #linha pivo
            print("Multiplicar por: X", positivo4)
            print(0," | ",round(ultimonegativox1,3)," | ",round(ultimonegativox2,3)," | ",round(ultimonegativoxf1,3)," | ",round(ultimonegativoxf2,3)," | ",round(ultimonegativoxf3,3)," | ", round(ultimonegativob,3))
            print("Somar com a 3 linha:")
            print(0," | ",r2x1," | ",r2x2," | ",r2xf1," | ",r2xf2," | ",r2xf3," | ",r2b)
            nl4x1 = ultimonegativox1 + r2x1
            nl4x2 = ultimonegativox2 + r2x2
            nl4xf1 = ultimonegativoxf1 + r2xf1
            nl4xf2 = ultimonegativoxf2 + r2xf2
            nl4xf3 = ultimonegativoxf3 + r2xf3
            nl4b = ultimonegativob +  r2b
            print(0," | ",round(nl4x1,3)," | ",round(nl4x2,3)," | ",round(nl4xf1,3)," | ",round(nl4xf2,3)," | ",round(nl4xf3,3)," | ",round(nl4b,3)," = nova  3 linha \n")  



    #6 Passo: Noba Tabela

    if pivo == r1x1 or pivo == r1x2:
        print("===========================================================================================================================================================================================================")
        print("|                                                      NOVA TABELA                                                                                                                                         |")
        print("|                                                                                                                                                                                                          |")
        print("|    Z     |    X1      |    X2      |      XF1     |    XF2     |      XF3    |      B                                                                                                                    |")                                                                                                           
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|") 
        print("|    ",round(nlpz,3),"  |    ",round(nlpx1,3),"  |    ",round(nlpx2,3),"  |  ",   round(nlpxf1,3),"  |    ",round(nlpxf2,3),"  |    ",round(nlpxf3,3),"  |     ",round(nlpb,3),"                           |")
        print("|    ",0,"  |   ",round(nlx1,3)," |   ",round(nlx2,3)," |    ",round(nlxf1,3)," |   ",round(nlxf2,3)," | ",round(nlxf3,3),"   | ",round(nlb,3),"                                                           |")
        print("|    ",0,"  |   ",round(nl3x1,3)," |   ",round(nl3x2,3)," |   ",round(nl3xf1,3),"  |   ",round(nl3xf2,3)," | ",round(nl3xf3,3),"   | ",round(nl3b,3),"                                                     |")
        print("|    ",0,"  |   ",round(nl4x1,3)," |   ",round(nl4x2,3)," |   ",round(nl4xf1),"  |   ",round(nl4xf2,3)," | ",round(nl4xf3,3),"   | ",round(nl4b,3),"                                                       |")                                                                                                                                                 
        print("===========================================================================================================================================================================================================")
    elif pivo == r2x1 or pivo == r2x2:
        print("===========================================================================================================================================================================================================")
        print("|                                                      NOVA TABELA                                                                                                                                         |")
        print("|                                                                                                                                                                                                          |")
        print("|    Z     |    X1      |    X2      |      XF1     |    XF2     |      XF3    |      B                                                                                                                    |")                                                                                                           
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|") 
        print("|    ",round(nlpz,3),"  |    ",round(nlpx1,3),"  |    ",round(nlpx2,3),"  |  ",   round(nlpxf1,3),"  |    ",round(nlpxf2,3),"  |    ",round(nlpxf3,3),"  |     ",round(nlpb,3),"                           |")
        print("|    ",0,"  |   ",round(nl3x1,3)," |   ",round(nl3x2,3)," |    ",round(nl3xf1,3)," |   ",round(nl3xf2,3)," | ",round(nl3xf3,3),"   | ",round(nl3b,3),"                                                     |")
        print("|    ",0,"  |   ",round(nlx1,3)," |   ",round(nlx2,3)," |   ",round(nlxf1,3),"  |   ",round(nlxf2,3)," | ",round(nlxf3,3),"   | ",round(nlb,3),"                                                           |")
        print("|    ",0,"  |   ",round(nl4x1,3)," |   ",round(nl4x2,3)," |   ",round(nl4xf1),"  |   ",round(nl4xf2,3)," | ",round(nl4xf3,3),"   | ",round(nl4b,3),"                                                       |")                                                                                                                                                 
        print("===========================================================================================================================================================================================================")
    elif pivo == r3x1 or pivo == r3x2:
        print("============================================================================================================================================================================================================")
        print("|                                                      NOVA TABELA                                                                                                                                         |")
        print("|                                                                                                                                                                                                          |")
        print("|    Z     |    X1      |    X2      |      XF1     |    XF2     |      XF3    |      B                                                                                                                    |")                                                                                                           
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|") 
        print("|    ",round(nlpz,3),"  |    ",round(nlpx1,3),"  |    ",round(nlpx2,3),"  |  ",   round(nlpxf1,3),"  |    ",round(nlpxf2,3),"  |    ",round(nlpxf3,3),"  |     ",round(nlpb,3),"                           |")
        print("|    ",0,"  |   ",round(nl3x1,3)," |   ",round(nl3x2,3)," |    ",round(nl3xf1,3)," |   ",round(nl3xf2,3)," | ",round(nl3xf3,3),"   | ",round(nl3b,3),"                                                     |")
        print("|    ",0,"  |   ",round(nl4x1,3)," |   ",round(nl4x2,3)," |   ",round(nl4xf1,3),"  |   ",round(nl4xf2,3)," | ",round(nl4xf3,3),"   | ",round(nl4b,3),"                                                     |")
        print("|    ",0,"  |   ",round(nlx1,3)," |   ",round(nlx2,3)," |   ",round(nlxf1),"  |   ",round(nlxf2,3)," | ",round(nlxf3,3),"   | ",round(nlb,3),"                                                             |")                                                                                                                                                 
        print("============================================================================================================================================================================================================")
    
    print("==========================================================================================================================")
    print("| Para montar as soluções: \n                                                                                            |")
    print("| VÁRIAVEIS BÁSICAS(VR): APENAS AS COLUNAS COM VALOR DE 0 E 1, A LINHA QUE TIVER 1 CORRESPONDE O VALOR DE B, EXEMLO:     |")
    print("| X1 | X2 | B                                                                                                            |")
    print("| 0 |  1 | 10                                                                                                            |")
    print("| 1 |  0 | 15                                                                                                            |")
    print("| VR: X1 = 15 e X2 = 10                                                                                                  |")
    print("| VÁRIAVEIS NÃO BÁSCIAS(VNB):COLUNAS COM VALORES QUE NÃO SEJAM 0 E 1, EXEMPLO:                                           |")
    print("| XF1 | XF2 | B                                                                                                          |")
    print("| 0.5 |  19 | 10                                                                                                         |")
    print("| 15 |  0.8 | 15                                                                                                         |")
    print("| (VNB:XF1 = 0 E XF2 0 (SEMPRE SERÃO 0)                                                                                  |")
    print("| A VÁRIAVEL Z SERÁ O CORRESPONDENTE, EXEMPLO:                                                                           |")
    print("| Z | B                                                                                                                  |")
    print("| 1 | 5                                                                                                                  |")
    print("| VÁRIAVEL Z:  Z = 5                                                                                                     |")
    print("==========================================================================================================================")

    print("\n CASO AINDA TENHA NÚMEROS NEGATIVOS, RECALCULE PARA TER O RESULTADO ÓTIMO \n")
    

    continuar = str(input("RECALCULAR?  "))
