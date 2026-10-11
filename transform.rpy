transform move_right_to_left:
    zoom 1.5
    align (0.2, 0.5)
    xoffset -448        # 从屏幕右侧外开始（1.0 代表屏幕右边缘）
    linear 30.0 xoffset 0

transform zoom_in_out:
    zoom 1.5
    align (0.5, 0.5)
    linear 2 zoom 1.0

transform zoom_in_out1:
    align (0.5, 0.5)
    linear 0.8 zoom 1.24
    align (0.5, 0.5)

transform zoom_in_out2:
    zoom 1.24
    align (0.5, 0.5)
    linear 0.5 zoom 1.0
    align (0.5, 0.5)

define mask004 = ImageDissolve("transform/mask004.png", 0.3, reverse=True)

define mask003 = ImageDissolve("transform/mask003.png", 1.0, reverse=True)

define mask003a = ImageDissolve("transform/mask003a.png", 1.0, reverse=True)

define mask024a = ImageDissolve("transform/mask024a.png", 1.2, reverse=True)

define mask016f = ImageDissolve("transform/mask016f.png", 1.0, reverse=True)

define mask016g = ImageDissolve("transform/mask016g.png", 1.0, reverse=True)

transform shake_xyw:
    xoffset 0
    yoffset 0
    linear 0.1 xoffset 5 yoffset -5
    linear 0.1 xoffset -5 yoffset 5
    linear 0.05 xoffset 0 yoffset 0

transform shake_xy:
    pause 0.5
    xoffset 0
    yoffset 0
    linear 0.1 xoffset 3 yoffset -3
    linear 0.1 xoffset -3 yoffset 3

transform shake_y:
    pause 0.5
    yoffset 0
    linear 0.1 yoffset -3
    linear 0.1 yoffset 3

transform shake_y2:
    pause 0.5
    yoffset 0
    linear 0.15 yoffset -5
    linear 0.15 yoffset 5

transform shake_y3:
    pause 0.5
    yoffset 0
    linear 0.25 yoffset 10
    linear 0.25 yoffset -10

transform shake_y1:
    yoffset 0
    linear 0.25 yoffset 10
    linear 0.25 yoffset -10

transform shake_ry:
    yoffset 0
    linear 0.25 yoffset -5
    linear 0.25 yoffset 5
    linear 0.125 yoffset 0
    repeat

transform character_sequence:
    # 初始状态：在屏幕内偏右的位置，透明
    align (0.47, -0.5)
    xpos 0.55
    alpha 0
    matrixcolor BrightnessMatrix(-1)

    # 入场：淡入 + 从右往左滑到中央（不是从屏幕外进来）
    parallel:
        linear 0.2 alpha 1.0
    parallel:
        easeout 0.2 xpos 0.5

    # 停留一下
    pause 0.5

    # 向左边快速跳一下
    parallel:
        easeout 0.3 xpos 0.45
    parallel:    
        easeout 0.15 yoffset -100
    parallel:
        pause 0.15
        easeout 0.15 yoffset 0
    pause 0.1
    easein 0.2 xpos 0.4 alpha 0.0

transform sequence:
    xpos 0.47
    easein 1 xpos 0.45 alpha 0.0