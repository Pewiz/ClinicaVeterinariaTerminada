import csv


class GestionArchivo:
    def __init__(self):
        pass
    
    @classmethod
    def seleccionarTodo(cls,nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf8") as archivo:
            lector = csv.reader(archivo,delimiter=",")
            next(lector,None)
            listaDelistas = []
            for lista in lector:
                try:
                    listaDelistas.append(lista)
                except Exception as e:
                    return listaDelistas
            
            return listaDelistas

    @classmethod
    def seleccionar(cls,nombre_archivo,objeto):
        with open(nombre_archivo,"r",encoding="utf8") as archivo:
            lector = csv.reader(archivo,delimiter=",")
            next(lector,None)
            listaDelistas = []
            for lista in lector:
                    try:                  
                        rut = lista[0]                                
                        if rut == objeto.get_rut():                       
                            listaDelistas.append(lista)   
                    except Exception as e:
                        return listaDelistas
            return listaDelistas
                

    @classmethod
    def insertar(cls,nombre_archivo,objeto):
        with open(nombre_archivo,"a",newline="") as archivo:
            lista = objeto.string().split(",")
            escritor = csv.writer(archivo,delimiter=",") 
            escritor.writerow(lista)

    @classmethod
    def modificar(cls,nombre_archivo,objeto):
        with open(nombre_archivo,"r",encoding="utf8") as archivo:
            pass

    @classmethod
    def eliminar(cls,nombre_archivo,i):       
        with open(nombre_archivo,'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for number,line in enumerate(lines):
                if number not in [i]:
                    file.write(line)
    
    @classmethod
    def identificarLinea(cls,nombre_archivo,id):
        with open(nombre_archivo) as archivo:
            lector = csv.reader(archivo,delimiter=",")
            lineas = []
            i = 0
            for lista in lector:
                if len(lista) != 0:
                    ids = format(lista[1])
                    if id == ids:
                        lineas.append(i)
                i += 1
        return lineas

            

if __name__ == "__main__":
    #cliente1 = Cliente(rut="21454138-6")
    
    #GestionArchivo.seleccionar("clientes.csv",cliente1)
    
    #cliente2 = Cliente("Diego Fernando","Jaune","Casa roja","Masculino","NOSE","No me acuerdo","diegojaune@gmail.com","123123","casa roja")
    #GestionArchivo.insertar("clientes.csv",cliente2)
    pass
