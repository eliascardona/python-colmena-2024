class Artista:
    def __init__(self, nombre, album, cancion):
        self.__nombre = nombre
        self.__album = album
        self.__cancion = cancion

    # getters y setters
    @property
    def get_cancion(self):
        return self.__cancion

    @get_cancion.setter
    def set_cancion(self, nueva_cancion):
        self.__cancion = nueva_cancion

    @property
    def get_datos_artista(self):
        return [self.__nombre, self.__cancion, self.__album]