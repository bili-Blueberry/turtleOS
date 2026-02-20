import turtle

# 初始化鼠标图标
mouse = turtle.Turtle()
mouse.speed(0)
mouse.penup()
mouse.showturtle()
mouse.left((90 + 22.5))

# 初始化UI
ui = turtle.Turtle()
ui.speed(0)
ui.hideturtle()

# 创建 screen 与 canvas
screen = turtle.Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

w = canvas.winfo_width()
h = canvas.winfo_height()

# 尝试设置真正全屏并移除窗口装饰（使其难以退出）
try:
    root.attributes("-fullscreen", True)
    # 去掉窗口装饰，部分平台能生效
    root.overrideredirect(True)
except Exception:
    pass

# 禁用常见退出手段：Esc 键与窗口关闭
def _ignore_event(event=None):
    return "break"

root.bind("<Escape>", _ignore_event)
root.bind('<Key>', _ignore_event)
try:
    root.protocol("WM_DELETE_WINDOW", lambda: None)
except Exception:
    pass

# 让 turtle 跟随鼠标
screen.tracer(0)
def on_motion(event):
    global w, h
    tx = event.x - w / 2
    ty = h / 2 - event.y
    mouse.goto(tx, ty)
    screen.update()

def ui_setup(x, y, pencolor, fillcolor, text, weight, height):
    global w, h
    ui.goto(x, y)
    ui.setheading(90)
    pts = [ui.position()]
    ui.pencolor(pencolor)
    ui.fillcolor(fillcolor)
    ui.begin_fill()
    ui.pendown()
    ui.forward(weight)
    ui.left(90)
    ui.forward(height)
    ui.left(90)
    ui.forward(weight)
    ui.left(90)
    ui.forward(height)
    ui.end_fill()
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    cx = (min(xs) + max(xs)) / 2
    cy = (min(ys) + max(ys)) / 2
    ui.penup()
    ui.goto(cx, cy - 8)
    ui.write(text, align="center", font=("Arial", 16, "normal"))

