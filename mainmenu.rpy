# Main menu entry point.
#
# This project ships a custom screens.rpy and does not call gui.init(), so the
# layout module that normally provides `label main_menu_screen` is not loaded.
# Provide it directly: show the baked title screen and wait for an action.
label main_menu_screen:
    if _smoke_label():
        python:
            import os as _mm_os
            _mm_confirm = bool(_mm_os.environ.get("BGI_SMOKE_CONFIRM"))
            _mm_started = bool(getattr(persistent, "_smoke_started", False))
        if _mm_started and not _mm_confirm:
            python:
                import os, time
                import json as _json
                _info = {
                    "label": os.environ.get("BGI_SMOKE_LABEL", "?"),
                    "time": time.strftime("%H:%M:%S"),
                    "flags": dict(persistent.bgi_flags or {}),
                    "cg": len(persistent.cg_unlocked or []),
                    "bgm": len(persistent.bgm_unlocked or []),
                    "steam_full": persistent.steam_full,
                    # BACK LOG 的数据源：真实跑完一段脚本后这里必须 > 0。
                    "log": len(renpy.store._history_list),
                }
                with open(os.path.join(config.basedir, "_smoke_done.txt"), "a", encoding="utf-8") as _f:
                    _f.write(_json.dumps(_info, ensure_ascii=False) + "\n")
                renpy.quit()
        $ persistent._smoke_started = False
        jump start
    if _os.environ.get("BGI_UI_TOUR"):
        jump start
    call screen main_menu
    return