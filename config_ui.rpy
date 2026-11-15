###########################################################################
##  系统设定 / SYSTEMCONFIG
##  原版 BGI 配置窗口的复刻。
##
##  静态美术全部来自原版精灵，在构建期烘焙进 game/ui/cfg*：
##    cfg_{text,game,sound}[_dim]_{lang}.png  —— 牌匾 + 面板 + 页面内容
##    cfgw_tab_{page}_{lang}.png              —— 选中态的白色标签
##    cfgw_{thumb,min,max,check,dot,...}.png  —— 运行时反复叠加的控件
##  这里负责原版「运行时才绘制」的那一层：滑条拇指、MIN/MAX 菱形、对勾、
##  单选圆点、读数、样本文字、按钮精灵与全部热区。
###########################################################################

default persistent.cfg_page = "text"
default persistent.cfg_flags = {}
default persistent.cfg_dirty = False
default persistent.cfg_target = "normal"
default persistent.cfg_hsv = None
default persistent.cfg_text_color = None
default persistent.cfg_read_color = None
default persistent.cfg_char_color = None
default persistent.cfg_auto_wait = 0.5
default persistent.cfg_window_opacity = 1.0
default persistent.cfg_char_volume = 1.0
default persistent.cfg_snap = None
default persistent.cfg_color_backup = None
# 语言 / 版本：界面里的选择只是暂存（None＝沿用当前生效值），
# 按「反映设定内容」才真正切换。
default persistent.cfg_lang = None
default persistent.cfg_edition = None

