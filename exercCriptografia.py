def crip(texto,chave): #pode usar numeros tbm
    aq = []
    for cont in range (len(texto)):
        if texto[cont] == (chr(32)) or (chr(97)<=texto[cont]<=chr(122)):
            if texto[cont] == " ":
                aq.append(" ")
            else:
                crip = ord(texto[cont])
                if chr(crip+chave) <= chr(122):
                    crip = chr(crip + chave)
                    aq.append(crip)
                elif chr(crip+chave) > chr(122):
                    numero = (crip + chave)
                    numero = numero - 122
                    crip = chr(96 + numero)
                    aq.append(crip)
        if chr(48)<=texto[cont]<=chr(57):
            crip = ord(texto[cont])
            if chr(crip+chave) <= chr(57):
                crip = chr(crip+chave)
                aq.append(crip)
            elif chr(crip+chave) > chr(57):
                numero = (crip+chave)
                numero = numero - 57
                crip = chr(47 + numero)
                aq.append(crip)
    aq = "".join(aq)
    return(aq)

def quebraCrip(texto):
    for a in range(0,26):
        b = crip(texto,a)
        print(f"{a+1}- {b}")

def desCrip(texto,chave):
    aq = []
    for cont in range (len(texto)):
        if texto[cont] == (chr(32)) or (chr(97)<=texto[cont]<=chr(122)):
            if texto[cont] == " ":
                aq.append(" ")
            else:
                crip = ord(texto[cont])
                if chr(crip-chave) >= chr(97):
                    crip = chr(crip - chave)
                    aq.append(crip)
                elif chr(crip-chave) < chr(97):
                    numero = (crip - chave)
                    numero = 97 - numero
                    crip = chr(123 - numero)
                    aq.append(crip)
        if chr(48)<=texto[cont]<=chr(57):
            crip = ord(texto[cont])
            if chr(crip-chave) >= chr(48):
                crip = chr(crip-chave)
                aq.append(crip)
            elif chr(crip-chave) < chr(48):
                numero = (crip-chave)
                numero = 48 - numero
                crip = chr(58 - numero)
                aq.append(crip)
    aq = "".join(aq)
    return(aq)

textoCrip= input("Digite o texto que deseja criptografar: ")
chaveCrip= int(input("Digite a chave da  criptografia: "))
a = crip(textoCrip,chaveCrip)
print(a)

textoDescrip= input("Digite o texto que deseja Descriptografar: ")
chaveDescrip= int(input("Digite a chave da  Descriptografia: "))
b = desCrip(textoDescrip,chaveDescrip)
print(b)

textoQuebra= input("Digite o texto que deseja forçar a Descriptografia: ")
quebraCrip(textoQuebra)

