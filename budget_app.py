import math
class Category:
#El método __init__ debe aceptar un nombre para la categoría y crear una variable de instancia ledger que sea una lista vacía.
    def __init__(self, nombre):
        self.nombre = nombre
        self.ledger = []
#El método deposit debe aceptar un monto y una descripción (opcional) y agregar un objeto a la variable de instancia ledger con esos valores.
    def deposit(self, cantidad, descripcion=''):
#El método deposit debe crear un objeto específico en la variable de instancia ledger.
        self.ledger.append({'amount': cantidad, 'description': descripcion})
        return None
    def withdraw(self, cantidad, descripcion=''):
        #El método withdraw debe verificar que la cantidad a retirar no sea mayor que el balance actual de la categoría. Si es mayor, el método no debe realizar ningún cambio en el ledger y debe devolver False.
        if not self.check_funds(cantidad):
            return False
#El método withdraw debe crear un objeto específico en la variable de instancia ledger.
        self.ledger.append({'amount': -cantidad, 'description': descripcion})
#El método withdraw debe devolver True si la retirada se realizó.
        return True
#El método get_balance debe devolver el balance actual de la categoría (la suma de los montos en el ledger).
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
#El método check_funds debe verificar si hay fondos suficientes para realizar una retirada o transferencia. Si la cantidad a retirar o transferir es mayor que el balance actual, el método debe devolver False. De lo contrario, debe devolver True.
    def check_funds(self, cantidad):
        if self.get_balance() < cantidad:
            return False
        return True
#El método transfer debe verificar que la cantidad a transferir no sea mayor que el balance actual de la categoría. Si es mayor, el método no debe realizar ningún cambio en el ledger y debe devolver False.
    def transfer(self, cantidad, categoria_destino):
        if not self.check_funds(cantidad):
            return False
        self.withdraw(cantidad, f'Transfer to {categoria_destino.nombre}')
        categoria_destino.deposit(cantidad, f'Transfer from {self.nombre}')
        return True

    def __str__(self):
        lineas = []
        lineas.append(self.nombre.center(30, '*'))
        for item in self.ledger:
            descripcion = item['description'][:23]
            monto = item['amount']
            lineas.append(f"{descripcion:<23}{monto:>7.2f}")
        lineas.append(f'Total: {self.get_balance()}')
        return '\n'.join(lineas)

def create_spend_chart(categories):
    title = 'Percentage spent by category'
#Se obtienen los gastos de las categorias.
    gastos = []
    for categoria in categories:
        gasto = sum([item['amount'] for item in categoria.ledger if item['amount'] < 0])
        gastos.append(abs(gasto))
#Se obtiene los porcentajes 
    total = sum(gastos)
    porcentajes = [math.floor((gasto / total) * 100 / 10) * 10 for gasto in gastos]
#Se realizan las barras
    lineas = [title]
    for nivel in range(100, -1, -10):
        fila = f"{nivel:>3}|"
        for porcentaje in porcentajes:
            if porcentaje >= nivel:
                fila += ' o '  # espacio, o, espacio
            else:
                fila += '   '  # tres espacios
        fila += ' '  # espacio al final de cada fila
        lineas.append(fila)
    lineas.append('    ' + '-' * (3 * len(categories) + 1))

    max_len = max(len(categoria.nombre) for categoria in categories)
    for i in range(max_len):
        fila = '    '
        for categoria in categories:
            if len(categoria.nombre) > i:
                fila += ' ' + categoria.nombre[i] + ' '
            else:
                fila += '   '
        fila += ' '
        lineas.append(fila)
    return '\n'.join(lineas)


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print()
print(create_spend_chart([food, clothing]))