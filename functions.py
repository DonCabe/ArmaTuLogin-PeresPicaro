def logUser(userDB):
    bandera = True
    while bandera == True:
        user = str(input("Usuario: "))
        userPass = userDB.get(user)
        # print(user, userPass) # Usar si es necesario para ver la contraseña del usuario ingresado
        if userPass == None:
            print("El usuario no existe.")
        else:
            for i in range(3):
                password = str(input("Contraseña: "))
                if userDB[user] != password:
                    print(f"Contraseña invalida. Quedan {2-i} intentos.")
                else:
                    print("Ha ingresado exitosamente!")
                    bandera = False
                    i = 2
                    return user
    

def addUser(userDB):
    while True:
        user = str(input("Ingrese un nuevo usuario: "))
        if userDB.get(user) != None:
            print("El usuario ya existe.")
        else:
            bandera = True
            while bandera:
                password = str(input("Ingrese una nueva contraseña: "))
                if len(password) < 4:
                    print("La contraseña es debe tener al menos 4 caracteres")
                else:
                    userDB[user] = password
                    print("Usuario creado exitosamente!")
                    bandera = False
            break
        break


def showUsers(userDB):
    print("Los usuarios existentes son: ")
    for key in userDB.keys():
        print(key)


def showUserPass(userDB):
        print("Los usuarios y contraseñas existentes son: ")
        for key in userDB.keys():
            print(key,"-",userDB[key])


def delUser(userDB):
    user = str(input("Ingrese el usuario a eliminar: "))
    if userDB.get(user) == None:
        print("El usuario no existe.")
    else:
        if user == "admin":
            print("No puede eliminar este usuario!")
        else:
            del userDB[user]
            print("Usuario eliminado exitosamente!")