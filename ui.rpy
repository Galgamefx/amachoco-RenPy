# Baked BGI UI art and layout helpers.
init -20 python:
    import json as _json_ui

    def _ui_read(name):
        f = renpy.file(name)
        try:
            return _json_ui.loads(f.read().decode("utf-8"))
        finally:
            f.close()

    UI_LAYOUT = _ui_read("ui_layout.json")

    def ui_lang():
        return persistent.lang or "sc"

    def ui_suffix():
        return {"jp": "_jp", "sc": "_sc", "tc": "_tc"}.get(ui_lang(), "")

    def ui_img(name, lang=None):
        if lang is None:
            lang = ui_lang()
        suffix = {"jp": "_jp", "sc": "_sc", "tc": "_tc"}.get(lang, "")
        path = "ui/%s%s.png" % (name, suffix)
        if renpy.loadable(path):
            return path
        return "ui/%s.png" % name

    def _ui_key(name, lang=None):
        if lang is None:
            lang = ui_lang()
        suffix = {"jp": "_jp", "sc": "_sc", "tc": "_tc"}.get(lang, "")
        key = name + suffix
        if key in UI_LAYOUT:
            return key
        return name

    def ui_boxes(name, lang=None):
        return UI_LAYOUT.get(_ui_key(name, lang), {}).get("boxes", [])

    def ui_crop(name, box, lang=None):
        return Transform(ui_img(name, lang), crop=(box[0], box[1], box[2] - box[0], box[3] - box[1]))

    def ui_hotspot(name, index):
        boxes = ui_boxes(name)
        if index < len(boxes):
            return boxes[index]
        return [0, 0, 1, 1]

    def ui_cg_list():
        return persistent.cg_unlocked or []

    def cg_unlocked(name):
        return name in ui_cg_list()

    def bgm_unlocked(name):
        return name in (persistent.bgm_unlocked or [])

init python:
    _CG_DATA = _ui_read("gallery_data.json")
    GALLERY_GROUPS = _CG_DATA["groups"]
    GALLERY_PAGES = _CG_DATA["pages"]
    MUSIC_LIST = _CG_DATA["music"]

    def gallery_groups(page):
        return [g for g in GALLERY_GROUPS if g["page"] == page]

    def group_unlocked(g):
        return any(cg_unlocked(n) for n in g["cgs"] if n)

    def group_first_unlocked(g):
        for n in g["cgs"]:
            if cg_unlocked(n):
                return n
        return None

    def _build_replay_scenes():
        out = []
        for g in GALLERY_GROUPS:
            hv = [n for n in g["cgs"] if n and n.startswith("hv")]
            if not hv:
                continue
            num = hv[0][2:5]
            out.append({
                "title": hv[0],
                "cgs": g["cgs"],
                "label": "ac_06general_AC_hscene%s_a" % num,
                "thumb": g["thumb"],
            })
        return out

    REPLAY_SCENES = _build_replay_scenes()
init -1 python:

    def _yizhi_yesno_prompt(message=None, prompt=None, *args, **kwargs):
        # Legacy layout hook used by renpy.savetoken.check_load() and
        # the old game-menu navigation. Show our baked confirm panel and
        # return the chosen value.
        text = prompt if prompt is not None else (message or "")
        return renpy.call_screen(
            "confirm",
            message=text,
            yes_action=Return(True),
            no_action=Return(False))

    layout.yesno_prompt = _yizhi_yesno_prompt

# Save-slot info: store the line that was on screen when the player saved,
# the way the original engine shows a quote inside each save card.
init -2 python:
    def _yizhi_save_json(d):
        d["line"] = getattr(store, "_last_line", "") or ""
        d["who"] = getattr(store, "_last_who", "") or ""

    if _yizhi_save_json not in config.save_json_callbacks:
        config.save_json_callbacks.append(_yizhi_save_json)
