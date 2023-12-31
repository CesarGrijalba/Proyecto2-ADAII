import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from readFile import open_file
from exect_minizinc import exec_minizinc

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto II - ADA II")

# Creando campos de texto por cada variable

campo_J = tk.Entry(ventana)
campo_K = tk.Entry(ventana)
campo_E = tk.Entry(ventana)
campo_A = tk.Entry(ventana)
campo_G = tk.Entry(ventana)
campo_F = tk.Entry(ventana)
campo_V = tk.Entry(ventana)
campo_P_inf = tk.Entry(ventana)
campo_P_sup = tk.Entry(ventana)
campo_Sup = tk.Entry(ventana)
campo_Inf = tk.Entry(ventana)
campo_P0 = tk.Entry(ventana)
campo_D = tk.Entry(ventana)
campo_R = tk.Entry(ventana)
# salida


# Funcion para convertor un conjutno de string a nuemros
#
def convert_to_float(data_set):
    subcadenas = data_set.split()
    numbers_float = [float(subcadena) for subcadena in subcadenas]
    return numbers_float


def convert_to_int(data_set):
    subcadenas = data_set.split()
    numbers_int = [int(subcadena) for subcadena in subcadenas]
    return numbers_int


# Funcion para agregar las variables a los campos
J_MATRIZ = 0
k_MATRIZ = 0


def agregar_etiquetas():
    global J_MATRIZ, k_MATRIZ
    data = open_file()
    J, K, E, A, G, F, V, P_inf, P_sup, Sup, Inf, P0, D, R = data
    J = J.strip()
    K = K.strip()
    J_MATRIZ = int(J)
    k_MATRIZ = int(K)
    campo_J.delete(0, tk.END)
    campo_K.delete(0, tk.END)
    campo_E.delete(0, tk.END)
    campo_A.delete(0, tk.END)
    campo_G.delete(0, tk.END)
    campo_F.delete(0, tk.END)
    campo_V.delete(0, tk.END)
    campo_P_inf.delete(0, tk.END)
    campo_P_sup.delete(0, tk.END)
    campo_Sup.delete(0, tk.END)
    campo_Inf.delete(0, tk.END)
    campo_P0.delete(0, tk.END)
    campo_D.delete(0, tk.END)
    campo_R.delete(0, tk.END)

    campo_J.insert(0, J)
    campo_K.insert(0, K)
    campo_E.insert(0, E)
    campo_A.insert(0, A)
    campo_G.insert(0, G)
    campo_F.insert(0, F)
    campo_V.insert(0, V)
    campo_P_inf.insert(0, P_inf)
    campo_P_sup.insert(0, P_sup)
    campo_Sup.insert(0, Sup)
    campo_Inf.insert(0, Inf)
    campo_P0.insert(0, P0)
    campo_D.insert(0, D)
    campo_R.insert(0, R)


# Funcion para escribir archivo
def write_file():
    #  Escribir archivo .dzn
    output_file = "DatosPUEnTe.dzn"
    J = campo_J.get()
    K = campo_K.get()
    E = campo_E.get()
    A = campo_A.get()
    G = campo_G.get()
    F = campo_F.get()
    V = campo_V.get()
    P_inf = campo_P_inf.get()
    P_sup = campo_P_sup.get()
    Sup = campo_Sup.get()
    Inf = campo_Inf.get()
    P0 = campo_P0.get()
    D = campo_D.get()
    R = campo_R.get()

    with open(output_file, "w") as file:
        J = J.strip()
        K = K.strip()
        E = convert_to_int(E)
        A = convert_to_float(A)
        G = convert_to_int(G)
        F = convert_to_int(F)
        V = convert_to_float(V)
        P_inf = convert_to_int(P_inf)
        P_sup = convert_to_int(P_sup)
        Sup = convert_to_int(Sup)
        Inf = convert_to_int(Inf)
        P0 = convert_to_int(P0)
        D = convert_to_int(D)
        R = convert_to_int(R)
        file.write(f"J = {J};\n")
        file.write(f"K = {K};\n")
        file.write(f"E = {E};\n")
        file.write(f"A = {A};\n")
        file.write(f"G = {G};\n")
        file.write(f"F = {F};\n")
        file.write(f"V = {V};\n")
        file.write(f"P_inf = {P_inf};\n")
        file.write(f"P_sup = {P_sup};\n")
        file.write(f"Sup = {Sup};\n")
        file.write(f"Inf = {Inf};\n")
        file.write(f"P0 = {P0};\n")
        file.write(f"D = {D};\n")
        file.write(f"R = {R};\n")
    print("Archivo .dzn generado")


