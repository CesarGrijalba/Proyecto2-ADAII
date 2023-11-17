import tkinter as tk
from tkinter import filedialog
from readFile import open_file

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto II - ADA II")

# Creando campos de texto por cada variable

campo_J = tk.Entry(ventana)
campo_K = tk.Entry(ventana)
campo_Ej = tk.Entry(ventana)
campo_Aj = tk.Entry(ventana)
campo_Gj = tk.Entry(ventana)
campo_Fj = tk.Entry(ventana)
campo_Vj = tk.Entry(ventana)
campo_Pjinferior = tk.Entry(ventana)
campo_Pjsuperior = tk.Entry(ventana)
campo_Supj = tk.Entry(ventana)
campo_Infj = tk.Entry(ventana)
campo_Pj_inicial = tk.Entry(ventana)
campo_Dk = tk.Entry(ventana)
campo_Rk = tk.Entry(ventana)

#Funcion para convertor un conjutno de string a nuemros
#
def convert_to_float(data_set):
    numbers_float = [float(x) for x in data_set]
    return numbers_float

# Funcion para agregar las variables a los campos
def agregar_etiquetas():
    data = open_file()
    J, K, Ej, Aj, Gj, Fj, Vj, Pj_inferior, Pj_superior, Supj, Infj, Pj_inicial, Dk, Rk = data
    campo_J.insert(0, J)
    campo_K.insert(0, K)
    campo_Ej.insert(0, Ej)
    campo_Aj.insert(0, Aj)
    campo_Gj.insert(0, Gj)
    campo_Fj.insert(0, Fj)
    campo_Vj.insert(0, Vj)
    campo_Pjinferior.insert(0, Pj_inferior)
    campo_Pjsuperior.insert(0, Pj_superior)
    campo_Supj.insert(0, Supj)
    campo_Infj.insert(0, Infj)
    campo_Pj_inicial.insert(0, Pj_inicial)
    campo_Dk.insert(0, Dk)
    campo_Rk.insert(0, Rk)

#  Escribir archivo .dzn
    output_file = 'DatosPUEnTe.dzn'

    with open(output_file, 'w') as file:
        J = J.strip()
        K = K.strip()
        Ej = convert_to_float(Ej)
        Aj = convert_to_float(Aj)
        Gj = convert_to_float(Gj)
        Fj = convert_to_float(Fj)
        Vj = convert_to_float(Vj)
        Pj_inferior = convert_to_float(Pj_inferior)
        Pj_superior = convert_to_float(Pj_superior)
        Supj = convert_to_float(Supj)
        Infj = convert_to_float(Infj)
        Pj_inicial = convert_to_float(Pj_inicial)
        Dk = convert_to_float(Dk)
        Rk = convert_to_float(Rk)
        file.write(f'int: J = {J};\n')
        file.write(f'int: K = {K};\n')
        file.write(f'set of float: Ej = {Ej};\n')
        file.write(f'set of float: Aj = {Aj};\n')
        file.write(f'set of float: Gj = {Gj};\n')
        file.write(f'set of float: Fj = {Fj};\n')
        file.write(f'set of float: Vj = {Vj};\n')
        file.write(f'set of float: Pj_Inferior = {Pj_inferior};\n')
        file.write(f'set of float: Pj_Superior = {Pj_superior};\n')
        file.write(f'set of float: Supj = {Supj};\n')
        file.write(f'set of float: Infj = {Infj};\n')
        file.write(f'set of float: Pj_inicial = {Pj_inicial};\n')
        file.write(f'set of float: Dk = {Dk};\n')
        file.write(f'set of float: Rk = {Rk};\n')
        




# Funcion para escribir archivo
'''
def write_file():
    file = open ("DatosPUEnTe.dzn", "w")
    file.write("J="+campo_J.get())
    file.write("J="+campo_K.get())
    file.close()
'''

