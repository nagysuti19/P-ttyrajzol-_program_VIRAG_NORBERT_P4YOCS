Virág Norbert P4YOCS

## Feladat leírása
A program egy grafikus felületet (tkinter) jelenít meg. Amikor a felhasználó a fehér vászonra kattint (eseménykezelés), a program egy véletlenszerű színű, méretű és körvonal-vastagságú kört rajzol a kattintás helyére. A kör tulajdonságait a `random` modul segítségével generálja, és az adatokat egy saját osztályban (`Pötty_VN`) tárolja. A rajzolási logika és az osztály a saját `utils_VN` modulban található.

## Modulok és a modulokban használt függvények

### 1. `main.py` (Indító fájl)
* **`tkinter`
    * `tk.Tk()`: A főablak (`root`) létrehozása.
    * `root.title()`: Ablak címének beállítása (a `PROGRAM_NÉV` változó alapján).
    * `root.geometry()`: Ablak méretének beállítása.
    * `tk.Canvas()`: Rajzvászon widget létrehozása.
    * `canvas.pack()`: Widget elhelyezése az ablakban.
    * `canvas.bind()`: Esemény (kattintás) összekötése egy `lambda` függvénnyel.
    * `root.mainloop()`: Eseménykezelő ciklus indítása.
* **`utils_VN` (Saját modul)**
    * `utils_VN.rajzolj_pöttyöt_VN()`: A kattintási eseményt kezelő, saját modulban lévő függvény hívása.

### 2. `utils_VN.py` 
* **`random` (Bemutatandó modul)**
    * `random.randint(a, b)`: Véletlen egész szám (pötty sugara).
    * `random.choice(seq)`: Véletlen elem (szín) kiválasztása listából.
    * `random.uniform(a, b)`: Véletlen lebegőpontos szám (körvonal vastagsága).

## Osztály(ok)

* **`Pötty_VN`** (az `utils_VN.py` modulban)
    * `__init__(self, x, y)`: Konstruktor. Létrehoz egy új pöttyöt a kattintás helyén (`x`, `y`), és a `random` modul segítségével véletlenszerű sugarat, színt és körvonal-vastagságot generál neki.
    * `get_koordináták(self)`: Metódus, amely a pötty középpontja és sugara alapján kiszámolja a `create_oval` számára szükséges sarokkoordinátákat.

