import tkinter as tk
import utils_VN

PROGRAM_NÉV = "App (VN)"
ABLAK_SZÉLESSÉG = 800
ABLAK_MAGASSÁG = 700

root = tk.Tk()
root.title(PROGRAM_NÉV)
root.geometry(f"{ABLAK_SZÉLESSÉG}x{ABLAK_MAGASSÁG}")

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", lambda esemény_objektum: utils_VN.rajzolj_pöttyöt_VN(canvas, esemény_objektum))

root.mainloop()