init -2 python:

    CFG_TAB_ORDER = ["text", "game", "sound"]
    CFG_TAB_X = {"text": 371, "game": 521, "sound": 671}
    CFG_TAB_W = {"text": 107, "game": 103, "sound": 247}

    CFG_DEFAULTS = {
        # 文本
        "text_instant": False,
        "auto_detail": False,
        "auto_char_instant": False,
        "auto_after_choice": False,
        "font_common": False,
        "click_next": False,
        "seen_instant": True,
        "skip_seen_instant": False,
        "skip_after_choice": False,
        "skip_unread": False,
        "rmb_auto": True,
        # 游戏
        "fullscreen": False,
        "aspect_fix": True,
        "res": "1280x720",
        "interp": "bicubic",
        "rmb_sysmenu": False,
        "space_enter": False,
        "show_info": True,
        "zoom_ui": True,
        "auto_mouse": True,
        "fx": True,
        "fx_big": True,
        "fx_small": True,
        "fx_ui": True,
        "fx_sys": True,
        "fx_anim": True,
        "confirm": True,
        "cf_overwrite": True,
        "cf_copy": True,
        "cf_delete": True,
        "cf_load": True,
        "cf_return": True,
        "cf_quickjump": True,
        "cf_resetcfg": True,
        "cf_apply": True,
        "cf_title": True,
        "cf_quit": True,
        # 声音
        "voice_duck": True,
        "voice_text": True,
        "voice_stop_page": False,
        "mute_master": False,
        "mute_bgm": False,
        "mute_se": False,
        "mute_voice": False,
        "char_sel": "other_m",
        "char_color_unify": False,
    }

    CFG_SAMPLE = {"sc": "巧可甜", "tc": "巧可甜", "jp": "ちょこたん"}

    CFG_TEXT = {
        "apply": {"sc": "要反映当前的设定内容吗？",
                  "tc": "要反映目前的設定內容嗎？",
                  "jp": "設定内容を反映しますか？"},
        "leave": {"sc": "有尚未反映的设定。\n离开将放弃这些改动，确定吗？",
                  "tc": "有尚未反映的設定。\n離開將放棄這些變更，確定嗎？",
                  "jp": "未反映の設定があります。\n移動すると変更は破棄されます。よろしいですか？"},
        "reset": {"sc": "要恢复系统的初始设定吗？",
                  "tc": "要恢復系統的初始設定嗎？",
                  "jp": "初期設定に戻しますか？"},
        "yes": {"sc": "是", "tc": "是", "jp": "はい"},
        "no": {"sc": "否", "tc": "否", "jp": "いいえ"},
    }

    def cfg_text(key):
        try:
            lang = ui_lang()
        except Exception:
            lang = "sc"
        return CFG_TEXT[key].get(lang) or CFG_TEXT[key]["sc"]

    CFG_COLOR_FIELD = {
        "normal": ("cfg_text_color", "#ffffff"),
        "read": ("cfg_read_color", "#fefb8f"),
        "char": ("cfg_char_color", "#ffffff"),
    }

    def _cfg_flags():
        if persistent.cfg_flags is None:
            persistent.cfg_flags = {}
        return persistent.cfg_flags

    def cfg_get(key, default=None):
        if default is None:
            default = CFG_DEFAULTS.get(key, False)
        return _cfg_flags().get(key, default)

    def cfg_set(key, value):
        flags = _cfg_flags()
        flags[key] = value
        persistent.cfg_flags = flags
        persistent.cfg_dirty = True
        # 立刻推给引擎，界面才是「即时预览」而不是只改了块颜色。
        apply_cfg()
        renpy.restart_interaction()

    def cfg_toggle(key, default=None):
        cfg_set(key, not cfg_get(key, default))

    # ---- 语言 / 版本 ---------------------------------------------------
    # 和音量、文字速度同一套模型：改动立刻生效（可以当场预览），但进入
    # 界面时的快照保留着，离开界面就退回，按「反映设定内容」才定为新基线。
    def cfg_lang_sel():
        try:
            return ui_lang()
        except Exception:
            return persistent.lang or "sc"

    def cfg_set_lang(code):
        if code != cfg_lang_sel():
            set_lang(code)
        persistent.cfg_dirty = True
        renpy.restart_interaction()

    def cfg_edition_sel():
        """True＝完整版，False＝全年龄版。"""
        return True if persistent.steam_full is None else bool(persistent.steam_full)

    def cfg_set_edition(full):
        persistent.steam_full = bool(full)
        persistent.cfg_dirty = True
        renpy.restart_interaction()

    # ---- 暂存 / 反映 ---------------------------------------------------
    # 原版行为：界面里的改动只是暂存，按「反映设定内容」才真正生效；
    # 直接离开这个界面会丢弃改动（离开前弹确认窗）；「初始化」把暂存值
    # 恢复成系统初值，同样要按「反映设定内容」才写进系统。
    def _cfg_flags_norm():
        """只保留与默认值不同的项，默认值补齐不会把界面误判成「已改动」。"""
        out = {}
        for k, v in _cfg_flags().items():
            if CFG_DEFAULTS.get(k, v) != v:
                out[k] = v
        return out

    def _cfg_state():
        return (
            round(float(preferences.text_cps), 3),
            round(float(preferences.afm_time), 3),
            tuple(round(preferences.get_volume(m), 3) for m in ("music", "sound", "voice")),
            tuple(sorted(_cfg_flags_norm().items())),
            tuple(getattr(persistent, f, None) for f in
                  ("cfg_text_color", "cfg_read_color", "cfg_char_color")),
            tuple(round(float(x), 4) for x in (persistent.cfg_hsv or ())),  # 未选过色时为空，与默认值等价
            round(float(persistent.cfg_auto_wait or 0.0), 3),
            round(float(persistent.cfg_window_opacity or 0.0), 3),
            round(float(persistent.cfg_char_volume or 0.0), 3),
            tuple(sorted((persistent.cfg_char_volumes or {}).items())),
            # 语言 / 版本：和音量、文字速度一样是「即时预览」，离开界面时
            # 由 cfg_restore() 一起退回，所以状态里记的就是当前生效值。
            persistent.lang or "sc",
            bool(persistent.steam_full),
        )

    def cfg_begin():
        """进入界面时记下当前生效值，作为「放弃改动」的回滚点。"""
        if persistent.cfg_snap is None:
            persistent.cfg_snap = _cfg_state()

    def cfg_dirty():
        return persistent.cfg_snap is not None and _cfg_state() != persistent.cfg_snap

    def cfg_restore():
        """丢弃暂存，把系统设定退回进入界面时的状态。"""
        st = persistent.cfg_snap
        if st:
            (tps, afm, vols, flags, cols, hsv, auto_wait, opacity, char_vol,
             char_vols, lang, full) = st
            preferences.text_cps = tps
            preferences.afm_time = afm
            for m, v in zip(("music", "sound", "voice"), vols):
                preferences.set_volume(m, v)
            persistent.cfg_flags = dict(flags)
            for f, c in zip(("cfg_text_color", "cfg_read_color", "cfg_char_color"), cols):
                setattr(persistent, f, c)
            persistent.cfg_hsv = list(hsv) if hsv else None
            persistent.cfg_auto_wait = auto_wait
            persistent.cfg_window_opacity = opacity
            persistent.cfg_char_volume = char_vol
            persistent.cfg_char_volumes = dict(char_vols)
            # 语言/版本也是即时生效的，回滚要把它俩一起退回去。
            if lang and lang != cfg_lang_sel():
                set_lang(lang)
            persistent.steam_full = bool(full)
        persistent.cfg_snap = None
        persistent.cfg_dirty = False
        persistent.cfg_color_backup = None
        if renpy.get_screen("confirm"):
            renpy.hide_screen("confirm")
        renpy.restart_interaction()

    def cfg_apply():
        """「反映设定内容」：暂存值已经在系统里，这里只把它定为新基线。"""
        persistent.cfg_snap = None
        persistent.cfg_dirty = False
        persistent.cfg_color_backup = None
        if renpy.get_screen("confirm"):
            renpy.hide_screen("confirm")
        renpy.restart_interaction()

    def cfg_ask_apply():
        if not cfg_dirty():
            return
        # 确认窗口统一走 screens.rpy 里的 screen confirm（和存读档、退出游戏
        # 用的是同一套美术），不要自己再画一套。
        if cfg_confirm_on("cf_apply"):
            renpy.run(Confirm(cfg_text("apply"), Function(cfg_apply), NullAction()))
        else:
            cfg_apply()

    def _cfg_leave_now(action):
        cfg_restore()
        # Return() 是「返回值型」动作：它返回 True，靠按钮动作的返回值来结束
        # 这次交互。Function 会把这里 return 出来的值当作它自己的返回值，
        # 所以必须一层层透传，否则点了「返回游戏」不会有任何反应。
        return renpy.run(action)

    def cfg_leave(action):
        if cfg_dirty():
            renpy.run(Confirm(cfg_text("leave"),
                              Function(_cfg_leave_now, action),
                              NullAction()))
        else:
            return _cfg_leave_now(action)

    def cfg_ask_reset():
        if not cfg_dirty():
            return
        if cfg_confirm_on("cf_resetcfg"):
            renpy.run(Confirm(cfg_text("reset"), Function(cfg_reset_all), NullAction()))
        else:
            cfg_reset_all()

    def cfg_reset_all():
        """「初始化」：暂存值恢复成系统初值，仍需按「反映设定内容」生效。"""
        persistent.cfg_flags = {}
        persistent.cfg_text_color = None
        persistent.cfg_read_color = None
        persistent.cfg_char_color = None
        persistent.cfg_hsv = None
        persistent.cfg_auto_wait = 0.5
        persistent.cfg_window_opacity = 1.0
        persistent.cfg_char_volume = 1.0
        persistent.cfg_char_volumes = {}
        persistent.cfg_color_backup = None
        persistent.cfg_page = "text"
        # 语言回简体中文、版本回完整版。语言/版本是即时生效的，直接写下去；
        # 不清 cfg_snap，所以重置后仍会显示成「已改动」，需再按一次反映。
        if cfg_lang_sel() != "sc":
            set_lang("sc")
        persistent.steam_full = True
        preferences.text_cps = config.default_text_cps or 40
        preferences.afm_time = 15
        for m in ("music", "sound", "voice"):
            preferences.set_volume(m, 1.0)
        apply_cfg()
        if renpy.get_screen("confirm"):
            renpy.hide_screen("confirm")
        renpy.restart_interaction()

    def cfg_set_page(page):
        persistent.cfg_page = page
        renpy.restart_interaction()

    # ---- 取色器 -------------------------------------------------------
    # 原版读数：色相 0..359，亮度 0..255，饱和度 0..255。
    CFG_HSV_DEFAULT = [0.0, 1.0, 146.0 / 255.0]

    def cfg_hsv():
        """当前取色值。**不写 persistent**：屏幕每帧都会读它，写回会让
        「只是打开界面」被误判成已改动（cfg_begin 的快照因此对不上）。"""
        v = persistent.cfg_hsv
        if not v:
            return list(CFG_HSV_DEFAULT)
        return v

    def _cfg_clamp(v):
        return 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)

    def _cfg_hsv_to_rgb(h, s, v):
        if s <= 0.0:
            c = int(round(v * 255))
            return (c, c, c)
        h = (h % 1.0) * 6.0
        i = int(h)
        f = h - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        r, g, b = [
            (v, t, p), (q, v, p), (p, v, t),
            (p, q, v), (t, p, v), (v, p, q),
        ][i % 6]
        return (int(round(r * 255)), int(round(g * 255)), int(round(b * 255)))

    def cfg_color_hex(which):
        field, fallback = CFG_COLOR_FIELD.get(which, CFG_COLOR_FIELD["normal"])
        return getattr(persistent, field, None) or fallback

    def cfg_target():
        return persistent.cfg_target or "normal"

    def cfg_set_target(which):
        persistent.cfg_target = which
        renpy.restart_interaction()

    def _cfg_push_color():
        h, s, v = cfg_hsv()
        hexcol = "#%02x%02x%02x" % _cfg_hsv_to_rgb(h, s, v)
        field, _fb = CFG_COLOR_FIELD.get(cfg_target(), CFG_COLOR_FIELD["normal"])
        # 取色器上的「取消」要能把这次选色退回去，所以第一次动之前先记一份。
        if persistent.cfg_color_backup is None:
            persistent.cfg_color_backup = [cfg_target(), getattr(persistent, field, None),
                                           list(cfg_hsv())]
        setattr(persistent, field, hexcol)
        renpy.restart_interaction()

    def cfg_color_accept():
        persistent.cfg_color_backup = None
        renpy.restart_interaction()

    def cfg_color_revert():
        bk = persistent.cfg_color_backup
        if bk:
            which, col, hsv = bk
            field, _fb = CFG_COLOR_FIELD.get(which, CFG_COLOR_FIELD["normal"])
            setattr(persistent, field, col)
            persistent.cfg_hsv = list(hsv)
        persistent.cfg_color_backup = None
        renpy.restart_interaction()

    def cfg_pick_hv(x, y, w, h):
        mx, my = renpy.get_mouse_pos()
        cur = cfg_hsv()
        hh = _cfg_clamp((mx - x) / float(max(1, w)))
        vv = 1.0 - _cfg_clamp((my - y) / float(max(1, h)))
        persistent.cfg_hsv = [hh, cur[1], vv]
        _cfg_push_color()

    def cfg_pick_sat(x, y, h):
        mx, my = renpy.get_mouse_pos()
        cur = cfg_hsv()
        ss = 1.0 - _cfg_clamp((my - y) / float(max(1, h)))
        persistent.cfg_hsv = [cur[0], ss, cur[2]]
        _cfg_push_color()

    def cfg_commit():
        persistent.cfg_dirty = False

    def cfg_set_char_vol_by_slider(value):
        """滑条回调：写当前选中角色的音量（界面层）。"""
        cfg_set_char_vol(cfg_char_sel(), value)
        renpy.restart_interaction()


    def cfg_char_select(name):
        cfg_set("char_sel", name)

    def _cfg_avg_volume():
        return (preferences.get_volume("music")
                + preferences.get_volume("sound")
                + preferences.get_volume("voice")) / 3.0

    def _cfg_set_all_volume(v):
        for _m in ("music", "sound", "voice"):
            preferences.set_volume(_m, v)

    class CfgCharVolume(BarValue):
        """「角色个别音量」：滑条编辑当前选中角色的音量。

        数据存在 persistent.cfg_char_volumes（角色 key → 0..1），
        生效层按语音文件名前缀把该角色的语音音量乘上去。"""

        def get_adjustment(self):
            return ui.adjustment(range=1.0, value=cfg_char_vol(),
                                 step=0.02, changed=cfg_set_char_vol_by_slider)

        def get_style(self):
            return "bar", "vbar"


    class CfgAllVolume(BarValue):
        """「整体音量」：同时驱动 music / sound / voice 三个混音器。

        Ren'Py 自带的 Preference("all volume") 在此版本会以 list 作为 mixer 键
        查找音量字典而抛 TypeError，所以这里自己实现一个。"""

        def get_adjustment(self):
            return ui.adjustment(range=1.0, value=_cfg_avg_volume(),
                                 step=0.02, changed=_cfg_set_all_volume)

        def get_style(self):
            return "bar", "vbar"


