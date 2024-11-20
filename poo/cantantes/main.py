from cantante import Artista

madonna = Artista("madonna", "celebration", "music")


madonna.set_cancion('vouge')
print(f"Cancion desde setter\t \"{madonna.get_cancion}\".")




# print(f"DATOS DEL ARTISTA\t /{madonna.get_datos_artista[0]} / {madonna.get_datos_artista[1]} / {madonna.get_datos_artista[2]}/ ")