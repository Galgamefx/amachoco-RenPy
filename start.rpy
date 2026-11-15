# Full-game entry point (mirrors the original _start.bss).
label start:
    if _os.environ.get("BGI_UI_TOUR"):
        jump ui_tour
    if persistent.lang is None:
        $ persistent.lang = "sc"
    if _smoke_label():
        jump smoke_start
    scene black
    with fade
    jump ac_00common
