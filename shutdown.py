import os
import ui

ui.text(0, 0, "请确保所有的操作已保存，然后选择一个选项。。。", "black", 24)
ui.button(0, ui.h / 2 - 50, "black", "red", "关闭TurtleOS", ui.w, ui.h / 5)
ui.button(0, ui.h / 2 - 150, "black", "orange", "关闭计算机", ui.w, ui.h / 5)
ui.button(0, ui.h / 2 - 250, "black", "yellow", "取消", ui.w, ui.h / 5)

ui.canvas.bind("<Motion>", ui.on_motion)

turtle.mainloop()