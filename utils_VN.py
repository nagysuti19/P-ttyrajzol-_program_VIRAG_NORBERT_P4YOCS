import random


class Pötty_VN:
    def __init__(self, x, y):
        self.r = random.randint(10, 40)

        színek = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'cyan']
        self.szín = random.choice(színek)

        self.outline_width = random.uniform(1.0, 3.5)

        self.x = x
        self.y = y

    def get_koordináták(self):
        x1 = self.x - self.r
        y1 = self.y - self.r
        x2 = self.x + self.r
        y2 = self.y + self.r
        return (x1, y1, x2, y2)


def rajzolj_pöttyöt_VN(canvas, esemény):
    x_klikk = esemény.x
    y_klikk = esemény.y

    uj_pötty = Pötty_VN(x_klikk, y_klikk)

    koords = uj_pötty.get_koordináták()

    canvas.create_oval(
        koords,
        fill=uj_pötty.szín,
        width=uj_pötty.outline_width,
        outline='black'
    )