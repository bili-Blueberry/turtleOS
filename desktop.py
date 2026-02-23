import turtle
import ui

ui.button(0, ui.h, "black", "red", "电源选项", ui.w / 5, ui.h / 5)

ui.canvas.bind("<Motion>", ui.on_motion)

turtle.mainloop()