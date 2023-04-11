class Boleta:
    rut_personas = []
    def __init__(self,rut,fecha,descuento,precio_neto):
        Boleta.rut_personas.append(rut)
        self._rut = rut
        self._fecha = fecha
        self._descuento = descuento
        self._precio_neto = int(precio_neto)
        self.calcularTotal()
    
    def calcularTotal(self):
        precioMasIva = int(self._precio_neto)*0.19
        total = int(self._precio_neto) + int(precioMasIva) 
        precioDescuento = int(total)*float(self._descuento)
        totalFinal = total-precioDescuento
        self._total = totalFinal
    def precioMasIva(self):
        return self._precio_neto+(self._precio_neto*0.19)
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self,rut):
        self._rut = rut

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self,descuento):
        self._descuento = descuento
    
    @property
    def precio_neto(self):
        return self._precio_neto
    
    @precio_neto.setter
    def precio_neto(self,precio_neto):
        self._precio_neto = precio_neto

    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,total):
        self._total = total
    
    @classmethod
    def verificarDescuentos(cls,rutCliente):
        try:
            if cls.rut_personas[0] == rutCliente:
                print("Descuento por Dos mascotas".center(50,"-"))
                return float(0.50)
            else: 
                return 0
        except Exception:
            return 0
        
    def string(self):
        return f"{self._rut},{self._fecha},{self._descuento},{self._precio_neto},{int(self._total)}"
    
    def __str__(self):
        return f"""Rut: {self._rut}
        Fecha Emitida: {self._fecha}
        Descuento: {self._descuento}
        Precio Neto: {self._precio_neto}
        Precio Mas Iva: {int(self.precioMasIva())}
        Total Mas Descuentos: {int(self._total)}"""

if __name__ == "__main__":
    boleta1 = Boleta("1234","2023",0.25,50000)
    print(boleta1)