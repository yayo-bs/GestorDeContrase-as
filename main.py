"""Interfaz grafica de la aplicacion generadora de contrasenas."""

import tkinter as tk

from utils.generador import generar_contrasena


def main() -> None:
    """Inicia la ventana principal de la aplicacion."""
    ventana = tk.Tk()
    ventana.title("Generador de contrasenas")
    ventana.resizable(False, False)

    contrasena = tk.StringVar()

    def generar() -> None:
        contrasena.set(generar_contrasena())

    marco = tk.Frame(ventana, padx=20, pady=20)
    marco.pack()

    campo_contrasena = tk.Entry(
        marco,
        textvariable=contrasena,
        width=24,
        justify="center",
        state="readonly",
    )
    campo_contrasena.pack(pady=(0, 10))

    boton_generar = tk.Button(marco, text="Generar", command=generar)
    boton_generar.pack()

    generar()
    ventana.mainloop()


if __name__ == "__main__":
    main()
