import subprocess


def exec_minizinc():
    # Comando para ejecutar en la consola
    comando = f"minizinc --solver COIN-BC ../PUEnTe.mzn ../DatosPUEnTe.dzn > solution.txt"
    # Ejecutar el comando en la consola
    subprocess.run(comando, shell=True)
    with open('solution.txt', 'r') as archivo:
        lineas = archivo.readlines()

    return lineas
   
    
