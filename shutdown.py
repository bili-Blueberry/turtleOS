import os
import ui
import subprocess

ui.text(0, 0, "请确保所有的操作都已保存，然后选择一个选项。。。", "black", 24)
ui.button(0, ui.h / 2 - 50, "black", "red", "关闭TurtleOS", ui.w, ui.h / 5)
ui.button(0, ui.h / 2 - 150, "black", "orange", "关闭计算机", ui.w, ui.h / 5)
ui.button(0, ui.h / 2 - 250, "black", "yellow", "取消", ui.w, ui.h / 5)

def onclick(x, y):
    if -ui.w / 2 <= x <= ui.w / 2:
        if ui.h / 2 - 50 <= y <= ui.h / 2 + 50:
            os._exit(0)
            dir = os.path.abspath(os.getcwd())
            cmd = f"pgrep -f 'python.*{dir}'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)\
            pids = result.stdout.strip().split("\n")
            for pid in pids:
                if pid:
                    os.system(f"kill {pid}")
        elif ui.h / 2 - 150 <= y <= ui.h / 2 - 50:
            os.system("shutdown /s /t 00")
        elif ui.h / 2 - 250 <= y <= ui.h / 2 - 150:
            os._exit(0)

ui.turtle.onclick(onclick)

ui.canvas.bind("<Motion>", ui.on_motion)

turtle.mainloop()