transform cfg_dim:
    alpha 0.3

transform cfg_none:
    alpha 1.0


style cfg_bar:
    xysize (316, 26)
    # 轨道渐变与上下白描边都烘焙在页图层里，bar 本体只当热区用：
    # 若交给 Ren'Py 的 thumb 通道，它会把拇指按 bar 宽度重采样，
    # 结果在轨道上糊出一层半透明粉色。所以这里全部置空，拇指自己 add。
    left_bar Null()
    right_bar Null()
    thumb Null()
    fore_gutter 0
    aft_gutter 0
    thumb_offset 0


## ---------------------------------------------------------------------
##  滑条：轨道与白色描边已烘焙在页图层里，这里只叠拇指和两端菱形
## ---------------------------------------------------------------------
screen cfg_bar(value, x, y, w=316, minpos=None, maxpos=None, dim=False,
               thumby=None, maxdim=False):
    $ _min = minpos or (x - 62, y - 3)
    $ _max = maxpos or (x + w + 41, y - 3)
    python:
        _adj = value.get_adjustment()
        _rng = float(getattr(_adj, "range", 0) or 0)
        _val = float(getattr(_adj, "value", 0) or 0)
        _ratio = min(1.0, max(0.0, _val / _rng)) if _rng > 0 else 0.0
        _thx = x + int(round((w - 26) * _ratio))
        _thy = y if thumby is None else thumby

    bar:
        value value
        style "cfg_bar"
        xpos x
        ypos y
        xysize (w, 26)
        at (cfg_dim if dim else cfg_none)

    add ui_img("cfgw_thumb") xpos _thx ypos _thy at (cfg_dim if dim else cfg_none)

    # 角色个别音量那条滑条的 MAX 菱形在原版里是 30% 淡出画出来的
    # （实测 (219,202,195) 描边 / (249,236,228) 内填，正是深棕菱形按
    # alpha 0.3 叠在面板色上的结果），所以给它一个单独的 maxdim 开关。
    add ui_img("cfgw_min") xpos _min[0] ypos _min[1] at (cfg_dim if dim else cfg_none)
    add ui_img("cfgw_max") xpos _max[0] ypos _max[1] at (cfg_dim if (dim or maxdim) else cfg_none)


