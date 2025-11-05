import tkinter as tk
import math

root = tk.Tk()
root.title("iPhone Calculator")
root.geometry("350x600")
root.resizable(False, False)
root.config(bg="#000000")

expression = ""
sci_mode = False  # Scientific mode flag

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("0")

def toggle_sci():
    global sci_mode
    sci_mode = not sci_mode

    if sci_mode:
        frame.pack_forget()   # hide normal pad
        sci_frame.pack(fill="both", expand=True)  # show full scientific pad
        toggle_button.config(text="STD")  # change button name
    else:
        sci_frame.pack_forget()
        frame.pack()
        toggle_button.config(text="SCI")

equation = tk.StringVar()
equation.set("0")

entry = tk.Label(
    root, textvariable=equation, font=("Arial", 40),
    bg="#000000", fg="white", anchor="e", padx=20
)
entry.pack(expand=True, fill="both")

btn_style = {
    "font": ("Arial", 20, "bold"),
    "bd": 0,
    "relief": tk.FLAT,
    "width": 4,
    "height": 2,
    "highlightthickness": 0,
    "borderwidth": 0
}

# ================= NORMAL KEYS ==================
buttons = [
    ("C", clear, "#A5A5A5", "black"), ("+/-", lambda: press("-"), "#A5A5A5", "black"), ("%", lambda: press("%"), "#A5A5A5", "black"), ("/", lambda: press("/"), "white", "black"),
    ("7", lambda: press("7"), "#333333", "white"), ("8", lambda: press("8"), "#333333", "white"), ("9", lambda: press("9"), "#333333", "white"), ("*", lambda: press("*"), "white", "black"),
    ("4", lambda: press("4"), "#333333", "white"), ("5", lambda: press("5"), "#333333", "white"), ("6", lambda: press("6"), "#333333", "white"), ("-", lambda: press("-"), "white", "black"),
    ("1", lambda: press("1"), "#333333", "white"), ("2", lambda: press("2"), "#333333", "white"), ("3", lambda: press("3"), "#333333", "white"), ("+", lambda: press("+"), "white", "black"),
    ("0", lambda: press("0"), "#333333", "white"), (".", lambda: press("."), "#333333", "white"), ("=", equalpress, "white", "black")
]

frame = tk.Frame(root, bg="#000000")
frame.pack()

r = 0
c = 0
for text, cmd, bg, fg in buttons:
    btn = tk.Button(frame, text=text, command=cmd, **btn_style, bg=bg, fg=fg)
    if text == "0":
        btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=45)
        c += 2
    else:
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        c += 1

    if c > 3:
        c = 0
        r += 1

# ================= SCIENTIFIC KEYS ==================
sci_frame = tk.Frame(root, bg="#000000")

sci_buttons = [
    ("sin", lambda: press("math.sin(")), ("cos", lambda: press("math.cos(")), ("tan", lambda: press("math.tan(")), ("^", lambda: press("**")),
    ("log", lambda: press("math.log(")), ("π", lambda: press("math.pi")), ("e", lambda: press("math.e")), ("√", lambda: press("math.sqrt(")),
    ("(", lambda: press("(")), (")", lambda: press(")")),
    ("C", clear), ("=", equalpress)
]

r = 0
c = 0
for text, cmd in sci_buttons:
    btn = tk.Button(sci_frame, text=text, command=cmd, **btn_style, bg="#444444", fg="white")
    btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
    c += 1
    if c > 3:
        c = 0
        r += 1

# Mode Toggle Button
toggle_button = tk.Button(root, text="SCI", command=toggle_sci, bg="#111", fg="white", font=("Arial", 14))
toggle_button.pack(pady=5)

root.mainloop()
