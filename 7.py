from tkinter import Tk, Frame, BOTH, Canvas
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Диаграмма")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        
        x = y = 100
        r = 50
        
        canvas.create_oval(x-r, y-r, x+r, y+r)
        canvas.create_arc(x-r, y-r, x+r, y+r, start=0, extent=160, fill='blue')
        canvas.create_arc(x-r, y-r, x+r, y+r, start=0, extent=-200, fill='red')

def main():
    root = Tk()
    root.geometry("250x250+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()