## ---------------------------------------------------------------------
##  复选框 / 单选：方框烘焙在页图层里，这里只画聚焦框和勾选标记
## ---------------------------------------------------------------------
screen cfg_cb(key, x, y, big=True):
    $ _on = cfg_get(key)
    $ _size = 30 if big else 15

    button:
        xpos x
        ypos y
        xysize (_size, _size)
        background None
        hover_background (ui_img("cfgw_focus30") if big else ui_img("cfgw_focus16"))
        action Function(cfg_toggle, key)
        if _on:
            if big:
                add ui_img("cfgw_check") xpos 0 ypos 0
            else:
                add ui_img("cfgw_check_small") xpos 3 ypos 3


## 单选。方框烘焙在页图层里时永远只是深棕的「未选中」态；原版一旦
## 选中就把框换成彩色（游戏页的分辨率/插值是粉色，声音页的角色是浅橘），
## 所以选中时要在原位再叠一层彩色框，圆点画在它上面。
screen cfg_radio(key, value, x, y, w=15, h=15, sel="pink"):
    $ _on = (cfg_get(key) == value)
    button:
        xpos x
        ypos y
        xysize (w, h)
        background None
        hover_background (ui_img("cfgw_focus30") if w > 20 else ui_img("cfgw_focus16"))
        action Function(cfg_set, key, value)
        if _on:
            if w > 20:
                add ui_img("cfgw_box30_" + sel) xpos 0 ypos 0
            else:
                add ui_img("cfgw_box15_" + sel) xpos 0 ypos 0
            add ui_img("cfgw_dot") xpos 0 ypos 0


