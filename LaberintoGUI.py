import tkinter as tk

class RectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Dibujar Rectángulos")
        self.geometry("400x150")
        
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Salir", command=self.quit)
        
        self.drawmenu = tk.Menu(self.menubar, tearoff=0)
        self.drawmenu.add_command(label="Dibujar Rectángulo", command=self.draw_rect)
        
        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)  
        self.menubar.add_cascade(label="Dibujar", menu=self.drawmenu)
        
        self.config(menu=self.menubar)
        
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack(expand=True, padx=10, pady=10)
        
        self.label_width = tk.Label(self, text="Ancho:")
        self.label_width.pack(side=tk.LEFT, padx=(10, 5))
        
        self.entry_width = tk.Entry(self)
        self.entry_width.pack(side=tk.LEFT)
        
        self.label_height = tk.Label(self, text="Alto:")
        self.label_height.pack(side=tk.LEFT, padx=(10, 5))
        
        self.entry_height = tk.Entry(self)
        self.entry_height.pack(side=tk.LEFT)
        
        self.button_draw = tk.Button(self, text="Dibujar", command=self.draw_rect)
        self.button_draw.pack(side=tk.LEFT, padx=(10, 0))
        
    def draw_rect(self):
        width = int(self.entry_width.get())
        height = int(self.entry_height.get())
        
        x1 = 10
        y1 = 10
        x2 = x1 + width
        y2 = y1 + height
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        
if __name__ == "__main__":
    app = RectApp()
    app.mainloop()
