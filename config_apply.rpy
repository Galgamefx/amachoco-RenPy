###########################################################################
# 系统设定的「生效层」
#
# 界面里点一下，只改 persistent.cfg_*，那只是「玩家的意愿」。这一层负责把
# 意愿翻译成 Ren'Py 真正会去读的开关（preferences / config / mixer mute /
# say 屏幕的颜色与速度），否则复选框画得再像，引擎那边也不会有任何变化。
#
# 调用时机：
#   * init / after_load / start：把上次留下的设定重新推给引擎；
#   * cfg_set / cfg_toggle 等改动函数：立刻生效（界面是「即时预览」模型）；
#   * 每次交互开始（interact_callbacks）：兜住拖滑条这类不经过 cfg_set 的改动。
###########################################################################

init -2 python:

    CFG_MIXER_KEYS = (("music", "mute_bgm"), ("sound", "mute_se"), ("voice", "mute_voice"))

    CFG_DEFAULT_TEXT_COLOR = "#fffaf0"

    def cfg_float(attr, default):
        v = getattr(persistent, attr, None)
        try:
            return float(v) if v is not None else float(default)
        except (TypeError, ValueError):
            return float(default)

    # ---- 消息窗口不透明率 -------------------------------------------
    def cfg_opacity():
        """0.0~1.00；原版的「消息窗口不透明率」滑条。"""
        return max(0.0, min(1.0, cfg_float("cfg_window_opacity", 1.0)))

    def cfg_opacity_two():
        """0.30~1.00；原版的「消息窗口不透明率」滑条。"""
        return max(0.30, min(1.0, cfg_float("cfg_window_opacity", 1.0)))

    # ---- 自动模式 ---------------------------------------------------
    def cfg_auto_characters():
        """「1 个文字的速度」→ config.afm_characters（每单位时间走多少个字）。

        原版滑条往右＝每个字停留更久＝更慢，所以这里取反。
        """
        v = max(0.0, min(1.0, cfg_float("cfg_auto_char", 0.65)))
        return int(round(560 - 480 * v))

    def cfg_auto_wait():
        """「文本显示后的等待时间」→ preferences.afm_time（秒）。"""
        return round(0.5 + 18.0 * max(0.0, min(1.0, cfg_float("cfg_auto_wait", 0.5))), 2)

    def cfg_text_instant():
        """整句立刻显示：总开关，或自动模式下子块里的那个开关。"""
        if cfg_get("text_instant"):
            return True
        return bool(preferences.afm_enable
                    and cfg_get("auto_detail") and cfg_get("auto_char_instant"))

    def cfg_say_cps():
        """say 屏幕的 slow_cps：None＝沿用「文本的显示速度」，0＝瞬间。"""
        return 0 if cfg_text_instant() else None

    # ---- 已读判定（「将已读文本瞬间显示」要用） ----------------------
    def cfg_seen_line(text):
        s = persistent.cfg_seen_lines
        return bool(s) and bool(text) and (text in s)

    def cfg_mark_seen(text):
        if not text:
            return
        s = persistent.cfg_seen_lines
        if s is None:
            s = set()
        if text in s:
            return
        s.add(text)
        # 只留最近的一批，别让 persistent 无限长大。
        if len(s) > 4000:
            s = set(sorted(s)[-2000:])
        persistent.cfg_seen_lines = s

    # ---- 文本颜色 ---------------------------------------------------
    def cfg_read_color_hex():
        """已读文本的颜色；勾了「将字体颜色共通」就跟着通常色走。"""
        if cfg_get("font_common"):
            return persistent.cfg_text_color or CFG_DEFAULT_TEXT_COLOR
        return (persistent.cfg_read_color
                or persistent.cfg_text_color
                or CFG_DEFAULT_TEXT_COLOR)

    def cfg_say_color(seen=False):
        if seen:
            return cfg_read_color_hex()
        if cfg_get("char_color_unify") and persistent.cfg_char_color:
            return persistent.cfg_char_color
        return persistent.cfg_text_color or CFG_DEFAULT_TEXT_COLOR

    # ---- 确认窗口 ---------------------------------------------------
    def cfg_confirm_on(key):
        """某个确认窗口该不该弹：总开关 + 单项开关。"""
        if not cfg_get("confirm"):
            return False
        return bool(cfg_get(key))

    # ---- 转场（显示特效） --------------------------------------------
    def cfg_transition_level():
        """2＝全部转场；1＝只留默认转场；0＝不转场。"""
        if not cfg_get("fx"):
            return 0
        for k in ("fx_big", "fx_small", "fx_ui", "fx_sys", "fx_anim"):
            if not cfg_get(k):
                return 1
        return 2

    # ---- 语音：按角色分组调音量 --------------------------------------
    # 语音文件名自带角色前缀（audio/voice/<prefix>_a000001.ogg），所以
    # 「角色个别设定」可以直接按前缀把该角色的语音音量乘上去，不用改脚本。
    CFG_CHAR_PREFIX = {
        "miku": "mik",      # 美久栗
        "chieri": "chi",    # 千绘莉
        "ichigo": "ich",    # 莓华
        "nana": "nan",      # 娜娜
        "other_m": "mob",   # 其他男性
        "other_f": "mob2",  # 其他女性（本作无语音文件，留着占位）
    }

    def cfg_char_volumes():
        d = persistent.cfg_char_volumes
        return d if isinstance(d, dict) else {}

    def cfg_char_sel():
        v = cfg_get("char_sel", "other_m")
        return v if v in CFG_CHAR_PREFIX else "other_m"

    def cfg_char_vol(name=None):
        name = name or cfg_char_sel()
        try:
            return max(0.0, min(1.0, float(cfg_char_volumes().get(name, 1.0))))
        except (TypeError, ValueError):
            return 1.0

    def cfg_set_char_vol(name, value):
        if name not in CFG_CHAR_PREFIX:
            name = cfg_char_sel()
        d = dict(cfg_char_volumes())
        d[name] = max(0.0, min(1.0, float(value)))
        persistent.cfg_char_volumes = d
        persistent.cfg_dirty = True

    def cfg_voice_factor():
        """当前播的语音属于哪个角色，就用那个角色的个别音量。"""
        cur = (renpy.music.get_playing("voice") or "").replace("\\", "/")
        pre = cur.rsplit("/", 1)[-1].split("_", 1)[0]
        for key, pfx in CFG_CHAR_PREFIX.items():
            if pfx == pre:
                return cfg_char_vol(key)
        return 1.0

    _CFG_VOICE_SIG = {"sig": None}

    def cfg_sync_voice_volume():
        cur = renpy.music.get_playing("voice") or ""
        f = cfg_voice_factor()
        sig = (cur, round(f, 3))
        if _CFG_VOICE_SIG["sig"] == sig:
            return
        _CFG_VOICE_SIG["sig"] = sig
        try:
            renpy.music.set_volume(f, delay=0, channel="voice")
        except Exception:
            pass

    # ---- 一次性把全部设定推给引擎 ------------------------------------
    def apply_cfg():
        # 静音：总开关压住各分项
        master = bool(cfg_get("mute_master"))
        for mixer, key in CFG_MIXER_KEYS:
            want = bool(master or cfg_get(key))
            if preferences.mute.get(mixer) != want:
                preferences.mute[mixer] = want

        # 自动模式
        if cfg_get("auto_detail"):
            chars, wait = cfg_auto_characters(), cfg_auto_wait()
        else:
            chars, wait = 250, 15.0
        if config.afm_characters != chars:
            config.afm_characters = chars
        if abs(float(preferences.afm_time) - wait) > 0.001:
            preferences.afm_time = wait

        # 快进
        preferences.skip_unseen = bool(cfg_get("skip_unread"))
        preferences.skip_after_choices = bool(cfg_get("skip_after_choice"))

        # 语音
        preferences.emphasize_audio = bool(cfg_get("voice_duck"))
        preferences.wait_voice = bool(cfg_get("voice_stop_page"))

        # 语音：角色个别音量（按语音文件名前缀）
        cfg_sync_voice_volume()

        # 「点击进入下一页」：关掉时鼠标左键不再推进对话，键盘仍可。
        km = config.keymap["dismiss"]
        want_click = bool(cfg_get("click_next"))
        has_click = "mousedown_1" in km
        if want_click != has_click:
            for k in ("mousedown_1", "mouseup_1"):
                while k in km:
                    km.remove(k)
            if want_click:
                km.extend(["mousedown_1", "mouseup_1"])

        # 「将已读文本瞬间显示」：跳过时不再等 skip_delay，已读文本一闪而过。
        want_delay = 0 if cfg_get("skip_seen_instant") else 75
        if config.skip_delay != want_delay:
            config.skip_delay = want_delay

        # 显示特效
        lvl = cfg_transition_level()
        if preferences.transitions != lvl:
            preferences.transitions = lvl

    # 记录上一次推给引擎的值，避免每帧都写（写得太频繁会让画面不停重启）。
    _CFG_LAST = {"chars": None, "wait": None, "mute": None, "skip": None,
                 "voice": None, "trans": None}

    def apply_cfg_throttled():
        """interact 回调里用的轻量版：只有在设定真的变了才重新推一遍。"""
        sig = (config.afm_characters, round(float(preferences.afm_time), 3),
               tuple(sorted(preferences.mute.items(), key=lambda kv: str(kv[0]))),
               bool(preferences.skip_unseen), bool(preferences.skip_after_choices),
               bool(preferences.emphasize_audio), bool(preferences.wait_voice),
               int(preferences.transitions), int(config.skip_delay),
               "mousedown_1" in config.keymap["dismiss"],
               tuple(sorted(cfg_char_volumes().items())))
        mut = (bool(cfg_get("mute_master")), bool(cfg_get("mute_bgm")),
               bool(cfg_get("mute_se")), bool(cfg_get("mute_voice")),
               bool(cfg_get("skip_unread")), bool(cfg_get("skip_after_choice")),
               bool(cfg_get("voice_duck")), bool(cfg_get("voice_stop_page")),
               bool(cfg_get("click_next")), bool(cfg_get("skip_seen_instant")),
               bool(cfg_get("auto_detail")),
               round(cfg_float("cfg_auto_char", 0.65), 3),
               round(cfg_float("cfg_auto_wait", 0.5), 3),
               int(cfg_transition_level()))
        # 「在选项选择完毕后继续进行自动模式」：选项窗关掉时若没开这个开关，
        # 就顺手把自动模式停掉（开着则保持，Ren'Py 本身不会主动停）。
        _has_choice = renpy.get_screen("choice") is not None
        if _CFG_LAST.get("choice") and not _has_choice:
            if not cfg_get("auto_after_choice") and preferences.afm_enable:
                preferences.afm_enable = False
        _CFG_LAST["choice"] = _has_choice

        if _CFG_LAST.get("want") == mut:
            return
        _CFG_LAST["want"] = mut
        apply_cfg()

    config.interact_callbacks.append(apply_cfg_throttled)
    config.after_load_callbacks.append(apply_cfg)
    config.start_callbacks.append(apply_cfg)

default persistent.cfg_seen_lines = None
default persistent.cfg_auto_char = 0.65
