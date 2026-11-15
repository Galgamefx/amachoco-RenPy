# Shared runtime support for the full port.
# Generated assets live in game/text_db_full.json (10473 lines x 3 languages).

init -10 python:
    import json as _json
    import os as _os

    def _load_game_json(name):
        f = renpy.file(name)
        try:
            return _json.loads(f.read().decode("utf-8"))
        finally:
            f.close()

    TEXT_DB = _load_game_json("text_db_full.json")
    SELECTION = TEXT_DB.pop("__selection__", {})

    UI_TEXT = {
        "title": {"sc": "巧可甜恋", "tc": "巧可甜戀", "jp": "チョコレート・レン"},
        "subtitle": {"sc": "完整版", "tc": "完整版", "jp": "フルバージョン"},
        "start": {"sc": "开始游戏", "tc": "開始遊戲", "jp": "ゲーム開始"},
        "continue": {"sc": "继续游戏", "tc": "繼續遊戲", "jp": "ゲームを続ける"},
        "load": {"sc": "读取存档", "tc": "讀取存檔", "jp": "ロード"},
        "save": {"sc": "保存进度", "tc": "保存進度", "jp": "セーブ"},
        "save_short": {"sc": "存档", "tc": "存檔", "jp": "セーブ"},
        "reset_confirm": {
            "sc": "要初始化已解锁的图鉴、音乐与路线记录吗？",
            "tc": "要初始化已解鎖的圖鑑、音樂與路線記錄嗎？",
            "jp": "解除したギャラリー・音楽・ルート記録を初期化しますか？",
        },
        "return_title_confirm": {
            "sc": "要回到标题画面吗？",
            "tc": "要回到標題畫面嗎？",
            "jp": "タイトルに戻りますか？",
        },
        "config": {"sc": "设置", "tc": "設定", "jp": "設定"},
        "gallery": {"sc": "图鉴", "tc": "圖鑑", "jp": "ギャラリー"},
        "music": {"sc": "音乐室", "tc": "音樂室", "jp": "ミュージック"},
        "replay": {"sc": "回想", "tc": "回想", "jp": "回想"},
        "quit": {"sc": "退出游戏", "tc": "離開遊戲", "jp": "ゲーム終了"},
        "back": {"sc": "返回", "tc": "返回", "jp": "戻る"},
        "full_version": {"sc": "完整版（含 H）", "tc": "完整版（含 H）", "jp": "完全版"},
        "all_ages": {"sc": "全年龄版", "tc": "全年齡版", "jp": "全年齢版"},
        "version_tag": {"sc": "v1.0 完整版", "tc": "v1.0 完整版", "jp": "v1.0 フル"},
        "history": {"sc": "回想", "tc": "回想", "jp": "履歴"},
        "auto": {"sc": "自动", "tc": "自動", "jp": "オート"},
        "skip": {"sc": "跳过", "tc": "跳過", "jp": "スキップ"},
        "hide": {"sc": "隐藏", "tc": "隱藏", "jp": "非表示"},
        "locked": {"sc": "尚未解锁", "tc": "尚未解鎖", "jp": "未解放"},
        "initialized": {"sc": "已初始化记录", "tc": "已初始化記錄", "jp": "初期化しました"},
        "copied": {"sc": "已复制存档", "tc": "已複製存檔", "jp": "コピーしました"},
        "deleted": {"sc": "已删除存档", "tc": "已刪除存檔", "jp": "削除しました"},
        "text_speed": {"sc": "文字速度", "tc": "文字速度", "jp": "文字速度"},
        "auto_forward": {"sc": "自动前进", "tc": "自動前進", "jp": "オート待ち"},
        "music_volume": {"sc": "音乐音量", "tc": "音樂音量", "jp": "BGM 音量"},
        "sound_volume": {"sc": "音效音量", "tc": "音效音量", "jp": "SE 音量"},
        "voice_volume": {"sc": "语音音量", "tc": "語音音量", "jp": "ボイス音量"},
        "display": {"sc": "画面模式", "tc": "畫面模式", "jp": "画面モード"},
        "windowed": {"sc": "窗口", "tc": "視窗", "jp": "ウィンドウ"},
        "fullscreen": {"sc": "全屏", "tc": "全螢幕", "jp": "全画面"},
        "skip_mode": {"sc": "跳过方式", "tc": "跳過方式", "jp": "スキップ"},
        "skip_all": {"sc": "全部跳过", "tc": "全部跳過", "jp": "全て"},
        "skip_seen": {"sc": "跳过已读", "tc": "跳過已讀", "jp": "既読のみ"},
        "language": {"sc": "语言", "tc": "語言", "jp": "言語"},
        "edition": {"sc": "版本", "tc": "版本", "jp": "バージョン"},
        "cg": {"sc": "CG 鉴赏", "tc": "CG 鑑賞", "jp": "CG 鑑賞"},
        "gallery_hint": {"sc": "点击缩略图查看大图；未解锁的 CG 显示为问号。", "tc": "點擊縮圖查看大圖；未解鎖的 CG 顯示為問號。", "jp": "サムネイルをクリックで拡大。未解放は「？」。"},
        "page": {"sc": "第", "tc": "第", "jp": "Page"},
        "play": {"sc": "播放", "tc": "播放", "jp": "再生"},
        "stop": {"sc": "停止", "tc": "停止", "jp": "停止"},
        "save_page": {"sc": "存档页", "tc": "存檔頁", "jp": "ページ"},
        "empty_slot": {"sc": "—— 空 ——", "tc": "—— 空 ——", "jp": "—— 空 ——"},
        "yes": {"sc": "是", "tc": "是", "jp": "はい"},
        "no": {"sc": "否", "tc": "否", "jp": "いいえ"},
        "return_game": {"sc": "返回游戏", "tc": "返回遊戲", "jp": "ゲームに戻る"},
    }

    def T(script, index):
        entry = TEXT_DB.get(script, {}).get("%06d" % index)
        if entry is None:
            return ("", "")
        lang = persistent.lang or "sc"
        item = entry.get(lang) or entry.get("jp") or {}
        return (item.get("name") or "", item.get("text") or "")

    def U(key):
        item = UI_TEXT.get(key, {})
        lang = persistent.lang or "sc"
        return item.get(lang) or item.get("sc") or key

    def SEL(jp_text):
        item = SELECTION.get(jp_text) or {}
        lang = persistent.lang or "sc"
        return item.get(lang) or item.get("sc") or jp_text

    def set_lang(code):
        persistent.lang = code
        apply_layout_text()
        renpy.restart_interaction()

    # ------------------------------------------------------------------
    # BGI global flags.  320 is the Steam/full-version switch; every other
    # flag records CG/route progress and feeds the gallery.
    # ------------------------------------------------------------------
    def bgi_global(n):
        n = int(n)
        if n == 320:
            return 1 if persistent.steam_full else 0
        return int((persistent.bgi_flags or {}).get(str(n), 0))

    def bgi_set_global(n, value):
        flags = persistent.bgi_flags
        if flags is None:
            flags = persistent.bgi_flags = {}
        flags[str(int(n))] = int(bool(value))

    def bgi_bool_and(left, right):
        return int(left != 0 and right != 0)

    def bgi_cg(name):
        seen = persistent.cg_unlocked
        if seen is None:
            seen = persistent.cg_unlocked = []
        if name not in seen:
            seen.append(name)

    def bgi_bgm(name):
        played = persistent.bgm_unlocked
        if played is None:
            played = persistent.bgm_unlocked = []
        if name not in played:
            played.append(name)

