class operaciones:
    nombre = ""
    cantCompradores = 0
    tarjetaCinecon = ""
    cantBoletos = 0
    res = 0
    res2 = 0

    def verificarMaximoBoletos(self, cantCompradores, cantBoletos):
        self.cantBoletos = cantBoletos
        self.cantCompradores = cantCompradores
        maximo = self.cantCompradores*7
        if (self.cantBoletos > maximo):
            return True
        else:
            return False

    def verificarDescuento(self, cantBoletos):
        self.cantBoletos = cantBoletos
        if (self.cantBoletos > 5):
            desc = (self.cantBoletos*12)*0.15
            self.res = (self.cantBoletos*12) - desc
            return self.res
        elif (self.cantBoletos <= 5 and self.cantBoletos >= 3):
            desc = (self.cantBoletos*12)*0.10
            self.res = (self.cantBoletos*12) - desc
            return self.res
        else:
            self.res = self.cantBoletos*12
            return self.res

    def verificarTarjeta(self, opcion, precio):
        print("OPCION", opcion)

        if (opcion == "si"):
            print("SI ES TARJETA")
            desc2 = precio*0.10
            self.res2 = precio-desc2
            print("PRECIO INICIAL", precio)
            print("PRECIO FINAL", self.res2)
            return self.res2
        else:
            self.res2 = precio
            print("PRECIO INICIAL", precio)
            print("PRECIO FINAL SIN DESCUENTO", self.res2)
            return self.res2