# Crear el botón
boton = tk.Button(ventana, text="Abrir navegador de archivos", command=agregar_etiquetas)
boton.grid(row=0, column=0, columnspan=7, pady=10)

#boton = tk.Button(ventana, text="Guardar y generar dzn", command=write_file)
#boton.grid(row=7, column=0, columnspan=7, pady=10)


names = ['J', 'K', 'Ej', 'Aj', 'Gj', 'Fj', 'Vj', 'Pj_inferior', 'Pj_superior', 'Supj', 'Infj', 'Pj_inicial', 'Dk', 'Rk']


# Creando etiquetas de cada campo

etiqueta_J = tk.Label(ventana, text="Ingresa J:")
etiqueta_K = tk.Label(ventana, text="Ingresa K:")
etiqueta_Ej = tk.Label(ventana, text="Ingresa Ej:")
etiqueta_Aj = tk.Label(ventana, text="Ingresa Aj:")
etiqueta_Gj = tk.Label(ventana, text="Ingresa Gj:")
etiqueta_Fj = tk.Label(ventana, text="Ingresa Fj:")
etiqueta_Vj = tk.Label(ventana, text="Ingresa Vj:")
etiqueta_Pjinferior = tk.Label(ventana, text="Ingresa Pj inferior")
etiqueta_Pjsuperior = tk.Label(ventana, text="Ingresa Pj superior:")
etiqueta_Supj = tk.Label(ventana, text="Ingresa Sup j:")
etiqueta_Infj = tk.Label(ventana, text="Ingresa Inf j")
etiqueta_Pj_inicial = tk.Label(ventana, text="Ingresa Pj inicial:")
etiqueta_Dk = tk.Label(ventana, text="Ingresa Dk:")
etiqueta_Rk = tk.Label(ventana, text="Ingresa Rk:")

# Organizando con grid las etiquetas

etiqueta_J.grid(row=2, column=0, pady=10)
etiqueta_K.grid(row=2, column=1, pady=10)
etiqueta_Ej.grid(row=2, column=2, pady=10)
etiqueta_Aj.grid(row=2, column=3, pady=10)
etiqueta_Gj.grid(row=2, column=4, pady=10)
etiqueta_Fj.grid(row=2, column=5, pady=10)
etiqueta_Vj.grid(row=2, column=6, pady=10)
etiqueta_Pjinferior.grid(row=5, column=0, pady=10)
etiqueta_Pjsuperior.grid(row=5, column=1, pady=10)
etiqueta_Supj.grid(row=5, column=2, pady=10)
etiqueta_Infj.grid(row=5, column=3, pady=10)
etiqueta_Pj_inicial.grid(row=5, column=4, pady=10)
etiqueta_Dk.grid(row=5, column=5, pady=10)
etiqueta_Rk.grid(row=5, column=6, pady=10)


# Organizando con Grid los campos de texto

campo_J.grid(row=3, column=0, padx=10, pady=10)
campo_K.grid(row=3, column=1, padx=10, pady=10)
campo_Ej.grid(row=3, column=2, padx=10, pady=10)
campo_Aj.grid(row=3, column=3, padx=10, pady=10)
campo_Gj.grid(row=3, column=4, padx=10, pady=10)
campo_Fj.grid(row=3, column=5, padx=10, pady=10)
campo_Vj.grid(row=3, column=6, padx=10, pady=10)
campo_Pjinferior.grid(row=6, column=0, padx=10, pady=10)
campo_Pjsuperior.grid(row=6, column=1, padx=10, pady=10)
campo_Supj.grid(row=6, column=2, padx=10, pady=10)
campo_Infj.grid(row=6, column=3, padx=10, pady=10)
campo_Pj_inicial.grid(row=6, column=4, padx=10, pady=10)
campo_Dk.grid(row=6, column=5, padx=10, pady=10)
campo_Rk.grid(row=6, column=6, padx=10, pady=10)

# Creando campos de texto por cada variable


# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
