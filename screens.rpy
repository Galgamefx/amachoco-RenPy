default quick_menu = True

init -1 python:
    ui_font = FontGroup()
    ui_font.add("DejaVuSans.ttf", 0x266A, 0x266A)
    ui_font.add("fonts/msyh.ttc", 0x0000, 0xFFFF)

    def ui_text_style():
        return dict(font=ui_font, size=24, color="#fff8ea")

    def cg_view_target(group, name):
        return Show("cg_viewer", group=group, cg=name)

    def open_cg(group):
        name = group_first_unlocked(group)
        if name:
            renpy.show_screen("cg_viewer", group=group, cg=name)
style default:
    font ui_font
    size 24
    color "#ffffff"

style button_text:
    font ui_font
    size 24
    color "#ffffff"
    hover_color "#ffd9a0"

style say_dialogue:
    font ui_font
    size 25
    color "#fff8ea"

style say_label:
    font ui_font
    size 22
    color "#fff3d6"

###########################################################################
# In-game message window (baked BGI window + name plate)
###########################################################################
screen say(who, what):
    # The original BACK LOG is a full screen window: the message box and the
    # quick menu row are not visible behind it.  Those live in this screen,
    # so they are skipped while the log is on screen and come back as soon
    # as it closes (this screen stays shown the whole time).
    if renpy.get_screen("history") is None:
        window:
            id "window"
            background None
            xfill True
            yfill False

            # 「系统设定」里的这几项要真的生效，所以颜色 / 速度 / 不透明率
            # 都在这里现算（详见 config_apply.rpy）。
            $ store._last_line = renpy.substitute(what or "")
            $ store._last_who = renpy.substitute(who or "")
            $ _cfg_was_seen = cfg_seen_line(store._last_line)
            $ cfg_mark_seen(store._last_line)
            $ _cfg_cps = 0 if (_cfg_was_seen and cfg_get("seen_instant")) else cfg_say_cps()
            $ _cfg_color = cfg_say_color(_cfg_was_seen)
            $ _cfg_alpha = cfg_opacity()
            $ _cfg_alpha_two = cfg_opacity_two()
            # 「扩大显示」：打开时文本区用满宽度，关闭时收窄（默认开着＝原来的版面）。
            $ _cfg_xsize = 1000 if cfg_get("zoom_ui") else 860
            # 「播放语音时显示文本」：关掉时语音播放期间不显示文字。
            $ _cfg_vshow = cfg_get("voice_text") or not renpy.music.get_playing("voice")

            add "ui/msgbg.png" xpos -7 ypos 535 alpha _cfg_alpha
            if who:
                add "ui/nameplate610000.png" xpos 160 ypos 495 alpha _cfg_alpha
                text who:
                    id "who"
                    xpos 240 ypos 500
                    color "#ffffff"
                    outlines [(1, "#3a210f", 0, 0)]
            if _cfg_vshow:
                text what:
                    id "what"
                    xpos 130 ypos 570
                    xsize _cfg_xsize
                    line_spacing 6
                    color _cfg_color
                    slow_cps _cfg_cps
                    outlines [(2, "#2b1608", 0, 0)]
        if quick_menu and cfg_get("show_info"):
            add "ui/quickmenu.png" xpos 400 ypos 680 zoom 1.5 alpha _cfg_alpha_two
            button:
                xpos 397 ypos 678
                xysize (74, 40)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("save")
            button:
                xpos 475 ypos 678
                xysize (74, 40)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("load")
            button:
                xpos 550 ypos 678
                xysize (96, 40)
                background None
                hover_background Solid("#ffffff26")
                action QuickSave()
            button:
                xpos 645 ypos 678
                xysize (96, 40)
                background None
                hover_background Solid("#ffffff26")
                action QuickLoad()
            button:
                xpos 740 ypos 678
                xysize (105, 40)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("preferences")
            button:
                xpos 857 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action Preference("auto-forward", "toggle")
            button:
                xpos 899 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action Skip()
            button:
                xpos 941 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action VoiceReplay()
            button:
                xpos 983 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("history")
            button:
                xpos 1025 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("history")
            button:
                xpos 1067 ypos 678
                xysize (40, 40)
                background None
                hover_background Solid("#ffffff26")
                action HideInterface()

style quick_button:
    background None
    hover_background Solid("#ffffff2a")
    padding (6, 2)

style quick_button_text:
    size 19
    color "#ffeacb"
    hover_color "#ffffff"
    font ui_font