## 带文字的 15x15 单选：方框不是烘焙在页图层里的（只有本页新增的两行
## 才用它），所以用 cfgw_box15 现画。整块（框＋文字）都是热区，手机上
## 好点；文字基线与页层里已有的 15x15 子项一致（ink 顶 = 框顶）。
screen cfg_pick(action, label, x, y, on, tw=0):
    # tw 只是给布局算宽度用的提示：0 表示按标签字数估（CJK 18px ≈ 20px/字）。
    $ _tw = tw or (len(label) * 20)
    button:
        xpos x - 5
        ypos y - 6
        xysize (_tw + 36, 26)
        background None
        hover_background Solid("#ffffff55")
        action action
        add ui_img("cfgw_box15") xpos 5 ypos 6
        if on:
            add ui_img("cfgw_dot") xpos 5 ypos 6
        text label:
            xpos 25
            ypos 1
            size 18
            font ui_font
            color "#482e1e"
            outlines []


## ---------------------------------------------------------------------
##  色块（71x71）：内填当前颜色，边框按是否选中切换
## ---------------------------------------------------------------------
screen cfg_swatch(target, x, y):
    $ _sel = (cfg_target() == target)
    $ _inset = 3 if _sel else 1

    button:
        xpos x
        ypos y
        xysize (71, 71)
        background None
        action Function(cfg_set_target, target)
        add Solid(cfg_color_hex(target)) xpos _inset ypos _inset xysize (71 - _inset * 2, 71 - _inset * 2)
        add ui_img("cfgw_sw_sel" if _sel else "cfgw_sw_unsel")


