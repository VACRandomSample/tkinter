from tkinter import Tk, Frame, BOTH, Canvas
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Равностороний вписанный треугольник")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        
        canvas.create_polygon(140, 60, 69.3, 180, 210.7, 180, fill='white', outline='black')
        canvas.create_oval(100, 100, 180, 180, width=1)

def main():
    root = Tk()
    root.geometry("250x250+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main() 