###########################################################################
# Choices
###########################################################################
screen choice(items):
    style_prefix "choice"
    vbox:
        xpos 243
        yalign 0.5
        spacing 12
        for i in items:
            button:
                xysize (793, 55)
                background ui_img("choice")
                hover_background ui_img("choice_hover")
                action i.action
                text i.caption:
                    xalign 0.5
                    yalign 0.5
                    size 26
                    color "#ffeacb"
                    hover_color "#ffffff"
                    font ui_font

###########################################################################
# Title screen
###########################################################################
screen main_menu():
    tag menu
    add ui_img("title_art")
    $ boxes = ui_boxes("title_buttons")
    $ acts = [
        Continue(),
        Start(),
        ShowMenu("load"),
        ShowMenu("gallery"),
        If(bgi_global(310) == 1, Start("ac_03harem"), Notify(U("locked"))),
        ShowMenu("preferences"),
        Quit(confirm=False),
    ]
    for i in range(min(len(boxes), len(acts))):
        $ box = boxes[i]
        imagebutton:
            idle ui_crop("title_buttons", box)
            hover ui_crop("title_buttons_hover", box)
            xpos box[0]
            ypos box[1]
            action acts[i]
    hbox:
        xpos 20
        ypos 16
        spacing 10
        textbutton "简体中文" action Function(set_lang, "sc") style "lang_button"
        textbutton "繁體中文" action Function(set_lang, "tc") style "lang_button"
        textbutton "日本語" action Function(set_lang, "jp") style "lang_button"
    text U("version_tag"):
        xpos 1180
        ypos 40
        size 18
        color "#ffeacb"
        outlines [(1, "#4a2c14", 0, 0)]

style lang_button:
    background "#00000066"
    hover_background "#8a5a3a"
    padding (8, 2)

style lang_button_text:
    size 18
    font ui_font
    color "#ffeacb"
    hover_color "#ffffff"

###########################################################################
# Game menu chrome (baked navigation bar)
###########################################################################
screen menu_nav():
    add ui_crop("menu_nav", [0, 640, 1280, 706]) xpos 0 ypos 640
    $ nav = ui_boxes("menu_nav")
    # The sc/tc chrome also has four tiny slider boxes between the icon
    # column and the top-right pair, so the Japanese sheet (12 boxes) and
    # the Chinese sheets (15 boxes) do not share indices. The six bottom
    # buttons are always the last six and the top-right pair is 3:5.
    if len(nav) >= 12:
        $ bottom = nav[-6:]
        $ top = nav[3:5]
        for i in range(6):
            $ b = bottom[i]
            imagebutton:
                idle ui_crop("menu_nav", b)
                hover ui_crop("menu_nav_hover", b)
                xpos b[0]
                ypos b[1]
                action [
                    ShowMenu("save"), ShowMenu("load"), ShowMenu("preferences"),
                    Return(), MainMenu(confirm=True), Quit(confirm=True),
                ][i]
        imagebutton:
            idle ui_crop("menu_nav", top[0])
            hover ui_crop("menu_nav_hover", top[0])
            xpos top[0][0]
            ypos top[0][1]
            action ShowMenu("preferences")
        imagebutton:
            idle ui_crop("menu_nav", top[1])
            hover ui_crop("menu_nav_hover", top[1])
            xpos top[1][0]
            ypos top[1][1]
            action Confirm(U("reset_confirm"), Function(reset_persistent_flags), NullAction())

init python:
    def slot_timestamp(mt):
        import time
        return time.strftime("%Y.%m.%d.%H.%M", time.localtime(mt))

    def reset_persistent_flags():
        persistent.bgi_flags = {}
        persistent.cg_unlocked = []
        persistent.bgm_unlocked = []
        renpy.restart_interaction()
        renpy.notify(U("initialized"))

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    add Solid("#12100f")
    frame:
        background Solid("#1b1714")
        xpos 40
        ypos 88
        xsize 1200
        ysize 540
        padding (24, 18)
        vbox:
            spacing 12
            text title size 30 color "#ffe0a8"
            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    mousewheel True
                    draggable True
                    ymaximum 470
                    vbox:
                        spacing 6
                        transclude
            else:
                transclude
    use menu_nav

###########################################################################
# Save / load
###########################################################################
screen save():
    tag menu
    use file_slots("save")

screen load():
    tag menu
    use file_slots("load")