## ---------------------------------------------------------------------
##  取色器（文本页 / 声音页共用）
## ---------------------------------------------------------------------
screen cfg_picker(x, y, apply_x, apply_y, ro_y=318, ro_x=(985, 1075, 1154)):
    $ _h, _s, _v = cfg_hsv()

    add ui_img("cfgw_hsv") xpos x ypos y

    # 横轴色相 × 纵轴亮度
    button:
        xpos x
        ypos y
        xysize (170, 147)
        background None
        action Function(cfg_pick_hv, x, y, 170, 147)

    # 饱和度竖条
    button:
        xpos (x + 182)
        ypos (y + 4)
        xysize (20, 138)
        background None
        action Function(cfg_pick_sat, x + 182, y + 4, 138)

    add ui_img("cfgw_cross_a") xpos (x + int(_h * 170) - 5) ypos (y + int((1.0 - _v) * 147) - 5)
    add ui_img("cfgw_cross_b") xpos (x + 180) ypos (y + 4 + int((1.0 - _s) * 138) - 5)

    # 读数用原版的深藏青（baked 的「色相」「亮度」「饱和度」标签就是
    # #17264D），棕色会比美术里的标签明显偏暖。
    text ("%d" % (int(round(_h * 360)) % 360)):
        xpos ro_x[0]
        ypos ro_y
        xanchor 1.0
        size 10
        font ui_font
        color "#17264d"
    text ("%d" % int(round(_v * 255))):
        xpos ro_x[1]
        ypos ro_y
        xanchor 1.0
        size 10
        font ui_font
        color "#17264d"
    # 原版饱和度按 0..256 显示（满值读作 256，不是 255）。
    text ("%d" % int(round(_s * 256))):
        xpos ro_x[2]
        ypos ro_y
        xanchor 1.0
        size 10
        font ui_font
        color "#17264d"

    button:
        xpos apply_x
        ypos apply_y
        xysize (80, 26)
        background ui_img("cfgw_apply")
        hover_background ui_img("cfgw_apply_hover")
        action Function(cfg_color_accept)

    button:
        xpos apply_x
        ypos (apply_y + 31)
        xysize (80, 26)
        background ui_img("cfgw_cancel")
        hover_background ui_img("cfgw_cancel_hover")
        action Function(cfg_color_revert)


## ---------------------------------------------------------------------
##  文本 / TEXT CONFIG
## ---------------------------------------------------------------------
screen cfg_page_text():
    $ _det = cfg_get("auto_detail")
    $ _lang = ui_lang()

    # 文本的显示速度
    use cfg_bar(Preference("text speed"), 184, 161, 316, (122, 158), (541, 158))
    use cfg_cb("text_instant", 321, 198, False)

    # 显示样本
    text CFG_SAMPLE.get(_lang, "巧可甜"):
        xpos 300
        ypos 229
        size 29
        font ui_font
        color cfg_color_hex("normal")
        outlines [(1, "#3a210f", 0, 0)]

    button:
        xpos 537
        ypos 235
        xysize (80, 26)
        background ui_img("cfgw_font")
        hover_background ui_img("cfgw_font_hover")
        action NullAction()

    # 使用自动模式的详细设定（关闭时子块整体 30% 透明）
    use cfg_cb("auto_detail", 81, 303)
    use cfg_bar(FieldValue(persistent, "cfg_auto_char", 0.65), 184, 401, 316, (122, 398), (541, 398), not _det)
    use cfg_cb("auto_char_instant", 321, 438, False)
    use cfg_bar(FieldValue(persistent, "cfg_auto_wait", 0.5), 184, 521, 316, (122, 518), (541, 518), not _det)

    use cfg_cb("auto_after_choice", 81, 583)

    # 选择字体颜色
    # 色块：选中项画 3px 橙圈（内填 65x65），未选中画 1px 深棕细圈（内填 69x69）。
    use cfg_swatch("normal", 683, 182)
    use cfg_swatch("read", 793, 182)

    use cfg_picker(914, 166, 1114, 247, 318, (985, 1075, 1154))

    use cfg_cb("font_common", 688, 291, False)

    use cfg_cb("click_next", 682, 353)
    use cfg_cb("seen_instant", 682, 403)
    use cfg_cb("skip_seen_instant", 682, 453)
    use cfg_cb("skip_after_choice", 682, 503)
    use cfg_cb("skip_unread", 682, 553)
    # 手机版没有右键：「将解除自动模式设定为单击右键」已从美术中裁掉。


