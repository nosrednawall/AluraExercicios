endereco = "Rua Gracho Cardoso, 92 – Ilha das Flores – SE – CEP: 49990-000"

import re

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
padrao = re.compile("[\d]{5}[-]{0,1}[\d]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)


texto_cpf = "Rafaela Brasil, CPF: 718.457.190-85"

padrao = re.compile("[\d]{3}[.]{0,1}[\d]{3}[.]{0,1}[\d]{3}[-]{0,1}[\d]{2}")
busca = padrao.search(texto_cpf)
if busca:
    cpf = busca.group()
    print(cpf)