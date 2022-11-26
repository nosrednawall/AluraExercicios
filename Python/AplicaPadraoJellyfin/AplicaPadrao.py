import os
import re
import math
import shutil
import glob


class ArquivoMultimidia:
    def __init__(self, nome_arquivo, caminho, ano, nome_serie, temporada):
        self._nome_arquivo = nome_arquivo
        self._extensao = self.__monta_extensao(nome_arquivo)
        self._caminho = caminho
        self._ano = ano
        self._nome_serie = nome_serie
        self._temporada = self.__monta_temporada(temporada)
        self._numero_episodio = self.__monta_numero_episodio(nome_arquivo, nome_serie)
        self._novo_nome = self.__monta_novo_nome_arquivo()

    def __monta_extensao(self, nome_arquivo):
        padrao = re.compile(r"\.[^.]+$")
        busca = padrao.search(nome_arquivo)
        return busca.group()

    def __monta_numero_episodio(self, nome_arquivo, nome_serie):
        nome_arquivo_sem_nome_serie = nome_arquivo.replace(nome_serie, "")
        padrao = re.compile(r"([\d]?[\d][\d]){1}([^\d.p])?")
        busca = padrao.search(nome_arquivo_sem_nome_serie)  # Match
        if busca:
            numero_episodio = busca.group()
            return numero_episodio.strip()
        else:
            return "Some Special"

    def __monta_temporada(self, numero):
        numero = abs(int(numero))
        resultado = (1 if numero == 0 else math.floor(math.log10(numero)) + 1)
        if resultado == 1:
            return "00"+str(numero)
        elif resultado == 2:
            return "0"+str(numero)
        else:
            return str(numero)

    '''
    Shows
    ├── Series (2010)
    │   ├── Season 00
    │   │   ├── Some Special.mkv
    │   │   ├── Episode S00E01.mkv
    │   │   └── Episode S00E02.mkv
    '''
    def __monta_novo_nome_arquivo(self):
        if "Some Special" in self.numero_episodio:
            return f"{self.numero_episodio}{self.extensao}"
        else:
            return f"Episode S{self.temporada}E{self.numero_episodio}{self.extensao}"

    @property
    def temporada(self):
        return self._temporada

    @property
    def numero_episodio(self):
        return self._numero_episodio

    @property
    def extensao(self):
        return self._extensao

    @property
    def novo_nome(self):
        return self._novo_nome

    @property
    def original(self):
        return f"{self._caminho}/{self._nome_arquivo}"

    @property
    def renomeado(self):
        return f"{self._caminho}/{self._novo_nome}"

def renomear():
    # specify your path of directory
    path = r"/home/anderson/Vídeos/Mob Pyscho 100 (2016)/mob_s3/"
    ano = "2016"
    nome_serie = "Mob Psycho 100"
    temporada = "003"

    # call listdir() method
    # path is a directory of which you want to list
    directories = os.listdir(path)

    # This would print all the files and directories
    for file in directories:
        print(file)

        padrao = re.compile(r"\.[^.]+$")
        possui_extensao = padrao.search(file)
        if possui_extensao:
            arquivo = ArquivoMultimidia(nome_arquivo=file,
                                        nome_serie=nome_serie,
                                        caminho=path,
                                        ano=ano,
                                        temporada=temporada)
            print(arquivo.novo_nome)
            shutil.move(arquivo.original, arquivo.renomeado)


def mover_arquivo_subpastas():
    path = r"/home/anderson/Vídeos/Mob Pyscho 100 (2016)/mob_s3/"
    files = glob.glob(path + '/**/*.mkv', recursive=True)
    for file in files:
        padrao = re.compile(r"[^\\/]+?(?=$)")
        possui_nome_arquivo = padrao.search(file)
        if possui_nome_arquivo:
            nome_arquivo = possui_nome_arquivo.group()

            source = file
            destination = f"{path}{nome_arquivo}"

            shutil.move(source, destination)


mover_arquivo_subpastas()