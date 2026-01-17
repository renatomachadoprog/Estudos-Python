peso = int(input('insira seu peso: '))
altura = int(input('insira sua altura:'))
idade = int(input("insira sua idade: "))

def tmb(x, y, z):
  tmb= (10*x)+(6.25*y) - (5*z)+5
  return round(tmb)

def gastocalorico(x,y,z):
  gastocalorico = tmb(x,y,z) * 1.55
  return round(gastocalorico)

def carboidratos(x,y,z):
  taxametabolica = gastocalorico(x,y,z)
  carboidratos = taxametabolica - (taxametabolica*0.65)
  return round(carboidratos)

def proteinas(x,y,z):
  taxametabolica = gastocalorico(x,y,z)
  proteina = taxametabolica - (taxametabolica*0.7)
  return round(proteina)

def gorduras(x,y,z):
  taxametabolica = gastocalorico(x,y,z)
  gorduras = taxametabolica-(taxametabolica*0.65)
  return round(gorduras)

def manterpeso(x,y,z):
  taxametabolica = tmb(x,y,z)
  gastocaloricoT = gastocalorico(x,y,z)
  valorproteinas = proteinas(x,y,z)
  valorgorduras = gorduras(x,y,z)
  valorcarboidratos = carboidratos(x,y,z)
  return gastocaloricoT, valorproteinas, valorgorduras, valorcarboidratos

    # pre condições da função : X, Y e Z
    # pós condições da função : tmb(), gastocalorico(), proteinas(), gorduras(), carboidratos()

gastocaloricoT, valorproteinas, valorgorduras, valorcarboidratos = manterpeso(peso,altura,idade)
print(f"com um gasto de {gastocaloricoT}, voce precisa de {valorproteinas} gramas de proteinas, {valorgorduras} gramas de gordura e {valorcarboidratos} gramas de carboidrato para manter seu peso atual")


# é um teste de versionamento de Git

