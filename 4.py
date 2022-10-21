from tkinter import Tk, Frame, BOTH, Canvas
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Описанный треугольник")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        canvas.create_line(0, 50, 200, 50, width=2)
        canvas.create_line(0, 50, 100, 185, width=2)
        canvas.create_line(100, 185, 200, 50, width=2)
        canvas.create_oval(50, 50, 150, 150, width=2)
                
        canvas.create_polygon(100+0, 100+50, 100+200, 100+50, 100+100, 100+185, width=2, outline='black', fill='white')
        canvas.create_oval(100+50, 100+50, 100+150, 100+150, width=2)
        
def main():
    root = Tk()
    root.geometry("350x350+350+350")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()