## ---------------------------------------------------------------------
##  游戏 / GAME CONFIG
## ---------------------------------------------------------------------
screen cfg_page_game():
    # 手机版：设定窗口模式 / 设定分辨率 / 图片插值方式 三块，以及
    # 单击右键进行系统界面切换 / 将空格与回车作用统一 / 自动追踪鼠标，
    # 在手机上都没有实际效果，已连同美术一起裁掉（见 _tools 的 MOBILE_TRIM），
    # 保留下来的项整体上移补齐版面。

    # 消息窗口不透明率
    use cfg_bar(FieldValue(persistent, "cfg_window_opacity", 1.0), 184, 190, 316, (122, 187), (541, 187))

    # 左栏：显示特效（连同 5 个子项，从右栏搬过来平衡版面）
    use cfg_cb("fx", 77, 233)
    use cfg_cb("fx_big", 144, 283, False)
    use cfg_cb("fx_small", 324, 283, False)
    use cfg_cb("fx_ui", 144, 308, False)
    use cfg_cb("fx_sys", 324, 308, False)
    use cfg_cb("fx_anim", 504, 308, False)

    # 右栏：显示信息 / 扩大显示 / 显示确认窗口（+10 个子项）
    use cfg_cb("show_info", 682, 123)
    use cfg_cb("zoom_ui", 682, 163)
    use cfg_cb("confirm", 682, 203)

    # 确认窗口的 10 个子项：美术里的行距被拉开到 60px
    # （_tools/spread_game_subitems.py 直接改烘焙图），
    # 所以这里的 y 也跟着走 263 / 323 / 383 / 443 / 503。
    use cfg_cb("cf_overwrite", 749, 263, False)
    use cfg_cb("cf_copy", 929, 263, False)
    use cfg_cb("cf_delete", 749, 323, False)
    use cfg_cb("cf_load", 929, 323, False)
    use cfg_cb("cf_return", 749, 383, False)
    use cfg_cb("cf_quickjump", 929, 383, False)
    use cfg_cb("cf_resetcfg", 749, 443, False)
    use cfg_cb("cf_apply", 929, 443, False)
    use cfg_cb("cf_title", 749, 503, False)
    use cfg_cb("cf_quit", 929, 503, False)

    # 语言 / 版本：原版没有这两项（语言在主菜单、版本是启动项），
    # 手机版把入口收进这里。行带、✳ 图标、15x15 方框都是烘焙素材，
    # 由 _tools/bake_config_extra.py 从本页美术里裁出，相位与本页一致，
    # 所以贴上去与上面几条烘焙行看起来是同一块底纹。
    # 行距 80 而不是 40：左栏烘焙内容只到 y=338，这样两行能压到面板
    # 下半部，底部不至于空出一大片。
    add ui_img("cfgw_band_l") xpos 61 ypos 400
    add ui_img("cfgw_star_l") xpos 71 ypos 400
    text U("language") xpos 103 ypos 402 size 18 font ui_font color "#482e1e" outlines []

    use cfg_pick(Function(cfg_set_lang, "sc"), "简体中文", 210, 407, cfg_lang_sel() == "sc")
    use cfg_pick(Function(cfg_set_lang, "tc"), "繁體中文", 340, 407, cfg_lang_sel() == "tc")
    use cfg_pick(Function(cfg_set_lang, "jp"), "日本語", 470, 407, cfg_lang_sel() == "jp")

    add ui_img("cfgw_band_l") xpos 61 ypos 480
    add ui_img("cfgw_star_l") xpos 71 ypos 480
    text U("edition") xpos 103 ypos 482 size 18 font ui_font color "#482e1e" outlines []

    use cfg_pick(Function(cfg_set_edition, True), U("full_version"), 210, 487, cfg_edition_sel())
    use cfg_pick(Function(cfg_set_edition, False), U("all_ages"), 430, 487, not cfg_edition_sel())


