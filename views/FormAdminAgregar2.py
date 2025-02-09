import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class FormAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar Material")
        self.root.geometry("800x500")
        self.root.configure(bg="#FFFFFF")

        # Métodos
        self.canvas()
        self.formulario()

    def canvas(self):
        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="#FFFFFF")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(0, 0, 226.77, 500, fill="#342217", outline="")

    def formulario(self):
        self.form_frame = ttk.Frame(self.root)
        self.form_frame.place(x=240, y=10, width=540, height=480)

        # Encabezado
        self.header = ttk.Label(self.form_frame, text="Agregar Material", font=("Arimo", 24))
        self.header.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Campos
        self.fields = [
            ("Resumen", "resumen"),
            ("Descriptor 1", "desc 1"),
            ("Descriptor 2", "desc 2"),
            ("Descriptor 3", "desc 3"),
        ]
        self.entries = {}

        for i, (label, var_name) in enumerate(self.fields):
            lbl = ttk.Label(self.form_frame, text=label, font=("Arimo", 16))
            lbl.grid(row=i * 2 + 1, column=0, sticky="w", padx=10, pady=5)

            entry_height = 5 if i == 0 else 1
            entry = tk.Text(self.form_frame, width=50, height=entry_height, bg="#d9d7d5")
            entry.grid(row=i * 2 + 2, column=0, padx=10, pady=(0, 10))
            self.entries[var_name] = entry

        self.aceptar_button = ttk.Button(
            self.form_frame, text="Aceptar", command=self.validar
        )
        self.aceptar_button.grid(row=len(self.fields) * 2 + 1, column=0, pady=20)

    def validar(self):
        """Valida que todos los campos estén llenos."""
        if not all(entry.get() for entry in self.entries.values()):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        else:
            messagebox.showinfo(" ", " ")


if __name__ == "__main__":
    root = tk.Tk()
    app = FormAdmin(root)
    root.mainloop()
