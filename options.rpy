define config.name = "巧可甜恋"
define config.version = "1.0-full"
define config.screen_width = 1280
define config.screen_height = 720
define config.window = "auto"
define config.save_directory = "qiaoketianlian-full"
define config.default_fullscreen = False
define config.developer = True

default persistent.lang = "sc"

define config.main_menu_music = "audio/bgm/BGM003.ogg"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.rollback_enabled = True

# BACK LOG 的数据源。Ren'Py 默认是 None（完全不记录历史），原版游戏的
# 日志窗口可以往上翻很多条，所以这里必须打开；没有这一行 screen history
# 拿到的 _history_list 永远为空，界面就是一张空底图。
define config.history_length = 250
