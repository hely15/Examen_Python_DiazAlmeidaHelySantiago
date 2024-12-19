import json
import os
import modulos.funcionVerf as llamarverF


def VerF(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero   
        except Exception:
            print('Opcion invalida. Ingrese un valor valido: ')

def guardarArchivo(Diccionario,archivo):
    with open (f"./databas/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    archivo_path = f"./databas/{archivo}.json"
    
    if not os.path.exists(archivo_path):
        print(f"El archivo {archivo_path} no existe.")
        return None  # Retorna None si no existe el archivo
    
    with open(archivo_path, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario


usuariosData = abrirArchivo('usuarios')


def aggClientes(usuariosData: dict): 
    nombres = input('Ingrese el nombre del cliente: ').capitalize()
    numeroDocumento = VerF('Ingrese el número de identificación de cliente: ')
    direccion = input('Ingrese la dirección de recidencia del cliente: ').capitalize()
    telefono = VerF('Ingrese el numero de telefono del cliente: ')
    
    usuariosData[numeroDocumento] = {
        'nombre': nombres,
        'numeroDocumento': numeroDocumento,
        'direccion': direccion,
        'telefono': telefono,
        'categoria': {
            "nuevo":True,
            "regular": False,
            "leal": False,
            "platinium": False,
            "vip": False,
        },
         'serviciosDelCliente': {
            'plan1N': False,
            'plan2N': False,
            'plan3N': False,
            'plan1R': False,
            'plan2R': False,
            'plan3R': False,
            'plan1L': False,
            'plan2L': False,
            'plan3L': False,
            'plan1P': False,
            'plan2P': False,
            'plan3P': False,
            'plan1V': False,
            'plan2V': False,
            'plan3V': False,
        },
        "pqr": {
            
        }

    }

    guardarArchivo(usuariosData, "usuarios")
    print(f"Usuario agregado con éxito su ID numero de documento {numeroDocumento}")

def verInfClientes(usuariosData: dict):
    while True:
        numeroDocumento = str(input('Ingrese el número de identificación de cliente: '))
        if numeroDocumento in usuariosData:
            nombreU = usuariosData[numeroDocumento]["nombre"]
            direccionU = usuariosData[numeroDocumento]["numeroDocumento"]
            telefonoU = usuariosData[numeroDocumento]["telefono"]

            iplan1N = usuariosData["planes"][1]
            iplan2N = usuariosData ["planes"][3]
            iplan3N = usuariosData ["planes"][5]
            iplan1L = usuariosData ["planes"][7]
            iplan2L = usuariosData ["planes"][9]
            iplan3L = usuariosData ["planes"][11]
            iplan1P = usuariosData ["planes"][13]
            iplan2P = usuariosData ["planes"][15]
            iplan3P = usuariosData ["planes"][17]
            iplan1V = usuariosData ["planes"][19]
            iplan2V = usuariosData ["planes"][21]
            iplan3V = usuariosData ["planes"][23]


            if usuariosData[numeroDocumento]["categoria"]["nuevo"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1N"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Nuevo.')
                    print(f'El plan actual del cliente es Plan1N')
                    print(f'{iplan1N}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2N"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Nuevo.')
                    print(f'El plan actual del cliente es Plan1N')
                    print(f'{iplan2N}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3N"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Nuevo.')
                    print(f'El plan actual del cliente es Plan1N')
                    print(f'{iplan3N}')
                

            if usuariosData[numeroDocumento]["categoria"]["leal"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Leal.')
                    print(f'El plan actual del cliente es {iplan1L}')
                    print(f'{iplan1L}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Leal.')
                    print(f'El plan actual del cliente es: {iplan2L} ')
                    print(f'{iplan2L}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Leal.')
                    print(f'El plan actual del cliente es: {iplan3L}')
                    print(f'{iplan3L}')

            if usuariosData[numeroDocumento]["categoria"]["platinium"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1P"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Platinium.')
                    print(f'El plan actual del cliente es: {iplan1P}')
                    print(f'{iplan1P}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2P"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Platinium.')
                    print(f'El plan actual del cliente es: {iplan1P} ')
                    print(f'{iplan2P}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3P"] == True:        
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Platinium.')
                    print(f'El plan actual del cliente es: {iplan1P} ')
                    print(f'{iplan3P}')
                

            if usuariosData[numeroDocumento]["categoria"]["vip"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Vip.')
                    print(f'El plan actual del cliente es: {iplan1V} ')
                    print(f'{iplan1V}')
                
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Vip.')
                    print(f'El plan actual del cliente es: {iplan2V} ')
                    print(f'{iplan2V}')
                
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'La direccion del cliente es: {direccionU}.')
                    print(f'El numero telefonico del cliente es: {telefonoU}.')
                    print(f'La categortia del cliente es: Vip.')
                    print(f'El plan actual del cliente es: {iplan3V} ')
                    print(f'{iplan3V}')
        else:
            print('Usuario no encontrado Intente denuevo.')
            return verInfClientes
        
def veriFicarUs(usuariosData: dict):
    while True:
        numeroDocumento = str(input('Ingrese el número de identificación: '))
        numeroDocUs = llamarverF.VerF('<:>')
        if numeroDocUs in usuariosData:
            nombre = usuariosData[numeroDocUs]["nombre"]
            print(f'Bienvenido {nombre}')
        
def verInfUsuario(usuariosData: dict):
    while True:
        numeroDocumento = str(input('Ingrese el número de identificación: '))
        if numeroDocumento in usuariosData:
            nombreU = usuariosData[numeroDocumento]["nombre"]
            direccionU = usuariosData[numeroDocumento]["direccion"]
            telefonoU = usuariosData[numeroDocumento]["telefono"]

            iplan1N = usuariosData["planes"][1]
            iplan2N = usuariosData ["planes"][3]
            iplan3N = usuariosData ["planes"][5]
            iplan1L = usuariosData ["planes"][7]
            iplan2L = usuariosData ["planes"][9]
            iplan3L = usuariosData ["planes"][11]
            iplan1P = usuariosData ["planes"][13]
            iplan2P = usuariosData ["planes"][15]
            iplan3P = usuariosData ["planes"][17]
            iplan1V = usuariosData ["planes"][19]
            iplan2V = usuariosData ["planes"][21]
            iplan3V = usuariosData ["planes"][23]


            if usuariosData[numeroDocumento]["categoria"]["nuevo"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1N"] == True:
                    print(f'Su nombre es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Nuevo.')
                    print(f'Su Plan es Plan1N')
                    print(f'{iplan1N}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2N"] == True:
                    print(f'Su nombre es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'LSu categortia es: Nuevo.')
                    print(f'Su Plan es Plan1N')
                    print(f'{iplan2N}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3N"] == True:
                    print(f'Su nombre es: {nombreU}.')
                    print(f'Su Direccion es:{direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Nuevo.')
                    print(f'Su Plan es Plan1N')
                    print(f'{iplan3N}')
                

            if usuariosData[numeroDocumento]["categoria"]["leal"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Leal.')
                    print(f'Su Plan es {iplan1L}')
                    print(f'{iplan1L}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortiaes: Leal.')
                    print(f'Su Plan es: {iplan2L} ')
                    print(f'{iplan2L}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3L"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Leal.')
                    print(f'Su Plan es: {iplan3L}')
                    print(f'{iplan3L}')

            if usuariosData[numeroDocumento]["categoria"]["platinium"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1P"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Platinium.')
                    print(f'Su Plan es: {iplan1P}')
                    print(f'{iplan1P}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2P"] == True:
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Platinium.')
                    print(f'Su Plan es: {iplan1P} ')
                    print(f'{iplan2P}')
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3P"] == True:        
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Platinium.')
                    print(f'Su Plan es: {iplan1P} ')
                    print(f'{iplan3P}')
                

            if usuariosData[numeroDocumento]["categoria"]["vip"] == True:
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan1V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Vip.')
                    print(f'Su Plan es: {iplan1V} ')
                    print(f'{iplan1V}')
                
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan2V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Vip.')
                    print(f'Su Plan es: {iplan2V} ')
                    print(f'{iplan2V}')
                
                if usuariosData[numeroDocumento]["serviciosDelCliente"]["plan3V"] == True: 
                    print(f'El nombre del cliente es: {nombreU}.')
                    print(f'Su Direccion es: {direccionU}.')
                    print(f'Su numero es: {telefonoU}.')
                    print(f'Su categortia es: Vip.')
                    print(f'Su Plan es: {iplan3V} ')
                    print(f'{iplan3V}')
        else:
            print('Usuario no encontrado Intente denuevo.')
            return verInfClientes


def aggPQR(usuariosData: dict):
    id = int(input('Ingrese su documento:'))
    tipo = input('Ingrese el tipo de PQR queja, reclamo, etc:')
    razon = input('Ingrese la razon de su Queja o reclamo: ')
    explicacion = input('Explique sus peticiones o quejas: ')
    numeroDePQR = int(input('Ingrese el numero con el cual se identificara su PQR: '))

    usuariosData[id]["pqr"][numeroDePQR] = {
        "tipo": tipo,
        "razon": razon,
        "explicacion": explicacion,
        "estado": {
            "recibida": True,
            "enproceso": False,
            "aprobada": False
        }
    }
guardarArchivo(usuariosData, "usuarios")
    