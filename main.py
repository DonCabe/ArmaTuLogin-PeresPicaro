from functions import logUser, addUser, showUsers, showUserPass, delUser
userPass_db = {"admin":"1234", "eperesp":"1234"}

userLogged = logUser(userPass_db)
opMenu = ""

while opMenu != 0:
    try:
        print(f'''Menú - usuario: {userLogged} 
    1 - Cambiar de Usuario
    2 - Registrar nuevo Usuario
    3 - Vista Usuarios
    4 - Vista Usuarios - Contraseña
    5 - Eliminar Usuario''')
        print("    0 - Salir")
        opMenu = int(input("Opción: "))
        print(opMenu)

        if opMenu < 0 or opMenu > 5:
            print("Opción invalida. Vuelva a intentar.")
        elif opMenu == 1:
            userLogged = logUser(userPass_db)
        elif opMenu == 2:
            addUser(userPass_db)
        elif opMenu == 3:
            showUsers(userPass_db)
        elif opMenu == 4:
            if userLogged == "admin":
                showUserPass(userPass_db)
            else:
                print("No tiene los permisos para ver las contraseñas de los usuarios.")
                print("(Ingrese con la cuenta 'admin')")
        elif opMenu == 5:
            if userLogged == "admin":
                delUser(userPass_db)
            else:
                print("No tiene los permisos para ver las contraseñas de los usuarios.")
                print("(Ingrese con la cuenta 'admin')")
        elif opMenu == 0:
            break
    except ValueError:
        print("Opción invalida. Vuelva a intentar.")