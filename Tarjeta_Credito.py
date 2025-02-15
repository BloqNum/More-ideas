historial=[]
class tarjetaC:
    def __init__(self, dueño, num, femision, vto, lcredito, bancoE, total):
        self.dueño=dueño
        self.num=num
        self.femision=femision
        self.vto=vto
        self.lcredito=lcredito
        self.total=total
        self.bancoE=bancoE
    def caracteristicas(self):
        print(f"Dueño: {self.dueño}\nNumero de tarjeta: {self.num}\n"
              f"Vencimiento: {self.vto}\nLimite de credito: ${self.lcredito}\n"
              f"Credito gastado: ${self.total}\nBanco Emisor: {self.bancoE}\n")
        input("Presione enter para regresar al menu")
        return
    def seehistorial(self):
        for i in historial:
            for w in i:
                print(w)
            print()
        input("Presione enter para regresar al menu")
        return
    def pagarT(self):
        pagar=int(input(f"Su saldo gastado actual es: {self.total}"
                        f"\n Ingrese el monto a pagar:"))
        self.total=self.total-pagar
        print(f"\nSu pago se ha realizado con exito, ahora su saldo gastado actual es {self.total}\n")
        input("Presione enter para regresar al menu")
        return
    def pagarX(self):
        pago=int(input("\nColoque el monto a pagar:"))
        articulo=input("Especifique el articulo a pagar:")
        fecha=input("Ingrese la fecha con el formato dd/mm/aa:")
        if pago>self.lcredito:
            print("\nEl pago no se puede realizar porque excede el limite de credito")
            input("Presione enter para regresar al menu")
            return
        if self.total>self.lcredito:
            print("\nEl pago no se puede realizar porque has alcanzado el limite de la tarjeta")
            input("Presione enter para regresar al menu")
            return
        else:
            self.total+=pago
            hoy=[]
            hoy.append(fecha)
            hoy.append(articulo)
            hoy.append(pago)
            historial.append(hoy)
            print(f"\nEl pago por el articulo {articulo} ha sido realizado correctamente")
            input("Presione enter para regresar al menu")
            return
try:
    dueño=input("Ingrese el nombre del titular:")
    num=int(input("Ingrese el numero de tarjeta:"))
    emision=input("Ingrese la fecha de emision con el formato dd/mm/aa:")
    vto=input("Ingrese la fecha de vto con el formato dd/mm/aa:")
    credito=int(input("Ingrese el limite de credito:"))
    banco=input("Ingrese el Banco emisor de la tarjeta:")
    total=0
    tarjet=tarjetaC(dueño,num,emision,vto,credito,banco,total)
    while 0!=1:
        print("------------MENU------------")
        eleccion=int(input("\nIngrese 1 para ver las caracteristicas de su tarjeta"
                           "\nIngrese 2 para realizar un pago"
                           "\nIngrese 3 para ver el historial de compra"
                           "\nIngrese 4 para pagar su tarjeta"
                           "\nIngrese 5 para salir\n"))
        if eleccion==1:
            tarjet.caracteristicas()
        if eleccion==2:
            tarjet.pagarX()
        if eleccion==3:
            tarjet.seehistorial()
        if eleccion==4:
            tarjet.pagarT()
        if eleccion==5:
            break
except Exception as mistake:
    print("Hubo un problema con la ejecucion del programa\n")
    eleccion=int(input("Ingrese 1 para salir sin mas o 2 para ver la especificacion del problema\n"))
    if eleccion==2:
        print(mistake)




