import turtle
import os
import ui

ui.ui_setup(0, ui.h, "black", "red", "关闭TurtleOS", ui.w / 5, ui.h / 5)

ui.canvas.bind("<Motion>", ui.on_motion)

turtle.mainloop()