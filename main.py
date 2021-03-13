def 原地右转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 150, makerobo.Motors.RIGHT, -150)
def 原地左转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, -150, makerobo.Motors.RIGHT, 150)
def 右转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 200, makerobo.Motors.RIGHT, 0)
def 左转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 0, makerobo.Motors.RIGHT, 200)
def 后退():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, -150, makerobo.Motors.RIGHT, -150)
def 前进():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 150, makerobo.Motors.RIGHT, 150)
def 停止():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 0, makerobo.Motors.RIGHT, 0)
while not (input.button_is_pressed(Button.A)):
    停止()

def on_forever():
    前进()
    basic.pause(2000)
    后退()
    basic.pause(2000)
    左转()
    basic.pause(2000)
    右转()
    basic.pause(2000)
    原地左转()
    basic.pause(2000)
    原地右转()
    basic.pause(2000)
    while not (input.button_is_pressed(Button.A)):
        停止()
basic.forever(on_forever)
