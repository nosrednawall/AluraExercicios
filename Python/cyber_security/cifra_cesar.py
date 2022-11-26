class CifraCesar:
    def __init__(self, texto_puro:None , texto_cifrado:None):
        if texto_puro is None and texto_cifrado is None:
            raise Exception(f"Por favor informe ao menos um texto puro ou um texto cifrado")
            
        self._texto = texto_puro #if len(texto_puro) > abs(0)  descifra_texto(texto_puro) else texto_puro
        self._texto_cifrado = texto_cifrado #self._texto_cifrado if len(texto_cifrado) > abs(0) cifra_texto(self._texto_puro) else self._texto_cifrado
    
    @property
    def texto_puro(self):
        return self._texto_puro
    
    @property
    def texto_cifrado(self):
        return self._texto_cifrado
    
    def cifra_texto(texto):
        return texto
    
    def descifra_texto(texto):
        return texto
            
        