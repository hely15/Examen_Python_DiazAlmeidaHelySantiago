def VerF(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero   
        except Exception:
            print('Opcion invalida. Ingrese un valor valido: ')