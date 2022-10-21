from tkinter import Tk, Frame, BOTH, Canvas
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Вписанный квадрат")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        
        
        canvas.create_oval(25, 25, 125, 125, width=2)
        canvas.create_rectangle(40, 40, 110, 110, width=2)

def main():
    root = Tk()
    root.geometry("250x250+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()