init -5 python:
    if persistent.steam_full is None:
        persistent.steam_full = True
    if persistent.bgi_flags is None:
        persistent.bgi_flags = {}
    if persistent.bgm_unlocked is None:
        persistent.bgm_unlocked = []
    if persistent.cg_unlocked is None:
        persistent.cg_unlocked = []
default bgi_local = {}
default bgi_localw = {}

define ch = Character("[speaker]", what_size=24, who_size=30)

# BGI shakes the bustshot sprite, not the whole screen.
transform sprite_shake:
    linear 0.03 xoffset 8
    linear 0.03 xoffset -8
    linear 0.03 xoffset 6
    linear 0.03 xoffset -6
    linear 0.03 xoffset 0

transform move_right_to_left:
    zoom 1.5
    align (0.2, 0.5)
    xoffset -448        # 从屏幕右侧外开始（1.0 代表屏幕右边缘）
    linear 30.0 xoffset 0

transform zoom_in_out:
    zoom 1.5
    align (0.5, 0.5)
    linear 2 zoom 1.0

transform shake_y:
    pause 0.3
    linear 0.15 yoffset -15
    linear 0.075 yoffset 0

transform shake_y1:
    pause 0.3
    linear 0.2 yoffset -10
    linear 0.1 yoffset 0

transform shake_yx:
    pause 0.3
    linear 0.2 yoffset 10
    pause 0.1
    linear 0.1 yoffset 0

transform shake_x:
    pause 0.3
    linear 0.2 xoffset -5
    linear 0.2 xoffset 5
    linear 0.2 xoffset 0

