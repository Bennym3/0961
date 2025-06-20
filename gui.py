import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from models import (
    fit_elastic_modulus,
    fit_hardness,
    larson_miller_parameter,
    oxide_thickness,
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CALPHAD Tools")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.mod_frame = ttk.Frame(notebook)
        self.hard_frame = ttk.Frame(notebook)
        self.creep_frame = ttk.Frame(notebook)
        self.oxide_frame = ttk.Frame(notebook)

        notebook.add(self.mod_frame, text="Modulus")
        notebook.add(self.hard_frame, text="Hardness")
        notebook.add(self.creep_frame, text="Creep")
        notebook.add(self.oxide_frame, text="Oxide")

        self.build_modulus()
        self.build_hardness()
        self.build_creep()
        self.build_oxide()

    def build_modulus(self):
        ttk.Label(self.mod_frame, text="Temperatures (comma)").pack()
        self.mod_temp = tk.Entry(self.mod_frame)
        self.mod_temp.pack()
        ttk.Label(self.mod_frame, text="Values (comma)").pack()
        self.mod_val = tk.Entry(self.mod_frame)
        self.mod_val.pack()
        ttk.Button(self.mod_frame, text="Fit", command=self.on_fit_modulus).pack()
        self.mod_result = ttk.Label(self.mod_frame, text="")
        self.mod_result.pack()

    def build_hardness(self):
        ttk.Label(self.hard_frame, text="Temperatures (comma)").pack()
        self.hard_temp = tk.Entry(self.hard_frame)
        self.hard_temp.pack()
        ttk.Label(self.hard_frame, text="Values (comma)").pack()
        self.hard_val = tk.Entry(self.hard_frame)
        self.hard_val.pack()
        ttk.Button(self.hard_frame, text="Fit", command=self.on_fit_hardness).pack()
        self.hard_result = ttk.Label(self.hard_frame, text="")
        self.hard_result.pack()

    def build_creep(self):
        ttk.Label(self.creep_frame, text="Temperature (K)").pack()
        self.creep_temp = tk.Entry(self.creep_frame)
        self.creep_temp.pack()
        ttk.Label(self.creep_frame, text="Time (h)").pack()
        self.creep_time = tk.Entry(self.creep_frame)
        self.creep_time.pack()
        ttk.Button(self.creep_frame, text="Compute LMP", command=self.on_creep).pack()
        self.creep_result = ttk.Label(self.creep_frame, text="")
        self.creep_result.pack()

    def build_oxide(self):
        ttk.Label(self.oxide_frame, text="k_p").pack()
        self.oxide_kp = tk.Entry(self.oxide_frame)
        self.oxide_kp.pack()
        ttk.Label(self.oxide_frame, text="Time (s)").pack()
        self.oxide_time = tk.Entry(self.oxide_frame)
        self.oxide_time.pack()
        ttk.Button(self.oxide_frame, text="Thickness", command=self.on_oxide).pack()
        self.oxide_result = ttk.Label(self.oxide_frame, text="")
        self.oxide_result.pack()

    def parse_list(self, entry: tk.Entry):
        return np.array([float(v) for v in entry.get().split(',') if v])

    def on_fit_modulus(self):
        try:
            temps = self.parse_list(self.mod_temp)
            vals = self.parse_list(self.mod_val)
            model = fit_elastic_modulus(temps, vals)
            self.mod_result.config(text=f"Coeffs: {model.coeffs}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_fit_hardness(self):
        try:
            temps = self.parse_list(self.hard_temp)
            vals = self.parse_list(self.hard_val)
            model = fit_hardness(temps, vals)
            self.hard_result.config(text=f"Coeffs: {model.coeffs}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_creep(self):
        try:
            T = float(self.creep_temp.get())
            t = float(self.creep_time.get())
            lmp = larson_miller_parameter(T, t)
            self.creep_result.config(text=f"LMP: {lmp:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_oxide(self):
        try:
            kp = float(self.oxide_kp.get())
            t = float(self.oxide_time.get())
            th = oxide_thickness(kp, t)
            self.oxide_result.config(text=f"Thickness: {th:.3g}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
