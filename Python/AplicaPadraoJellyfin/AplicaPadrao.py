import os
import math

class ArquivoMultimidia:
    def __init__(self, nome_arquivo, extensao, caminho, ano, nome_serie, temporada):
        self._nome_arquivo = nome_arquivo
        self._extensao = extensao
        self._caminho = caminho
        #self._novo_nome = novo_nome
        self._ano = ano
        self._nome_serie = nome_serie
        self._temporada = self.__monta_temporada(temporada)
        self._numero_episodio = self.__monta_numero_episodio(nome_arquivo)

    def __monta_numero_episodio(self ,nome_arquivo):
        pass

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
        return f"Episode S{self.temporada}E{self.numero_episodio}.{self.extensao}"

    @property
    def temporada(self):
        return self._temporada

    @property
    def numero_episodio(self):
        return self._numero_episodio

    @property
    def extensao(self):
        return self._extensao

# primeiro pegamos os nomes dos arquivos
files = [next(os.walk(r"/home/anderson/Vídeos/Mob Pyscho 100 (2016)/mob_s1"))]
print(files)