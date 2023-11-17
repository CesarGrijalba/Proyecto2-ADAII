from tkinter import filedialog

def open_file():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    Ej, Aj, Gj, Fj, Vj, Pj_inferior, Pj_superior, Supj, Infj, Pj_inicial, Dk, Rk = [], [], [], [], [], [], [], [], [], [], [], []
    
    with open(archivo) as file:
        J = file.readline()
        K = file.readline()
        Ej = (((file.readline()).strip().split(',')))
        Aj = (((file.readline()).strip().split(',')))
        Gj = (((file.readline()).strip().split(',')))
        Fj = (((file.readline()).strip().split(',')))
        Vj = (((file.readline()).strip().split(',')))
        Pj_inferior = (((file.readline()).strip().split(',')))
        Pj_superior = (((file.readline()).strip().split(',')))
        Supj = (((file.readline()).strip().split(',')))
        Infj = (((file.readline()).strip().split(',')))
        Pj_inicial = (((file.readline()).strip().split(',')))
        Dk = (((file.readline()).strip().split(',')))
        Rk = (((file.readline()).strip().split(',')))
    
    return J, K, Ej, Aj, Gj, Fj, Vj, Pj_inferior, Pj_superior, Supj, Infj, Pj_inicial, Dk, Rk
       