## ---------------------------------------------------------------------
##  声音&角色 / SOUND & CHARACTER CONFIG
## ---------------------------------------------------------------------
screen cfg_page_sound():
    use cfg_bar(CfgAllVolume(), 175, 164, 316, (113, 161), (532, 161))
    use cfg_cb("mute_master", 466, 198, False)

    use cfg_bar(Preference("music volume"), 175, 264, 316, (113, 261), (532, 261))
    use cfg_cb("mute_bgm", 466, 298, False)

    use cfg_bar(Preference("sound volume"), 175, 364, 316, (113, 361), (532, 361))
    use cfg_cb("mute_se", 466, 398, False)

    use cfg_bar(Preference("voice volume"), 175, 464, 316, (113, 461), (532, 461))
    use cfg_cb("mute_voice", 466, 498, False)

    use cfg_cb("voice_duck", 81, 523)
    use cfg_cb("voice_text", 81, 563)
    use cfg_cb("voice_stop_page", 81, 603)

    # 角色个别设定
    add ui_img("cfgw_ph_circle") xpos 713 ypos 255
    add ui_img("cfgw_ph_rect") xpos 708 ypos 368

    button:
        xpos 856
        ypos 175
        xysize (88, 31)
        background ui_img("cfgw_snd_on")
        hover_background ui_img("cfgw_snd_on_hover")
        action NullAction()

    button:
        xpos 984
        ypos 175
        xysize (88, 31)
        background ui_img("cfgw_snd_off")
        hover_background ui_img("cfgw_snd_off_hover")
        action NullAction()

    use cfg_bar(CfgCharVolume(), 904, 225, 247,
                (842, 222), (1181, 222), maxdim=True)

    use cfg_radio("char_sel", "miku", 855, 272, sel="orange")
    use cfg_radio("char_sel", "chieri", 1035, 272, sel="orange")
    use cfg_radio("char_sel", "ichigo", 855, 298, sel="orange")
    use cfg_radio("char_sel", "nana", 1035, 298, sel="orange")
    use cfg_radio("char_sel", "other_m", 855, 324, sel="orange")
    use cfg_radio("char_sel", "other_f", 1035, 324, sel="orange")

    use cfg_cb("char_color_unify", 855, 376, False)

    button:
        xpos 855
        ypos 488
        xysize (71, 71)
        background None
        action Function(cfg_set_target, "char")
        add Solid(cfg_color_hex("char") or "#ffffff") xpos 3 ypos 3 xysize (65, 65)
        add ui_img("cfgw_sw_sel" if cfg_target() == "char" else "cfgw_sw_unsel")

    # 声音页的读数位置比文本页靠右（本页的「色相/亮度/饱和度」标签烘焙在
    # x=947/1037/1127，参考图的数字分别收在 1009/1099/1178 处）。
    use cfg_picker(941, 442, 1141, 523, 594, (1010, 1100, 1179))


## ---------------------------------------------------------------------
##  确认窗
##  统一用 screens.rpy 里的 screen confirm（和存读档、退出游戏同一套美术、
##  同一套按钮），这里不再自己画一个，避免同一个游戏出现两种确认对话框。
## ---------------------------------------------------------------------


## ---------------------------------------------------------------------
##  底部导航 + 右上两枚按钮（整层美术里已有，这里只补热区）
## ---------------------------------------------------------------------
screen cfg_nav():
    $ _nav = ui_boxes("menu_nav")
    $ _bottom = _nav[-6:]
    $ _acts = [
        ShowMenu("save"),
        ShowMenu("load"),
        ShowMenu("preferences"),
        Return(),
        MainMenu(confirm=cfg_confirm_on("cf_title")),
        Quit(confirm=cfg_confirm_on("cf_quit")),
    ]

    for _i in range(min(6, len(_bottom))):
        $ _b = _bottom[_i]
        imagebutton:
            xpos _b[0]
            ypos _b[1]
            idle Null(_b[2] - _b[0], _b[3] - _b[1])
            hover ui_crop("menu_nav_hover", _b)
            # 有未反映的改动时离开，先弹确认窗；确认后丢弃改动再走。
            action Function(cfg_leave, _acts[_i])

    imagebutton:
        xpos 946
        ypos 33
        idle Null(130, 40)
        hover Null(130, 40)
        action Function(cfg_ask_apply)

    imagebutton:
        xpos 1092
        ypos 33
        idle Null(130, 40)
        hover Null(130, 40)
        # 「初始化」只有在改动过之后才可按（未改动时整块是压暗的）。
        action Function(cfg_ask_reset)


## ---------------------------------------------------------------------
##  入口
## ---------------------------------------------------------------------
screen preferences(page=None):
    tag menu
    modal True

    # 进来时记一份回滚点：所有改动先暂存，按「反映设定内容」才生效。
    on "show" action Function(cfg_begin)
    on "replace" action Function(cfg_begin)

    $ _page = (page if page in CFG_TAB_ORDER else
               (persistent.cfg_page if persistent.cfg_page in CFG_TAB_ORDER else "text"))

    # 页图层整张使用：原版「使用自动模式的详细设定」未勾选时，
    # 烘焙进美术的轨道/文字/方框**不淡出**，只有运行时绘制的
    # 拇指与 MIN/MAX 菱形按 30% alpha 画（见 cfg_bar 的 dim 参数）。
    add ui_img("cfg_" + _page)

    add ui_img("cfg_navbar")
    add ui_img("cfgw_tab_" + _page) xpos CFG_TAB_X[_page] ypos 27

    if _page == "text":
        use cfg_page_text
    elif _page == "game":
        use cfg_page_game
    else:
        use cfg_page_sound

    use cfg_nav

    if not cfg_dirty():
        add ui_img("cfgw_topdim") xpos 946 ypos 33

    for _t in CFG_TAB_ORDER:
        if _t != _page:
            imagebutton:
                xpos CFG_TAB_X[_t]
                ypos 27
                idle Null(CFG_TAB_W[_t], 45)
                action Function(cfg_set_page, _t)