transform shake_ry:
    yoffset 0
    linear 0.25 yoffset -5
    linear 0.25 yoffset 5
    linear 0.125 yoffset 0
    repeat

transform zoom_in_out1:
    align (0.5, 0.5)
    linear 0.8 zoom 1.24
    align (0.5, 0.5)

transform zoom_in_out2:
    zoom 1.24
    align (0.5, 0.5)
    linear 0.5 zoom 1.0
    align (0.5, 0.5)

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
init -9 python:

    # Strings used by Ren'Py's own confirm paths (overwrite/delete save,
    # quit, main menu, load token prompt).  They live on the legacy
    # ``layout`` object and in the ``gui`` store namespace.
    LAYOUT_TEXT = {
        "sc": {
            "ARE_YOU_SURE": "确定吗？",
            "QUIT": "确定要退出游戏吗？",
            "MAIN_MENU": "返回标题将丢失未保存的进度。\n确定吗？",
            "OVERWRITE_SAVE": "要覆盖此存档吗？",
            "DELETE_SAVE": "要删除此存档吗？",
            "LOADING": "读取存档将丢失未保存的进度。\n确定吗？",
            "CONTINUE": "要从上次中断处继续吗？",
            "END_REPLAY": "要结束回放吗？",
            "SLOW_SKIP": "要开始快进吗？",
            "FAST_SKIP_SEEN": "要跳到下一个选项吗？",
            "FAST_SKIP_UNSEEN": "要快进未读文本到下一个选项吗？",
            "UNKNOWN_TOKEN": "无法验证此存档的来源，载入可能不安全。\n仍要载入吗？",
            "TRUST_TOKEN": "此存档由其他设备创建，可能被篡改。\n仍要信任并载入吗？",
        },
        "tc": {
            "ARE_YOU_SURE": "確定嗎？",
            "QUIT": "確定要退出遊戲嗎？",
            "MAIN_MENU": "返回標題將丟失未保存的進度。\n確定嗎？",
            "OVERWRITE_SAVE": "要覆蓋此存檔嗎？",
            "DELETE_SAVE": "要刪除此存檔嗎？",
            "LOADING": "讀取存檔將丟失未保存的進度。\n確定嗎？",
            "CONTINUE": "要從上次中斷處繼續嗎？",
            "END_REPLAY": "要結束回放嗎？",
            "SLOW_SKIP": "要開始快進嗎？",
            "FAST_SKIP_SEEN": "要跳到下一個選項嗎？",
            "FAST_SKIP_UNSEEN": "要快進未讀文本到下一個選項嗎？",
            "UNKNOWN_TOKEN": "無法驗證此存檔的來源，載入可能不安全。\n仍要載入嗎？",
            "TRUST_TOKEN": "此存檔由其他裝置建立，可能被竄改。\n仍要信任並載入嗎？",
        },
        "jp": {
            "ARE_YOU_SURE": "よろしいですか？",
            "QUIT": "ゲームを終了しますか？",
            "MAIN_MENU": "タイトルに戻ると、保存されていない進行状況は失われます。\nよろしいですか？",
            "OVERWRITE_SAVE": "このセーブデータに上書きしますか？",
            "DELETE_SAVE": "このセーブデータを削除しますか？",
            "LOADING": "ロードすると、保存されていない進行状況は失われます。\nよろしいですか？",
            "CONTINUE": "前回の続きから始めますか？",
            "END_REPLAY": "リプレイを終了しますか？",
            "SLOW_SKIP": "スキップを開始しますか？",
            "FAST_SKIP_SEEN": "次の選択肢まで進みますか？",
            "FAST_SKIP_UNSEEN": "未読テキストを次の選択肢までスキップしますか？",
            "UNKNOWN_TOKEN": "このセーブデータの出所を確認できません。\n読み込むと危険な場合があります。よろしいですか？",
            "TRUST_TOKEN": "このセーブデータは別の端末で作成されました。\n改ざんされている可能性があります。信頼して読み込みますか？",
        },
    }

    def apply_layout_text():
        lang = persistent.lang or "sc"
        table = LAYOUT_TEXT.get(lang, LAYOUT_TEXT["sc"])
        for key in ("ARE_YOU_SURE", "QUIT", "MAIN_MENU", "OVERWRITE_SAVE",
                    "DELETE_SAVE", "LOADING", "CONTINUE", "END_REPLAY",
                    "SLOW_SKIP", "FAST_SKIP_SEEN", "FAST_SKIP_UNSEEN"):
            setattr(layout, key, table[key])
        gui.UNKNOWN_TOKEN = table["UNKNOWN_TOKEN"]
        gui.TRUST_TOKEN = table["TRUST_TOKEN"]

    apply_layout_text()
