import subprocess

def exec_minizinc():
    # Ruta del archivo .mzn y .dzn
    archivo_mzn = 'model-1.mzn'
    archivo_dzn = 'DatosPUEnTe.dzn'

    # Comando para ejecutar en la consola
    comando = f"minizinc {archivo_mzn}"

    # Ejecutar el comando en la consola
    subprocess.run(comando, shell=True)