def exec():
    global J_MATRIZ, k_MATRIZ
    filas = J_MATRIZ
    columnas = k_MATRIZ
    salida = exec_minizinc()
    print(salida)
    # Extraer el costo y la matriz P de la salida
    try:
        costo = float(salida[0].split("Costo: ")[1].split(",")[0])
        matriz_P = eval(salida[0].split("P: ")[1])
    except IndexError:
        costo = "INSATISFACTIBLE"
        matriz_P = ""

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Mostrar Costo y Matriz P")

    # Crear un widget Text
    texto_salida = ScrolledText(ventana, wrap="word", width=40, height=10)
    texto_salida.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Mostrar el costo
    texto_salida.insert(tk.END, f"Costo: {costo}\n\n")
    texto_salida.insert(tk.END, f"Potencia \n\n")
    # Organizar la matriz P en filas y columnas
    if type(matriz_P) is not str:
        for i in range(filas):
            for j in range(columnas):
                indice = i * columnas + j
                valor = matriz_P[indice]
                texto_salida.insert(tk.END, f"{valor}\t")
            texto_salida.insert(tk.END, "\n")

    # Hacer el widget Text de solo lectura
    texto_salida.config(state=tk.DISABLED)


# Crear el botón
boton = tk.Button(
    ventana, text="Abrir navegador de archivos", command=agregar_etiquetas
)
boton.grid(row=0, column=0, columnspan=7, pady=10)

boton = tk.Button(ventana, text="Guardar y generar dzn", command=write_file)
boton.grid(row=7, column=0, columnspan=7, pady=10)

boton = tk.Button(ventana, text="Ejecutar modelo", command=exec)
boton.grid(row=7, column=2, columnspan=7, pady=10)


names = [
    "J",
    "K",
    "E",
    "A",
    "G",
    "F",
    "V",
    "P_inf",
    "P_sup",
    "Sup",
    "Inf",
    "P0",
    "D",
    "R",
]


# Creando etiquetas de cada campo

etiqueta_J = tk.Label(ventana, text="Ingresa J:")
etiqueta_K = tk.Label(ventana, text="Ingresa K:")
etiqueta_E = tk.Label(ventana, text="Ingresa E:")
etiqueta_A = tk.Label(ventana, text="Ingresa A:")
etiqueta_G = tk.Label(ventana, text="Ingresa G:")
etiqueta_F = tk.Label(ventana, text="Ingresa F:")
etiqueta_V = tk.Label(ventana, text="Ingresa V:")
etiqueta_P_inf = tk.Label(ventana, text="Ingresa P_Sup")
etiqueta_P_sup = tk.Label(ventana, text="Ingresa P_Inf:")
etiqueta_Sup = tk.Label(ventana, text="Ingresa Sup:")
etiqueta_Inf = tk.Label(ventana, text="Ingresa Inf:")
etiqueta_P0 = tk.Label(ventana, text="Ingresa P0:")
etiqueta_D = tk.Label(ventana, text="Ingresa D:")
etiqueta_R = tk.Label(ventana, text="Ingresa R:")


# Organizando con grid las etiquetas

etiqueta_J.grid(row=2, column=0, pady=10)
etiqueta_K.grid(row=2, column=1, pady=10)
etiqueta_E.grid(row=2, column=2, pady=10)
etiqueta_A.grid(row=2, column=3, pady=10)
etiqueta_G.grid(row=2, column=4, pady=10)
etiqueta_F.grid(row=2, column=5, pady=10)
etiqueta_V.grid(row=2, column=6, pady=10)
etiqueta_P_inf.grid(row=5, column=0, pady=10)
etiqueta_P_sup.grid(row=5, column=1, pady=10)
etiqueta_Sup.grid(row=5, column=2, pady=10)
etiqueta_Inf.grid(row=5, column=3, pady=10)
etiqueta_P0.grid(row=5, column=4, pady=10)
etiqueta_D.grid(row=5, column=5, pady=10)
etiqueta_R.grid(row=5, column=6, pady=10)


# Organizando con Grid los campos de texto

campo_J.grid(row=3, column=0, padx=10, pady=10)
campo_K.grid(row=3, column=1, padx=10, pady=10)
campo_E.grid(row=3, column=2, padx=10, pady=10)
campo_A.grid(row=3, column=3, padx=10, pady=10)
campo_G.grid(row=3, column=4, padx=10, pady=10)
campo_F.grid(row=3, column=5, padx=10, pady=10)
campo_V.grid(row=3, column=6, padx=10, pady=10)
campo_P_inf.grid(row=6, column=0, padx=10, pady=10)
campo_P_sup.grid(row=6, column=1, padx=10, pady=10)
campo_Sup.grid(row=6, column=2, padx=10, pady=10)
campo_Inf.grid(row=6, column=3, padx=10, pady=10)
campo_P0.grid(row=6, column=4, padx=10, pady=10)
campo_D.grid(row=6, column=5, padx=10, pady=10)
campo_R.grid(row=6, column=6, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
