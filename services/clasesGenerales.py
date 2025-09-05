from .models import UserType, Services

class clasesGenerales():

    def errorMessages(mensaje):
        match mensaje:
            case mensaje if mensaje == "UNIQUE constraint failed: auth_user.username":
                return "El nombre de usuario ya existe"
            case _:
                return 'Error desconocido'
            
    def createTipodeUsuario(lastUser, tipoUsuario):
        UserType.objects.create(usuario_principal=lastUser, tipo_usuario=tipoUsuario)

    def createServicio(serviceName):
        try:
            Services.objects.create(nombre_servicio=serviceName)
        except Exception as e:
            mensaje = ''
            print(mensaje)

    def updateServicio(idService, serviceName):
        try:
            Services.objects.filter(id=idService).update(nombre_servicio=serviceName)
        except Exception as e:
            mensaje = ''
            print(mensaje)

    def deleteServicio(idService):
        try:
            Services.objects.filter(id=idService).delete()
        except Exception as e:
            mensaje = ''
            print(mensaje)
