class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, cadena):
        
        if not isinstance(cadena, str):
            return f'{cadena} el valor solo deben de ser letras.'
        
        codigos = []
        for letra in cadena:
            codigos.append(ord(letra))
        
        return sum(codigos)
    
    def add(self, clave, valor):

        if not isinstance(clave, (str, int, tuple)):
            return f'{clave} debe ser una cadena, entero o tupla.'
        
        valor_hash = self.hash(clave)
        
        if valor_hash in self.collection:
            self.collection[valor_hash].update({clave: valor})
        else:
            self.collection[valor_hash] = {clave: valor}
    
    def remove(self, clave):

        valor_hash = self.hash(clave)

        if valor_hash in self.collection:
            return self.collection[valor_hash].pop(clave, None)
    
    def lookup(self, clave):

        valor_hash = self.hash(clave)

        diccionario_hash = self.collection.get(valor_hash, {})

        return diccionario_hash.get(clave, None)