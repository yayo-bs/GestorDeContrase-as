"""Interfaz grafica de la aplicacion generadora de contrasenas."""

import tkinter as tk

from utils.generador import generar_contrasena


def main() -> None:
    """Inicia la ventana principal de la aplicacion."""
    ventana = tk.Tk()
    ventana.title("Generador de contrasenas")
    ventana.resizable(False, False)

    contrasena = tk.StringVar()
    longitud = tk.IntVar(value=12)
    categorias = {
        "Mayusculas": tk.BooleanVar(value=True),
        "Minusculas": tk.BooleanVar(value=True),
        "Numeros": tk.BooleanVar(value=True),
        "Simbolos": tk.BooleanVar(value=False),
    }
    estado = tk.StringVar()

    def generar() -> None:
        contrasena.set(
            generar_contrasena(
                longitud=longitud.get(),
                mayusculas=categorias["Mayusculas"].get(),
                minusculas=categorias["Minusculas"].get(),
                numeros=categorias["Numeros"].get(),
                simbolos=categorias["Simbolos"].get(),
            )
        )

    def actualizar_estado(*_) -> None:
        seleccionadas = sum(variable.get() for variable in categorias.values())
        try:
            longitud_valida = longitud.get() >= seleccionadas
        except tk.TclError:
            longitud_valida = False

        puede_generar = seleccionadas > 0 and longitud_valida
        boton_generar.config(state=tk.NORMAL if puede_generar else tk.DISABLED)

        if seleccionadas == 0:
            estado.set("Selecciona al menos una categoria")
        elif not longitud_valida:
            estado.set("La longitud debe incluir todas las categorias")
        else:
            estado.set("")

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

    controles = tk.LabelFrame(marco, text="Personalizacion", padx=10, pady=5)
    controles.pack(fill="x", pady=(0, 10))

    tk.Label(controles, text="Longitud:").pack(anchor="w")
    tk.Spinbox(
        controles,
        from_=1,
        to=64,
        textvariable=longitud,
        width=5,
        justify="center",
    ).pack(anchor="w", pady=(0, 5))

    for nombre, variable in categorias.items():
        tk.Checkbutton(controles, text=nombre, variable=variable).pack(anchor="w")

    estado_label = tk.Label(marco, textvariable=estado, fg="red")
    estado_label.pack(pady=(0, 5))

    boton_generar = tk.Button(marco, text="Generar", command=generar)
    boton_generar.pack()

    for variable in (*categorias.values(), longitud):
        variable.trace_add("write", actualizar_estado)

    actualizar_estado()
    generar()
    ventana.mainloop()


if __name__ == "__main__":
    main()
