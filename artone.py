from tkinter import *
from tkinter import filedialog, messagebox
import turtle
import json
import time
import sys
import os
from PIL import ImageGrab

# ------------------ START MENU ------------------ #
def launch_main_app(project_to_load=None):
    start_root.destroy()

    # Setup main drawing window
    root = Tk()
    root.title("Turtle Art")
    root.geometry("1000x700")
    root.resizable(True, True)

    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=True)

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")
    t = turtle.RawTurtle(screen)
    t.shape("classic")
    t.speed(0)
    t.pensize(2)

    is_eraser = False
    default_color = "black"
    default_pensize = 2
    actions = []
    redo_stack = []

    def add_action():
        actions.append({
            "pos": t.pos(),
            "heading": t.heading(),
            "color": t.pencolor(),
            "pen": t.isdown(),
            "shape": t.shape(),
            "size": t.pensize()
        })
        redo_stack.clear()

    def forward(): t.forward(20); add_action()
    def up(): t.setheading(90); t.forward(20); add_action()
    def down(): t.setheading(270); t.forward(20); add_action()
    def left(): t.setheading(180); t.forward(20); add_action()
    def right(): t.setheading(0); t.forward(20); add_action()
    def uleft(): t.lt(45); t.forward(20); add_action()
    def uright(): t.rt(45); t.forward(20); add_action()
    def dleft(): t.lt(135); t.forward(20); add_action()
    def dright(): t.rt(135); t.forward(20); add_action()

    def set_color(c):
        nonlocal is_eraser, default_color
        default_color = c
        is_eraser = False
        t.pencolor(c)
        t.pensize(default_pensize)

    def toggle_eraser(event=None):
        nonlocal is_eraser
        is_eraser = not is_eraser
        if is_eraser:
            t.pencolor("white")
            t.pensize(2.5)
        else:
            t.pencolor(default_color)
            t.pensize(default_pensize)

    def penup(event=None): t.penup()
    def pendown(event=None): t.pendown()

    def redraw():
        t.clear()
        t.penup()
        for a in actions:
            t.shape(a.get("shape", "classic"))
            t.pensize(a.get("size", default_pensize))
            t.setpos(a["pos"])
            t.setheading(a["heading"])
            t.pencolor(a["color"])
            if a["pen"]:
                t.pendown()
            else:
                t.penup()
            t.forward(0.1)

    def save_project():
        filepath = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json")])
        if filepath:
            with open(filepath, 'w') as f:
                json.dump(actions, f)
            messagebox.showinfo("Saved", f"Project saved to:\n{filepath}")

    def load_project():
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filepath:
            with open(filepath, 'r') as f:
                data = json.load(f)
            actions.clear()
            redo_stack.clear()
            actions.extend(data)
            redraw()

    def save_image():
        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png")])
        if filepath:
            t.hideturtle()
            root.update()
            x = root.winfo_rootx() + canvas.winfo_x()
            y = root.winfo_rooty() + canvas.winfo_y()
            w = canvas.winfo_width()
            h = canvas.winfo_height()
            time.sleep(0.2)
            ImageGrab.grab(bbox=(x, y, x + w, y + h)).save(filepath)
            t.showturtle()
            messagebox.showinfo("Saved", f"Image saved to:\n{filepath}")

    def show_instructions():
        msg = (
            "Keyboard Controls:\n"
            "- Arrow Keys or WASD: Move turtle\n"
            "- Q/E/Z/C: Diagonal directions\n"
            "- B/G/R/L/Y/O: Change color\n"
            "- E: Toggle eraser/brush\n"
            "- Mouse Left Click: Pen up\n"
            "- Mouse Right Click: Pen down\n"
            "- Middle Click: Toggle eraser\n\n"
            "Menu:\n"
            "- File > Save Project: Save drawing steps\n"
            "- File > Load Project: Reload drawing\n"
            "- File > Save as Image: Save PNG of canvas\n"
            "- Edit > Turtle Shape: Change shape of the brush\n"
        )
        messagebox.showinfo("Instructions", msg)

    # If loading project
    if project_to_load:
        try:
            with open(project_to_load, 'r') as f:
                data = json.load(f)
            actions.clear()
            actions.extend(data)
            redraw()
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not load project:\n{e}")

    # Key bindings
    screen.listen()
    screen.onkey(forward, "Up")
    screen.onkey(up, "w")
    screen.onkey(down, "s")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    screen.onkey(uleft, "q")
    screen.onkey(uright, "e")
    screen.onkey(dleft, "z")
    screen.onkey(dright, "c")

    screen.onkey(lambda: set_color("blue"), "b")
    screen.onkey(lambda: set_color("green"), "g")
    screen.onkey(lambda: set_color("red"), "r")
    screen.onkey(lambda: set_color("black"), "l")
    screen.onkey(lambda: set_color("yellow"), "y")
    screen.onkey(lambda: set_color("orange"), "o")
    screen.onkey(toggle_eraser, "E")

    canvas.bind("<Button-1>", penup)
    canvas.bind("<Button-2>", toggle_eraser)
    canvas.bind("<Button-3>", pendown)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save Project", command=save_project)
    filemenu.add_command(label="Load Project", command=load_project)
    filemenu.add_command(label="Save as Image", command=save_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    shapemenu = Menu(editmenu, tearoff=0)
    shapemenu.add_command(label="Arrow", command=lambda: t.shape("arrow"))
    shapemenu.add_command(label="Turtle", command=lambda: t.shape("turtle"))
    shapemenu.add_command(label="Circle", command=lambda: t.shape("circle"))
    shapemenu.add_command(label="Square", command=lambda: t.shape("square"))
    shapemenu.add_command(label="Triangle", command=lambda: t.shape("triangle"))
    shapemenu.add_command(label="Classic", command=lambda: t.shape("classic"))
    editmenu.add_cascade(label="Turtle Shape", menu=shapemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instructions", command=show_instructions)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()

# ------------------ START WINDOW ------------------ #
start_root = Tk()
start_root.title("Turtle Art - Start")
start_root.geometry("400x250")
start_root.configure(bg="#f0f0f0")
start_root.resizable(False, False)

Label(start_root, text="🎨 Turtle Art Playground", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

def start_new():
    launch_main_app()

def load_existing():
    path = filedialog.askopenfilename(
        title="Load Turtle Project",
        filetypes=[("Turtle Project Files", "*.json")]
    )
    if path:
        launch_main_app(path)

button_style = {"font": ("Helvetica", 12), "width": 30, "padx": 5, "pady": 5}
Button(start_root, text="🖌️ Enter a New Turtle Art Project", command=start_new, **button_style).pack(pady=5)
Button(start_root, text="📂 Load Existing Project", command=load_existing, **button_style).pack(pady=5)
Button(start_root, text="❌ Exit", command=start_root.quit, **button_style).pack(pady=20)

start_root.mainloop()
