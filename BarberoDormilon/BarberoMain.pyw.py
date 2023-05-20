from tkinter import *

import Barberia


def main():
    root = Tk()
    root.title('BARBERIA')
    root.configure(bg="#FAF8AF")
    root.geometry("+350+180")
    root.resizable(0, 0)
    Barberia.Barberia(root)
    root.mainloop()


if __name__ == "__main__":
    main()