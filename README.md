# turtleOS
A OS with Python Turtle

闲着没事做的基于Python Turtle的“系统”。

功能不完善，见谅。

# UI.py
Make UI with Turtle

也是闲着没事做的，当第三方库用吧。

```Python
import ui
exit_fullscreen() # 退出全屏
ui.button(0, ui.h, "black", "red", "电源选项", ui.w / 5, ui.h / 5) # 在窗口左下角创建一个黑色边框的红色按钮“电源选项”
ui.canvas.bind("<Motion>", ui.on_motion)
turtle.mainloop()
```

像这样。

注：默认全屏！！！

AI写的，有问题可以反馈。