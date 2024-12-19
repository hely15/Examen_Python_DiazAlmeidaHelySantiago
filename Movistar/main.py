import modulos.menus as menus
import modulos.funcionVerf as llamarverF
import modulos.admin as funAdmin




if __name__ == '__main__':
    while(True):
        print(menus.menuPrincipal)
        opMenuPrincipal = llamarverF.VerF('<:>')
        match opMenuPrincipal:
            case 1:
                print(menus.menuCliente1)
                opMenuCliente = llamarverF.VerF('<:>')
                match opMenuCliente:
                    case 1:
                        funAdmin.verInfUsuario(funAdmin.usuariosData)
                    case 2:
                        funAdmin.aggPQR(funAdmin.usuariosData)
                    case 3:
                        pass
                    case _:
                        break
            case 2: 
                print(menus.menuAdmin1)
                opMenuAdmin1 = llamarverF.VerF('<:>')
                match opMenuAdmin1:
                    case 1:
                        funAdmin.aggClientes(funAdmin.usuariosData)
                    case 2:
                        funAdmin.verInfClientes(funAdmin.usuariosData)
                    case 3:
                        pass
                    case 4:
                        pass
                    case _:
                        llamarverF.VerF('<:>')
            case 3:
                break
            case _: 
                llamarverF.VerF('<:>')
