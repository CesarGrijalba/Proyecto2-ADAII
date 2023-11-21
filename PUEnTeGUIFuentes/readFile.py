from tkinter import filedialog


def open_file():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    E, A, G, F, V, P_Inf, P_Sup, Sup, Inf, P0, D, R = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )

    with open(archivo) as file:
        J = file.readline()
        K = file.readline()
        E = (file.readline()).strip().split(",")
        A = (file.readline()).strip().split(",")
        G = (file.readline()).strip().split(",")
        F = (file.readline()).strip().split(",")
        V = (file.readline()).strip().split(",")
        P_Inf = (file.readline()).strip().split(",")
        P_Sup = (file.readline()).strip().split(",")
        Sup = (file.readline()).strip().split(",")
        Inf = (file.readline()).strip().split(",")
        P0 = (file.readline()).strip().split(",")
        D = (file.readline()).strip().split(",")
        R = (file.readline()).strip().split(",")

    return (
        J,
        K,
        E,
        A,
        G,
        F,
        V,
        P_Inf,
        P_Sup,
        Sup,
        Inf,
        P0,
        D,
        R,
    )