screen file_slots(mode):
    add ui_img("save_bg" if mode == "save" else "load_bg")
    $ tb = ui_boxes("save_toolbar")
    $ page = min(8, max(1, persistent.save_page or 1))
    $ xs = [62, 301, 540, 779, 1018]
    $ ys = [154, 421]
    # screenshots sit *under* the card artwork, visible through its holes
    for i in range(10):
        $ slot = "%d-%d" % (page, i + 1)
        if renpy.slot_mtime(slot):
            add FileScreenshot(slot, slot=True):
                xpos xs[i % 5]
                ypos ys[i // 5]
                xysize (199, 110)
    add "ui/save_grid.png"
    # invisible click targets over the card interiors
    for i in range(10):
        $ slot = "%d-%d" % (page, i + 1)
        $ sx = xs[i % 5] - 8
        $ sy = (ys[i // 5] - 38)
        button:
            xpos sx
            ypos sy
            xysize (215, 253)
            background None
            hover_background Solid("#ffffff18")
            action (FileSave(slot, confirm=(renpy.slot_mtime(slot) is not None), slot=True) if mode == "save" else FileLoad(slot, confirm=True, slot=True))
    # empty slot placeholder art (the game logo, as in the original)
    for i in range(10):
        $ slot = "%d-%d" % (page, i + 1)
        if not renpy.slot_mtime(slot):
            add ui_img("save_empty"):
                xpos xs[i % 5] + 4
                ypos ys[i // 5] + 6
                xysize (191, 105)
    # slot labels: date on the card's title bar, dialogue line under the photo
    for i in range(10):
        $ slot = "%d-%d" % (page, i + 1)
        $ lx = xs[i % 5] - 8
        $ ly = ys[i // 5] - 38
        $ mt = renpy.slot_mtime(slot)
        if mt:
            text slot_timestamp(mt):
                xpos lx + 54
                ypos ly + 8
                xsize 155
                size 15
                color "#4a3128"
                font ui_font
            $ line = FileJson(slot, "line", empty="", slot=True)
            $ who = FileJson(slot, "who", empty="", slot=True)
            if line:
                if line.startswith(u"\u300c") or line.startswith(u"\u201c"):
                    $ shown_line = line
                else:
                    $ shown_line = u"\u300c%s\u300d" % line
                text shown_line:
                    xpos lx + 8
                    ypos ly + 156
                    xsize 199
                    size 15
                    line_spacing 2
                    text_align 0.5
                    color "#4a3128"
                    font ui_font
    add ui_crop("save_toolbar", [0, 0, 1280, 92])
    # page tabs: the eight numbered circles baked into the toolbar art
    if len(tb) >= 8:
        for i in range(8):
            $ b = tb[i]
            button:
                xpos b[0]
                ypos b[1]
                xysize (b[2] - b[0], b[3] - b[1])
                background None
                hover_background Solid("#ffffff30")
                action SetVariable("persistent.save_page", i + 1)
    # toolbar buttons: save / load / copy / delete
    if len(tb) >= 12:
        for i in range(4):
            $ b = tb[8 + i]
            imagebutton:
                idle ui_crop("save_toolbar", b)
                hover ui_crop("save_toolbar_hover", b)
                xpos b[0]
                ypos b[1]
                action [ShowMenu("save"), ShowMenu("load"),
                        Function(renpy.notify, U("copied")),
                        Function(renpy.notify, U("deleted"))][i]
    # bottom command bar (same art as the in-game menu bar)
    add ui_crop("menu_nav", [0, 640, 1280, 706]) xpos 0 ypos 640
    $ nav = ui_boxes("menu_nav")
    if len(nav) >= 12:
        $ bottom = nav[-6:]
        for i in range(6):
            $ b = bottom[i]
            imagebutton:
                idle ui_crop("menu_nav", b)
                hover ui_crop("menu_nav_hover", b)
                xpos b[0]
                ypos b[1]
                action [ShowMenu("save"), ShowMenu("load"), ShowMenu("preferences"),
                        Return(), MainMenu(confirm=True), Quit(confirm=True)][i]

style tab_button:
    background "#2a211b"
    hover_background "#8a5a3a"
    padding (14, 4)

style tab_button_text:
    size 20
    font ui_font
    color "#ffeacb"
    hover_color "#ffffff"

style page_button:
    background "#2a211b"
    hover_background "#8a5a3a"
    padding (8, 3)

style page_button_text:
    size 18
    font ui_font
    color "#ffeacb"
    hover_color "#ffffff"

style opt_button:
    background "#3a2c22"
    hover_background "#8a5a3a"
    padding (10, 3)

style opt_button_text:
    size 20
    font ui_font
    color "#ffeacb"
    hover_color "#ffffff"

###########################################################################
# History / BACK LOG
###########################################################################
# Geometry taken from the original log window (1280x720 base):
#   four slots, slot height 159, first slot top 36, so the dotted rules baked
#   into history_bg (y = 195/354/513/672) close every slot.
#   The numbers below are the layout origins; the 1px outline adds one more
#   pixel, so the measured ink lands at x 137 / y top+78 (slot 0: 120..146),
#   which is what the original screenshot shows.
#   A speaker's paw plate sits at (128, top+10), the name ink at (184, top+24);
#   the Q.Jump capsule of a slot sits at (1056, top+34).
init -1 python:
    LOG_SLOT_H = 159
    LOG_SLOT_TOP = 36
    LOG_SLOTS = 4
    LOG_TEXT_X = 135
    LOG_TEXT_W = 1008
    LOG_TEXT_DY = 76
    LOG_PLATE_X = 128
    LOG_PLATE_DY = 10
    LOG_NAME_X = 182
    LOG_NAME_DY = 16
    LOG_QJUMP_X = 1056
    LOG_QJUMP_DY = 34
    # The Voice capsule sits on the same line as Q.Jump, just to its left, and
    # only on entries that actually carry a voice clip.
    LOG_VOICE_X = 958
    LOG_VOICE_DY = 34
    # scrollbar groove measured from history_bg: y 170..558, thumb 28px tall
    LOG_TRACK_TOP = 170
    LOG_TRACK_TRAVEL = 369

    def log_plain(s):
        """Drop text tags; the log window uses one fixed size for everything."""
        if not s:
            return u""
        try:
            return renpy.filter_text_tags(s, allow=set())
        except Exception:
            return s

    def log_voice_file(h):
        """Voice clip attached to a history entry, or None.

        Ren'Py's 00voice.rpy installs _voice_history_callback, which stores a
        VoiceInfo on every entry as h.voice; its .filename is the path that was
        handed to the `voice` statement, already in loadable form.
        """
        vi = getattr(h, "voice", None)
        fn = getattr(vi, "filename", None) if vi is not None else None
        if fn and renpy.loadable(fn):
            return fn
        return None

    # Back Log replay needs its own channel: 00voice.rpy's voice_interact() stops
    # the "voice" channel on every interaction that happens inside a game menu
    # (unless the player turned on voice_after_game_menu), so a clip started from
    # the log would be cut off on the very next interaction. A separate channel
    # shares the voice mixer/volume but is invisible to that logic.
    LOG_VOICE_CHANNEL = "voicelog"

    def log_voice_channel_init():
        """Create the channel. register_channel only works during init, so this
        is called once from the init block below."""
        if not renpy.music.channel_defined(LOG_VOICE_CHANNEL):
            renpy.music.register_channel(
                LOG_VOICE_CHANNEL, mixer="voice", loop=False,
                stop_on_mute=True, synchro_start=False)

    def log_replay_voice(fn):
        """Replay one line's voice clip, replacing whatever is playing."""
        if not fn:
            return
        store._last_voice_play = fn
        renpy.sound.play(fn, channel=LOG_VOICE_CHANNEL, synchro_start=False)
        renpy.restart_interaction()

    def log_voice_stop():
        if renpy.music.channel_defined(LOG_VOICE_CHANNEL):
            renpy.sound.stop(channel=LOG_VOICE_CHANNEL)

    # A clip started from the log is silenced as soon as real dialogue starts a
    # voice of its own, so the two can never talk over each other.
    def _log_voice_callback(event, info, **kwargs):
        if event == "play":
            log_voice_stop()

    # Leaving the log silences the clip however the player got out — the back
    # button, Escape, or a jump straight into another menu screen. Inside the
    # game menu the history screen is not visible to get_screen() (it runs in its
    # own context), so the menu flag keeps it from cutting the clip while the
    # player is still browsing the log.
    def _log_voice_guard():
        # Runs on every interaction, so bail out before touching the mixer
        # unless a replay actually survived to this point.
        if not renpy.music.channel_defined(LOG_VOICE_CHANNEL):
            return
        if not renpy.sound.get_playing(LOG_VOICE_CHANNEL):
            return
        if getattr(renpy.context(), "_menu", False):
            return
        if renpy.get_screen("history") is None:
            renpy.sound.stop(channel=LOG_VOICE_CHANNEL)

    if not any(getattr(c, "__name__", "") == "_log_voice_callback"
               for c in config.voice_callbacks):
        config.voice_callbacks.append(_log_voice_callback)
    if not any(getattr(c, "__name__", "") == "_log_voice_guard"
               for c in config.start_interact_callbacks):
        config.start_interact_callbacks.append(_log_voice_guard)

    log_voice_channel_init()


screen history():
    tag menu
    add ui_img("history_bg")
    add ui_img("log_chrome")

    default log_start = None

    # Leaving the log silences the replayed clip. A screen lifecycle event is
    # used instead of polling renpy.get_screen(), which is not reliable inside
    # the fresh context a game menu runs in.
    on "hide" action Function(log_voice_stop)

    $ _n = len(_history_list)
    $ _max = max(0, _n - LOG_SLOTS)
    $ _start = _max if log_start is None else min(max(0, log_start), _max)

    key "mousedown_4" action SetScreenVariable("log_start", max(0, _start - 1))
    key "mousedown_5" action SetScreenVariable("log_start", min(_max, _start + 1))

    for _k in range(LOG_SLOTS):
        $ _idx = _start + _k
        $ _ry = LOG_SLOT_TOP + LOG_SLOT_H * _k
        if _idx < _n:
            $ _h = _history_list[_idx]
            # The original log window renders every entry at its own fixed
            # size (logwnd sets the font to 28), so per-line {size=...} tags
            # from the script are dropped here instead of being honoured.
            $ _what = log_plain(_h.what)
            $ _who = log_plain(_h.who)

            if _who:
                add ui_img("nameplate610000") xpos LOG_PLATE_X ypos _ry + LOG_PLATE_DY
                text _who:
                    xpos LOG_NAME_X
                    ypos _ry + LOG_NAME_DY
                    size 30
                    font ui_font
                    color "#fdfdfd"
                    outlines [(1, "#3a2320", 0, 0)]
                    substitute False

            # A viewport of the exact slot height clips long lines so text can
            # never bleed past the dotted rule into the next slot.
            viewport:
                xpos LOG_TEXT_X
                ypos _ry + LOG_TEXT_DY
                xsize LOG_TEXT_W
                ysize LOG_SLOT_H - LOG_TEXT_DY - 4
                mousewheel False
                draggable False
                text _what:
                    xsize LOG_TEXT_W
                    size 28
                    line_spacing 6
                    font ui_font
                    color "#fbfbfb"
                    outlines [(1, "#372a20", 0, 0)]
                    substitute False

            # Lines that were voiced get the Voice capsule to the left of
            # Q.Jump; silent lines show nothing there, matching the original.
            $ _vfn = log_voice_file(_h)
            if _vfn:
                imagebutton:
                    idle ui_img("log_voice")
                    hover ui_img("log_voice_hover")
                    xpos LOG_VOICE_X
                    ypos _ry + LOG_VOICE_DY
                    action Function(log_replay_voice, _vfn)

            # Every slot but the newest carries a Q.Jump capsule that rolls
            # back to that line, as the original does.
            if _idx < _n - 1:
                $ _rid = getattr(_h, "rollback_identifier", None)
                imagebutton:
                    idle ui_img("log_qjump")
                    hover ui_img("log_qjump_hover")
                    insensitive ui_img("log_qjump_off")
                    xpos LOG_QJUMP_X
                    ypos _ry + LOG_QJUMP_DY
                    action (RollbackToIdentifier(_rid) if _rid else NullAction())
                    sensitive _rid is not None

    # Scrollbar: up diamond, thumb riding in the groove, down diamond.
    imagebutton:
        idle ui_img("log_updia")
        hover ui_img("log_updia_hover")
        xpos 1172
        ypos 127
        action SetScreenVariable("log_start", max(0, _start - 1))
        sensitive _start > 0

    imagebutton:
        idle ui_img("log_dndia")
        hover ui_img("log_dndia_hover")
        xpos 1172
        ypos 568
        action SetScreenVariable("log_start", min(_max, _start + 1))
        sensitive _start < _max

    if _max > 0:
        $ _frac = float(_start) / _max
    else:
        $ _frac = 1.0
    add ui_img("log_thumb") xpos 1174 ypos int(LOG_TRACK_TOP + LOG_TRACK_TRAVEL * _frac)

    imagebutton:
        idle ui_img("log_back")
        hover ui_img("log_back_hover")
        xpos 994
        ypos 686
        # Stopping the replay here covers the game-menu path, where ending the
        # menu context tears the screen down without a "hide" event.
        action [Function(log_voice_stop), Return()]

###########################################################################
# Gallery / music room / replay
###########################################################################
init 10 python:
    # Omake gallery geometry measured from the original 1280x720 layout:
    # 4x4 cells, 246x139 each, origin (26,73), pitch (267,149).
    GALLERY_CELL = [(26 + 267 * (i % 4), 27 + 149 * (i // 4)) for i in range(16)]
    GALLERY_W, GALLERY_H = 249, 141
    GALLERY_BY_CAT = {0: [], 1: [], 4: [], 5: []}
    for _g in GALLERY_GROUPS:
        _t = _g["thumb"]
        if _t.startswith("AC_tmb_ev1") or _t.startswith("AC_tmb_hv1"):
            GALLERY_BY_CAT[0].append(_g)
        elif _t.startswith("AC_tmb_ev2") or _t.startswith("AC_tmb_hv2"):
            GALLERY_BY_CAT[1].append(_g)
        elif _t.startswith("AC_tmb_hv0") or _t.startswith("AC_tmb_mv"):
            GALLERY_BY_CAT[4].append(_g)
        elif _t.startswith("AC_tmb_bg"):
            GALLERY_BY_CAT[5].append(_g)
    GALLERY_TAB_BOXES = [(1113, 36 + 78 * i, 1280, 100 + 78 * i) for i in range(8)]
    GALLERY_PAGE_BOXES = [(348, 628, 478, 684), (500, 628, 630, 684), (652, 628, 782, 684)]
    GALLERY_EXIT_BOXES = [(784, 683, 939, 718), (944, 683, 1099, 718)]

    def gallery_page_count(cat):
        return max(1, (len(GALLERY_BY_CAT.get(cat, [])) + 15) // 16)

    def play_bgm(name):
        renpy.music.play("audio/bgm/%s.ogg" % name, loop=True)
        store._music_playing = name

    def stop_bgm():
        renpy.music.stop()
        store._music_playing = None

default _music_playing = None

init 10 python:
    def omake_return_title():
        # MainMenu() is a no-op inside the main-menu context (its
        # get_sensitive() returns False there), so go through
        # full_restart() directly.
        renpy.full_restart()

    def play_op_movie():
        renpy.invoke_in_new_context(renpy.movie_cutscene, "movies/op.webm")
        renpy.restart_interaction()

    # SetupForReplay.bss registers exactly these seven recollections and
    # unlocks them through global flags 111/112/113/121/122/123/101.
    REPLAY_FIXED = [
        ("AC_tmb_hv101", "ac_06general_AC_hscene101_a", 111),
        ("AC_tmb_hv103", "ac_06general_AC_hscene102_a", 112),
        ("AC_tmb_hv105", "ac_06general_AC_hscene103_a", 113),
        ("AC_tmb_hv201", "ac_06general_AC_hscene201_a", 121),
        ("AC_tmb_hv203", "ac_06general_AC_hscene202_a", 122),
        ("AC_tmb_hv206", "ac_06general_AC_hscene203_a", 123),
        ("AC_tmb_hv001", "ac_06general_AC_hscene001_a", 101),
    ]

    # The wide cream bar at the bottom of the music room is the OP movie
    # entry (SetupForMusic registers "AC_OP.mpg" when flag 320 is set).
    MUSIC_BAR_BOX = (38, 566, 1048, 608)

screen omake_tabs(cat=None):
    if cat is not None:
        $ _ab = GALLERY_TAB_BOXES[cat]
        add ui_crop("gallery_chrome_hover", _ab) xpos _ab[0] ypos _ab[1]
    for _li in (2, 3):
        $ _lb = GALLERY_TAB_BOXES[_li]
        add "ui/tab_locked.png" xpos _lb[0] ypos _lb[1]
    for i in range(8):
        $ bx = GALLERY_TAB_BOXES[i]
        button:
            xpos bx[0]
            ypos bx[1]
            xysize (bx[2] - bx[0], bx[3] - bx[1])
            background None
            hover_background ui_crop("gallery_chrome_hover", box=[bx[0], bx[1], bx[2] - bx[0], bx[3] - bx[1]])
            action (ShowMenu("replay") if i == 6
                    else ShowMenu("music_room") if i == 7
                    else ShowMenu("gallery", cat=i, page=1) if i in (0, 1, 4, 5)
                    else NullAction())

screen omake_exit():
    $ eb = GALLERY_EXIT_BOXES
    button:
        xpos eb[0][0]
        ypos eb[0][1]
        xysize (eb[0][2] - eb[0][0], eb[0][3] - eb[0][1])
        background None
        hover_background ui_crop("gallery_chrome_hover", eb[0])
        action Show("confirm", message=U("return_title_confirm"),
                    yes_action=Function(omake_return_title),
                    no_action=Hide("confirm"))
    button:
        xpos eb[1][0]
        ypos eb[1][1]
        xysize (eb[1][2] - eb[1][0], eb[1][3] - eb[1][1])
        background None
        hover_background ui_crop("gallery_chrome_hover", eb[1])
        action Quit(confirm=True)

screen gallery(cat=0, page=1):
    tag menu
    add "ui/gallery_bg.png"

    $ groups = GALLERY_BY_CAT.get(cat, [])
    $ page = max(1, min(page, gallery_page_count(cat)))
    $ chunk = groups[(page - 1) * 16: page * 16]

    for i, g in enumerate(chunk):
        $ cx, cy = GALLERY_CELL[i]
        if group_unlocked(g):
            button:
                xpos cx
                ypos cy
                xysize (GALLERY_W, GALLERY_H)
                background None
                hover_background "ui/cg_hover.png"
                action Function(open_cg, g)
                add ("ui/thumb/%s.png" % g["thumb"]) xysize (GALLERY_W, GALLERY_H)
        else:
            add ui_img("save_empty") xpos cx ypos cy
        add "ui/cg_frame.png" xpos cx ypos cy

    add ui_img("gallery_chrome")

    use omake_tabs(cat)

    # Replace the baked three-paw row with a centred row for the actual
    # page count (the original engine centres the needed pages).
    add ui_crop("gallery_bg", (330, 626, 800, 696)) xpos 330 ypos 626
    $ npages = gallery_page_count(cat)
    if npages > 1:
        $ pstart = 560 - 75 * npages
        for i in range(npages):
            $ px = pstart + 150 * i
            button:
                xpos px
                ypos 632
                xysize (150, 60)
                background None
                hover_background Solid("#ffffff26")
                action ShowMenu("gallery", cat=cat, page=i + 1)
                add ("ui/page_paw%d.png" % (i + 1)) xysize (150, 60)

    use omake_exit

screen music_room():
    tag menu
    add "ui/gallery_bg.png"
    add ui_img("music_chrome")

    for i, m in enumerate(MUSIC_LIST):
        $ col = i // 9
        $ row = i % 9
        $ mx = 50 if col == 0 else 565
        $ my = 28 + 60 * row
        button:
            xpos mx
            ypos my
            xysize (490, 36)
            background (Solid("#ff7fbf40") if _music_playing == m else None)
            hover_background Solid("#ff7fbf33")
            action (Function(play_bgm, m) if bgm_unlocked(m) else Notify(U("locked")))

    # The gallery chrome also carries the Page1-3 paw row, which the
    # music room does not have; only take the tab column and the two
    # exit pills from it.
    add ui_crop("gallery_chrome", (1100, 18, 1280, 700)) xpos 1100 ypos 18
    add ui_crop("gallery_chrome", (770, 662, 1110, 718)) xpos 770 ypos 662

    # SetupForMusic.bss calls grp__f_40d("AC_OP.mpg") when global flag 320
    # is set; the wide cream bar is that OP movie entry, so clicking it
    # plays the opening movie.
    button:
        xpos MUSIC_BAR_BOX[0]
        ypos MUSIC_BAR_BOX[1]
        xysize (MUSIC_BAR_BOX[2] - MUSIC_BAR_BOX[0], MUSIC_BAR_BOX[3] - MUSIC_BAR_BOX[1])
        background ui_crop("gallery_chrome_hover", (MUSIC_BAR_BOX[0], MUSIC_BAR_BOX[1], MUSIC_BAR_BOX[2] - MUSIC_BAR_BOX[0], MUSIC_BAR_BOX[3] - MUSIC_BAR_BOX[1]))
        hover_background Solid("#ff7fbf33")
        action (Function(play_op_movie) if persistent.steam_full else Notify(U("locked")))

    # Volume slider row (the original draws it between the two
    # diamonds, with MIN/MAX labels).
    text "MIN" xpos 630 ypos 645 size 14 color "#4a3128" font ui_font
    text "MAX" xpos 982 ypos 645 size 14 color "#4a3128" font ui_font
    bar:
        value Preference("music volume")
        xpos 658
        ypos 648
        xsize 330
        ysize 12
        left_bar Solid("#fb6eab")
        right_bar Solid("#ca0c5e")
        thumb "ui/vol_knob.png"

    button:
        xpos 300
        ypos 636
        xysize (80, 56)
        background None
        action (Function(play_bgm, _music_playing) if _music_playing else Notify(U("locked")))
    button:
        xpos 390
        ypos 636
        xysize (80, 56)
        background None
        action Function(stop_bgm)
    button:
        xpos 480
        ypos 636
        xysize (80, 56)
        background None
        action Function(stop_bgm)

    use omake_tabs(7)
    use omake_exit

init python:
    def open_cg_at(group, i):
        names = [n for n in group["cgs"] if n]
        if not names:
            return
        i = max(0, min(i, len(names) - 1))
        renpy.show_screen("cg_viewer", group=group, cg=names[i])

screen cg_viewer(group, cg=None):
    modal True
    add Solid("#000000")
    $ names = [n for n in group["cgs"] if n]
    $ idx = names.index(cg) if cg in names else 0
    add ("images/%s.png" % names[idx]):
        xalign 0.5
        yalign 0.5
    key "game_menu" action Hide("cg_viewer")
    key "K_ESCAPE" action Hide("cg_viewer")
    if idx > 0:
        textbutton "\u2039" xpos 12 ypos 330 action Function(open_cg_at, group, idx - 1) style "cg_nav"
    # The next arrow stays visible on the final image and leaves the viewer
    # instead: paging past the last CG goes back to the gallery, the way the
    # original omake viewer behaves, so the player is never stuck at the end.
    if idx < len(names) - 1:
        textbutton "\u203a" xpos 1236 ypos 330 action Function(open_cg_at, group, idx + 1) style "cg_nav"
    else:
        textbutton "\u203a" xpos 1236 ypos 330 action Hide("cg_viewer") style "cg_nav"
    text ("%d / %d" % (idx + 1, len(names))) xpos 1180 ypos 680 size 20 color "#ffeacb"

style cg_nav:
    background "#00000088"
    hover_background "#8a5a3a"
    padding (10, 6)

style cg_nav_text:
    size 32
    font ui_font
    color "#ffffff"

screen replay():
    tag menu
    add "ui/gallery_bg.png"

    # SetupForReplay.bss registers seven recollections (4 + 3 cells) and
    # shows the logo card for the ones that are still locked.
    for i, (thumb, label, flag) in enumerate(REPLAY_FIXED):
        $ cx, cy = GALLERY_CELL[i]
        if bgi_global(flag) == 1:
            button:
                xpos cx
                ypos cy
                xysize (GALLERY_W, GALLERY_H)
                background None
                hover_background "ui/cg_hover.png"
                action Start(label)
                add ("ui/thumb/%s.png" % thumb) xysize (GALLERY_W, GALLERY_H)
        else:
            add ui_img("save_empty") xpos cx ypos cy xysize (GALLERY_W, GALLERY_H)
        add "ui/cg_frame.png" xpos cx ypos cy

    add ui_img("gallery_chrome")
    add ui_crop("gallery_bg", (320, 612, 800, 702)) xpos 320 ypos 612
    use omake_tabs(6)
    use omake_exit

style replay_button:
    background "#2a211b"
    hover_background "#8a5a3a"
    xsize 560
    padding (12, 6)

style replay_button_text:
    size 22
    font ui_font
    hover_color "#ffffff"

###########################################################################
# Confirm / input / notify
###########################################################################
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#00000099")
    add "ui/confirm_panel.png" xpos 325 ypos 180
    frame:
        xpos 325
        ypos 180
        xysize (631, 360)
        background None
        padding (0, 0)
        text message:
            xalign 0.5
            ypos 118
            xsize 570
            ymaximum 130
            text_align 0.5
            size 27
            line_spacing 8
            color "#fff3e0"
            outlines [(3, "#402310", 0, 0)]
            font ui_font
    button:
        xpos 473 ypos 461
        xysize (151, 31)
        background "ui/yesno_yes.png"
        hover_background "ui/yesno_yes_hover.png"
        action yes_action
    button:
        xpos 666 ypos 461
        xysize (151, 31)
        background "ui/yesno_no.png"
        hover_background "ui/yesno_no_hover.png"
        action no_action
    key "K_ESCAPE" action no_action

screen input(prompt):
    modal True
    add Solid("#00000099")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12
        text prompt size 24 color "#ffeacb" font ui_font xalign 0.5
        input id "input" size 24 font ui_font

screen notify(message):
    zorder 100
    frame at notify_appear:
        background Solid("#2a211bdd")
        xalign 0.5
        ypos 60
        padding (16, 6)
        text message size 20 color "#ffeacb" font ui_font
    timer 3.25 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0
        linear 0.15 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0