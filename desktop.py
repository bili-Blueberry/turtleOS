import ui
import os

ui.button(0, ui.h / 5, "white", "blue", "文件管理", ui.w / 5, ui.h / 5)
ui.button(0, ui.h / 5 * 2, "white", "green", "壁纸", ui.w / 5, ui.h / 5)
ui.button(0, ui.h / 5 * 3, "white", "gray", "设置", ui.w / 5, ui.h / 5)
ui.button(0, ui.h, "black", "red", "电源选项", ui.w / 5, ui.h / 5)

def onclick(x, y):
    if -ui.w / 10 <= x <= ui.w / 10:
        if ui.h / 5 * 0.5 <= y <= ui.h / 5 * 1.5:
            os.system("python3 file_manager.py")
        elif ui.h / 5 * 1.5 <= y <= ui.h / 5 * 2.5:
            os.system("python3 wallpaper.py")
        elif ui.h / 5 * 2.5 <= y <= ui.h / 5 * 3.5:
            os.system("python3 settings.py")
        elif ui.h / 5 * 3.5 <= y <= ui.h / 5 * 4.5:
            os.system("python3 shutdown.py")

ui.turtle.onclick(onclick)

ui.canvas.bind("<Motion>", ui.on_motion)

turtle.mainloop()