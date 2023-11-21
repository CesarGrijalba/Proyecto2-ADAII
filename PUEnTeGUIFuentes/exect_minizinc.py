import subprocess
import platform


def exec_minizinc():
    sistema = platform.system()

    # Comando para ejecutar en la consola
    subprocess.run('cd /PUEnTeGUIFuentes', shell=True)
    comando = f"minizinc --solver COIN-BC ../PUEnTe.mzn ../DatosPUEnTe.dzn > solution.txt"
    # Ejecutar el comando en la consola
    subprocess.run(comando, shell=True)
    with open('solution.txt', 'r') as archivo:
        lineas = archivo.readlines()
    
    if sistema=='Windows':
        subprocess.run('del solution.txt', shell=True)
    else:
        subprocess.run('rm solution.txt', shell=True)
    
    return lineas
   
    
