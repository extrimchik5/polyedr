#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()
try:
    for name in ["cow", 'box']:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()

        # Создаем полиэдр и рисуем его
        polyedr = Polyedr(f"data/{name}.geom")
        polyedr.draw(tk)

        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")

        # Выводим длину полуневидимых рёбер
        invisible_count = polyedr.calculate()
        print(f"Сумма длин проекций: {invisible_count}")

        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()