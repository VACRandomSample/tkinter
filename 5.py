from tkinter import Tk, Frame, BOTH, Canvas
from random import randint, choice
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Заполнение кругами")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        
        x = y = 0
        r = 50
        spawn = 1
        size = 250

        while spawn < 10000:
            colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime', "#f55c4b"])
            x = randint(0, size)
            y = randint(0, size)
            d = randint(0, size/2)
            canvas.create_oval(x, y, x+d, y+d, fill=colors)
            self.update()
            spawn += 1
        
def main():
    root = Tk()
    root.geometry("250x250+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()