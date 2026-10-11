style ruby_style is default:
    size 12
    yoffset -20
    color None # 使用父文本相同的颜色。
    font None #使用父文本相同的字体。

style say_dialogue:
    ruby_line_leading 12
    ruby_style style.ruby_style

style history_text:
    ruby_line_leading 12
    ruby_style style.ruby_style

label language:
    with dissolve
    menu:
        "言語を選択してくださし\n言語を変更するとゲミムンステムカ再起動ます"
        "简体中文/簡體中文/简体字中文":
            $ renpy.change_language("sc")
            $ persistent.柚希 = _("柚希")
            $ persistent.女の子 = _("女孩")
            $ persistent.千絵莉 = _("千绘莉")
            $ persistent.巫女さん = _("神社少女")
            $ persistent.苺華 = _("莓华")
            $ persistent.ナナ = _("娜娜")
            $ persistent.font = "SourceHanSansLite.ttf"
            jump ac_00common
        "繁体中文/繁體中文/繁休字中文":
            $ renpy.change_language("tc")
            $ persistent.柚希 = _("柚希")
            $ persistent.女の子 = _("女孩")
            $ persistent.千絵莉 = _("千繪莉")
            $ persistent.巫女さん = _("神社少女")
            $ persistent.苺華 = _("莓華")
            $ persistent.ナナ = _("娜娜")
            $ persistent.font = "microsoft-jhenghei.ttf"
            jump ac_00common
        "日語/日塔/日本語":
            $ renpy.change_language("jp")
            $ persistent.柚希 = _("柚希")
            $ persistent.女の子 = _("女の子")
            $ persistent.千絵莉 = _("千絵莉")
            $ persistent.巫女さん = _("巫女さん")
            $ persistent.苺華 = _("苺華")
            $ persistent.ナナ = _("ナナ")
            $ persistent.font = "ms-prgothic.ttf"
            jump ac_00common

label start:
    with dissolve
    menu:
        "現在は目本語が選択されでします。\n言語を変更しますか？"
        "日本語のままプレイします":
            if _preferences.language == "sc":
                $ renpy.change_language("sc")
                $ persistent.柚希 = _("柚希")
                $ persistent.女の子 = _("女孩")
                $ persistent.千絵莉 = _("千绘莉")
                $ persistent.巫女さん = _("神社少女")
                $ persistent.苺華 = _("莓华")
                $ persistent.ナナ = _("娜娜")
            elif _preferences.language == "jp":
                $ persistent.柚希 = _("柚希")
                $ persistent.女の子 = _("女の子")
                $ persistent.千絵莉 = _("千絵莉")
                $ persistent.巫女さん = _("巫女さん")
                $ persistent.苺華 = _("苺華")
                $ persistent.ナナ = _("ナナ")
            elif _preferences.language == "tc":
                $ persistent.柚希 = _("柚希")
                $ persistent.女の子 = _("女孩")
                $ persistent.千絵莉 = _("千繪莉")
                $ persistent.巫女さん = _("神社少女")
                $ persistent.苺華 = _("莓華")
                $ persistent.ナナ = _("娜娜")
            jump ac_00common
        "言語を変更します":
            jump language

label ac_00common:
    play music "bgm/bgm003.ogg"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    yx "……今日からこニ住むんだよね"
    scene bg31DAY at move_right_to_left
    with dissolve
    "ここが{rb}夕渚町{/rb}{rt}ゆうなぎちょう{/rt}。日本離れしてるとは聞いてたけど、まるで外国だ。"
    "昼下がりの町を歩いていると、石畳を一歩踏みしめる度に、知らない場所にやってきたんだと実感が湧く。"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    play sound "se/se_byu.ogg"
    pause 1.0
    scene bg31DAY:
        align (0.5, 0.5) 
    with hpunch
    yx "うっ……ちょっと風が強いかな"
    "海辺の町らしい、湿気を帯びた冷たい風に肌を撫でられ、少し鳥肌が立つ。"
    yx "もうすっかり秋だし、体調には気を付けないと――"
    scene white
    with dissolve
    pause 1.0
    scene ev201a at zoom_in_out
    with dissolve
    voice "voice/chi/chi_a000001.ogg"
    chi_no "き、喫茶『セタリア』ですっ。よろしくおねがいしますっ"
    "道の少し先のところで、メイド服のような服装の女の子がお店のチラシを配っていた。"
    "僕より年下だろうか。小さな背丈や幼い顔立ちに、リボンやエプロンがよく似合っている。"
    voice "voice/chi/chi_a000002.ogg"
    chi_no "あの……セタリアですっ。よかったら来てください"
    voice "voice/chi/chi_a000003.ogg"
    chi_no "お、お願いしますっ"
    "だけど表情には緊張が表れていて、うまくチラシを渡せないこともあったり。"
    "それでも１人で頑張っている姿を見ていると、力になってあげたい気持ちになった。"
    yx "チラシ、僕にももらえるかな"
    scene ev201b at hpunch:
        align (0.5, 0.5)
    with dissolve 
    voice "voice/chi/chi_a000004.ogg"
    chi_no "あっ、はいっ、どうぞ"
    "突然話しかけられて驚いたのか、少し目を見開きながらチラシを渡してくれた。"
    yx "お店はここから近いのかな？　この町は初めてだから、ちょっとわからなくて"
    voice "voice/chi/chi_a000005.ogg"
    chi_no "はい、町の中心からは外れるんですけど……"
    "チラシにも地図は描いてあるんだけど、せっかくだから道順を教えてもらった。"
    yx "ありがとう。ちょうどひと休みしたかったところだし、行ってみるよ"
    scene ev201c:
        align (0.5, 0.5)
    with dissolve
    voice "voice/chi/chi_a000006.ogg"
    chi_no "あ……はいっ！　ありがとうございます！"
    "女の子の表情がぱっと明るくなった。"
    yx_no "（あれ？　でもどこか……）"
    "女の子の姿にちょっとした違和感を覚える。"
    "まるで間違い探しのクイズを前にした時のような感覚。"
    "だけどその瞬間――"
    play sound "se/se_byua.ogg"
    scene black with mask004
    show bg31DAY with mask004:
        align (0.5, 0.5)
    show chi01A 402 at shake_xy:
        align (0.42, -1.65)
    with dissolve
    voice "voice/chi/chi_a000007.ogg"
    chi_no "きゃっ！？"
    "風にチラシが舞い上げられ、飛ばされていく。"
    scene bg31DAY_br:
        align (0.5, 0.5)
    show chi12A 402 at shake_xy:
        align (0.35, 0.25)
    with dissolve
    voice "voice/chi/chi_a000008.ogg"
    chi_no "あ……拾わないと……えっと……"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    "辺りに舞い散るチラシを追いかけようとする女の子。"
    "だけどチラシがあちこちに飛ばされてしまって、どうしていいか困惑している様子だ。"
    show chi01A 303:
        align (0.42, -1.65)
    with dissolve
    yx "僕があっち行くから、向こうはお願い"
    show chi01A 402 at shake_y
    with dissolve
    voice "voice/chi/chi_a000009.ogg"
    chi_no "は、はいっ"
    scene black with mask024a
    pause 2
    show bg31DAY with mask024a:
        align (0.5, 0.5)
    scene bg31DAY at shake_ry:
        align (0.5, 0.5)
    play sound "se/se_run.ogg"
    "チラシを町のごみにするわけにいかない。風に乗って離れていくチラシを追いかけ、人の間をすり抜けながら駆ける。"
    "地面に落ちたチラシを拾い集め、またチラシを追って走ってを繰り返す。"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    yx "あともうちょっと……"
    scene bg31DAY at zoom_in_out1
    "隅に落ちたチラシに手を伸ばす。"
    play sound "se/se_byua.ogg"
    scene bg31DAY at zoom_in_out2
    yx "あっ！？"
    scene bg80day:
        align (0.5, 0.5)
    with dissolve
    "だけど、また風に巻き上げられて――"
    scene bg31DAY_ex:
        align (0.5, 0.5)
    with dissolve
    pause 1.0
    play sound "se/SE_JARI.ogg"
    show mik02B 001 at character_sequence
    with dissolve
    pause 0.2
    voice "voice/chi/mik_a000001.ogg"
    w "ほいっ"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    "誰かが高くジャンプして、舞い上がったチラシをキャッチした。"
    scene bg31DAY_br:
        align (0.5, 0.5)
    show mik11B 102:
        align (1.3, 0.4)
    with dissolve
    voice "voice/chi/mik_a000002.ogg"
    mik_no "はい、これでいいの？"
    show mik11B 102 at shake_y1
    "そしてチラシを手渡してくれたのは、巫女さんの衣装を着た女の子だった。"
    yx "ありがとう、助かったよ"
    hide mik11B
    show mik12B 102 at shake_y1:
        align (0.5, 0.2)
    with dissolve
    play sound "se/SE_FLOWER_a.ogg"
    voice "voice/chi/mik_a000003.ogg"
    mik_no "どーいたしましてー♪"
    scene bg31DAY:
        align (0.5, 0.5)
    show mik02B 102:
        align (0.47, -0.55)
    with dissolve
    "僕がお礼を言うと、人懐っこい笑顔を浮かべる。"
    "こっちまで元気をもらえそうな屈託のない笑顔だ。"
    show black75
    with dissolve
    yx_no "（んん？　この子も、さっきの女の子みたいに……）"
    hide black75
    with dissolve
    hide mik02B
    show mik01B 001 at shake_y2:
        align (0.48, -0.25)
    with dissolve
    voice "voice/chi/mik_a000004.ogg"
    mik_no "ん？　わたしの顔に何か付いてる？"
    yx "いや……ごめん、何でもない"
    "うん、顔には変なもの付いてないよね。"
    hide mik01B
    show mik02B 102 at shake_y3:
        align (0.47, -0.55)
    with dissolve
    voice "voice/chi/mik_a000005.ogg"
    mik_no "じゃーねー♪"
    play sound "se/SE_FOOT.ogg"
    show mik02B 102 at sequence
    "パタパタと手を振って去っていく巫女さん。"
    scene bg31DAY_ex with mask024a:
        align (0.15, 0.5)
    with dissolve
    play sound "se/SE_JARI.ogg"
    show mik01B 402 at shake_y2:
        align (0.51, -0.25)
    with dissolve
    voice "voice/chi/mik_a000006.ogg"
    mik_no "あ"
    "だけど突然立ち止まって、僕の方を振り返った。"
    scene bg31DAY_br:
        align (0.15, 0.45)
    show mik11B 103:
        align (1.3, 0.4)
    with dissolve 
    voice "voice/chi/mik_a000007.ogg"
    mik_no "君、きっといいことあるよ。神様がそう言ってるから！"
    yx "神様？"
    show mik11B 103:
        xpos 1.3
        easein 0.5 xpos 1.25 alpha 0.0
    "あっけに取られているうちに、巫女さんの姿が雑踏の中に消えていく。"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    yx "いいことある……か。本当だといいな"
    scene bg31DAY with vpunch:
        align (0.5, 0.5)
    play sound "se/SE_KYUPIN.ogg"
    yx "あれ？　巫女さん！？"
    yx "こんな外国っぽい町に巫女さん？　……そもそも巫女さんって、巫女服で町を歩き回ったりするの？"
    "別れた後になって、次々と疑問が浮かんでくるのだった。"
    scene black with mask016f
    pause 1.0
    show bg31DAY with mask016f:
        align (0.5, 0.5)
    pause 1.0
    play music "bgm/BGM001.ogg"
    show chi01A 301:
        align (0.42, -1.7)
        pause 0.5
        yoffset 0
        linear 0.25 yoffset 10
        linear 0.25 yoffset -10
    with dissolve
    voice "voice/chi/chi_a000010.ogg"
    chi_no "本当に……すみませんでしたっ"
    "拾い終わったチラシを渡すと、女の子は深々と頭を下げた。"
    "本当に申し訳なさそうな様子で、こっちが気の毒になるくらいだ。"
    yx "大丈夫、困ったときはお互い様だよ。僕だって、さっき巫女さんに手伝ってもらったしね"
    hide chi01A
    show chi02A 401:
        align (0.49, -2.0)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset 10
        linear 0.15 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000011.ogg"
    chi_no "巫女さん……ですか？　珍しいですね……"
    "女の子も不思議そうに首を傾げる。"
    "やっぱりそうそうお目にかかるものではないようだ。"
    hide chi02A
    show chi02A 301:
        align (0.49, -2.0)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 10
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000012.ogg"
    chi_no "この度はご迷惑をおかけしました。お詫びをいたしますので、お名前とご連絡先を……"
    yx "気にしなくていいよ。頼まれてもいないのに、僕が勝手にやったことだから"
    yx "それに、さっきはお店に行く道を教えてもらったしね"
    hide chi02A
    show chi01A 303:
        align (0.42, -1.6)
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.2 xoffset 0
    with dissolve
    voice "voice/chi/chi_a000013.ogg"
    chi_no "でも……"
    "しかし女の子は納得していないみたいだ。"
    yx "ところで、これからどうするの？　チラシ配り続ける？"
    hide chi01A
    show chi02A 001:
        align (0.49, -1.9)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000014.ogg"
    chi_no "クシャクシャになったチラシをお渡しするわけにはいきませんし、一度お店に戻ろうと思います"
    yx "じゃあ、お店まで案内してくれないかな？　道は教えてもらったけど、僕、ちょっと方向音痴だから迷わないか心配で"
    yx "それも込みでおあいこってことでどうかな？"
    hide chi02A
    show chi01A 101:
        align (0.42, -1.6)
    with dissolve
    voice "voice/chi/chi_a000015.ogg"
    chi_no "それなら――"
    play sound "se/SE_COMEDY.ogg"
    show chi01A 602:
        align (0.42, -1.6)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000016.ogg"
    chi_no "いえ、おあいこになりません！　お客様を案内するのは店員として当然のこと……むしろ、来店して頂くのはこちらの利益です！"
    play sound "se/SE_ZAN.ogg"
    with vpunch
    yx "ダメだった！？"
    "なんて真面目な子なんだ。"
    "微笑ましいと思ってしまうけど、これじゃ何を言っても聞かないかもしれない。"
    yx "えーっと……じゃあ、何かお礼してもらうってことでいいかな？"
    hide chi01A
    show chi02A 101:
        align (0.49, -1.9)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000017.ogg"
    chi_no "はい、このお礼は必ず"
    "彼女の表情は心なしかちょっと嬉しそうで、お礼してと言った方がかえって元気が出たみたいだった。"
    hide chi02A 
    show chi01A 001:
        align (0.42, -1.6)
    with dissolve
    voice "voice/chi/chi_a000018.ogg"
    chi_no "それではお名前を伺ってもよろしいですか？"
    yx "僕は{rb}城川柚希{/rb}{rt}しろかわゆずき{/rt}。今日この町に越してきたところで、いろいろ手続きしてきたんだ"
    show chi01A 302
    with dissolve
    hide chi01A
    show chi02A 301:
        align (0.49, -1.9)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000019.ogg"
    chi_no "そうでしたか……。お忙しいのにお手間を取らせてすみませんでした"
    hide chi02A
    show chi01A 001:
        align (0.42, -1.6)
    with dissolve
    voice "voice/chi/chi_a000020.ogg"
    chi "私は{rb}雪村千絵莉{/rb}{rt}ゆ き む ら ち え り{/rt}といいます。セタリアという喫茶店でアルバイトをしています"
    yx "そっか。千絵莉ちゃん、だね"
    hide chi01A
    show chi02A 201:
        align (0.49, -1.9)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    play sound "se/SE_COMEDY_d.ogg"
    voice "voice/chi/chi_a000021.ogg"
    chi "むぅ……"
    "あ、ちょっと複雑な顔になった。"
    yx "ごめん、いきなり名前で呼ぶなんて馴れ馴れしかったね"
    hide chi02A
    show chi01A 301:
        align (0.42, -1.6)
    with dissolve
    voice "voice/chi/chi_a000022.ogg"
    chi "すみません、そういうことではなく……"
    hide chi01A
    with dissolve
    scene bg31DAY_br:
        align (0.5, 0.5)
    show black50
    show chi12A 703:
        align (0.35, 0.18)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    play sound "se/SE_DOYON_a.ogg"
    voice "voice/chi/chi_a000023.ogg"
    chi2 "（やっぱり“ちゃん”なんだ……）"
    scene bg31DAY:
        align (0.5, 0.5)
    with dissolve
    yx "？"
    "今、小さい声でなんて言ったんだろ？"
    show chi01A 101:
        align (0.42, -1.6)
        pause 0.5
        xoffset 0
        linear 0.3 xoffset 10
        linear 0.3 xoffset -10
        linear 0.3 xoffset 0
    with dissolve
    voice "voice/chi/chi_a000024.ogg"
    chi "いえ、気にしないでください。では、お店にご案内しますね"
    hide chi01A
    with dissolve
    play sound "se/SE_WALK.ogg"
    scene black with mask003
    pause 2.0
    scene bg01DAY with mask016g:
        align (0.5, 0.5)
    "一緒に歩くことしばらく――"
    show chi02A 104:
        align (0.49, -1.9)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -10
        linear 0.15 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000025.ogg"
    chi "ここがセタリアです"
    yx "やっぱりお店も外国風なんだね"
    yx "夕渚町には初めて来たけど、まるで外国みたいで趣があるというか、素敵な町だよね"
    hide chi02A
    show chi01A 101:
        align (0.42, -1.7)
    with dissolve
    show chi01A 102:
        align (0.42, -1.7)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000026.ogg"
    chi "私はずっとこの町で暮らしてるので、逆に普通の町はあまり知らないんですけど……そう言ってもらえると嬉しいですね"
    hide chi01A
    show chi02A 601:
        align (0.49, -1.9)
    with dissolve
    voice "voice/chi/chi_a000027.ogg"
    chi "何十年も前にヨーロッパから日本に渡ってきた人がいて、その人が中心になってこの町を作ったと聞いています"
    show chi02A 001
    with dissolve
    voice "voice/chi/chi_a000028.ogg"
    chi "だからドイツやチェコ、ルーマニアなど、ヨーロッパのいろんな国の建物を参考にしているんだそうです"
    yx "なるほど、それで……"
    "異国から渡ってきた時、その人はどんな心境だったんだろうか。"
    "見知らぬ人と土地に大きな不安を抱いていたのか、それとも期待に胸を膨らませて新天地にやってきたのか――"
    "ちょうど今、僕も今まで住んでいたところを離れてこの町に来たけど……ちょっと想像つかないな。"
    scene bg01DAY_br:
        align (0.5, 0.5)
    show chi12A 104:
        align (0.35, 0.25)
        pause 0.5
        yoffset 0
        linear 0.3 yoffset 20
        linear 0.3 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000029.ogg"
    chi "どうぞ、城川さん"
    scene bg01DAY:
        align (0.5, 0.5)
    with dissolve
    "千絵莉ちゃんがお店のドアを開けて――"
    scene white 
    with dissolve
    pause 2.0
    stop music
    play sound "se/SE_BELL.ogg"
    scene bg03DAY:
        align (0.5, 0.5)
    with dissolve
    pause 2.0
    play music "bgm/BGM011.ogg"
    scene bg03DAY_br:
        align (0.71, 0.45)
    show ich12A 105:
        align (0.5, 0.29)
    with dissolve
    voice "voice/chi/ich_a000001.ogg"
    w "いらっしゃいませ～"
    scene bg03DAY:
        align (0.5, 0.5)
    show chi02A 001:
        align (0.17, -1.9)
    with dissolve
    show ich01A 402:
        align (0.83, -0.85)
        xpos 0.84
        alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easeout 0.5 xpos 0.83
        pause 0.1
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
        pause 1.5
        yoffset 0
        linear 0.15 yoffset 20
        linear 0.15 yoffset 0
    voice "voice/chi/ich_a000002.ogg"
    w "あれ、千絵莉ちゃん？　おかえりなさい、早かったね"
    hide chi02A
    show chi01A 301:
        align (0.03, -1.6)
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.2 xoffset 0
    with dissolve
    voice "voice/chi/chi_a000030.ogg"
    chi "それが、ちょっとトラブルがありまして……"
    hide chi01A
    show chi02A 101:
        align (0.17, -1.9)
    with dissolve
    voice "voice/chi/chi_a000031.ogg"
    chi "それより、こちらお客様です。{rb}苺華{/rb}{rt}いちか{/rt}先輩"
    hide ich01A
    show ich02A 104:
        align (0.8, -0.7)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
    with dissolve
    play sound "se/SE_COMEDY_d.ogg"
    voice "voice/chi/ich_a000003.ogg"
    ich "あっ、すみません。すぐにご案内しますね"
    yx "いえいえお構いなく……って、お店で言うことじゃないですね"
    hide ich02A
    show ich01A 102:
        align (0.83, -0.85)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset 20
        linear 0.15 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000004.ogg"
    ich "ふふっ、そうですね。お客様なんですから、構わせてください"
    scene bg03DAY_br:
        align (0.5, 0.5)
    with dissolve
    pause 0.5
    show ich12A 101 zorder 99:
        align (0.5, 0.29)
    with dissolve
    show white:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos -0.125
        yanchor 0
        linear 0.5 ypos 0
    show white_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 1.0
        yanchor 0
        linear 0.5 ypos 0.875
    play sound "se/SE_FLOWER_a.ogg"
    "とても柔らかそうで、ふわふわした雰囲気の女の子だ。"
    "小柄で華奢な印象だけど、先輩と呼ばれてるから、きっと千絵莉ちゃんより年上なんだろう。"
    show white:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0
        yanchor 0
        linear 0.5 ypos -0.125
    show white_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0.875
        yanchor 0
        linear 0.5 ypos 1.0
    hide ich12A
    with dissolve
    pause 0.5
    scene bg03DAY:
        align (0.5, 0.5)
    with dissolve
    pause 0.5
    show black75
    with dissolve
    yx_no "（ん？　このふわふわしてもこもこした感じ、僕は知っているような……）"
    "なぜか既視感を覚えたけど、今日はこんなことばかりな気がする。"
    hide black75
    with dissolve
    yx_no "（うーん……気のせいかな。初めての町だし、落ち着かないのかも）"
    scene bg02DAY with mask024a:
        align (0.5, 0.5)
    "他にお客さんがいないようなので、窓際の席に座らせてもらった。"
    show chi01A 302:
        align (0.03, -1.6)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    show ich01A 101:
        align (0.83, -0.85)
    with dissolve
    voice "voice/chi/chi_a000032.ogg"
    chi "実はさっき、チラシが飛ばされて、助けていただいて……"
    show ich01A 601
    with dissolve
    voice "voice/chi/ich_a000005.ogg"
    ich "なるほど、それで早く帰ってきたんだね"
    window hide
    with dissolve
    pause 0.3
    scene bg02DAY_br:
        align (0.71, 0.45)
    show ich12A 104:
        align (0.5, 0.29)
        pause 5.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000006.ogg"
    ich "すみません、先ほどは店の者がお世話になりました。ありがとうございます"
    yx "いえいえ、本当に大したことはしてないですから"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.4)
    with dissolve
    pause 0.5
    show chi01A 001:
        alpha 0.0
        align (0.42, -1.7)
        xpos 0.41
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easeout 0.5 xpos 0.42
    "そこに、千絵莉ちゃんがお冷とメニューを持ってやってくる。"
    show chi01A 101:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
        pause 5.0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000033.ogg"
    chi "どうぞ、メニューです。本日はサービスさせていただきますので、お好きなものをご注文してください"
    yx "……そのお金って千絵莉ちゃんが出すの？"
    show chi01A 602 :
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000034.ogg"
    chi "はい、ですから気兼ねなくどうぞ"
    show chi01A 601
    with dissolve
    "真剣な眼差しが僕を見つめる。"
    "何かお礼をしないと気が済まない、と言わんばかりだ。"
    window hide 
    with dissolve
    scene bg02DAY_br:
        align (0.5, 0.5)
    show chi12A 704:
        align (0.35, 0.25)
    with dissolve
    voice "voice/chi/chi_a000035.ogg"
    chi "じー……"
    yx "……とりあえず、決めるまで待ってくれるかな？"
    window hide 
    with dissolve
    scene bg02DAY:
        align (0.5, 0.4)
    show chi01A 101:
        align (0.42, -1.7)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000036.ogg"
    chi "かしこまりました"
    show chi01A 101:
        align (0.42, -1.7)
        alpha 1.0
        xpos 0.42
        parallel:
            linear 0.6 alpha 0.0
        parallel:
            easeout 0.6 xpos 0.4
    "千絵莉ちゃんがぺこりと完璧な角度で頭を下げ、カウンターへと下がっていく。"
    window hide 
    with dissolve
    scene bg03DAY with mask003a:
        align (0.5, 0.5)
    pause 1.2
    scene bg03DAY_ex:
        align (0.5, 0.5)
    with dissolve
    pause 0.2
    show ich02A 001:
        align (0.8, -0.7)
    show chi01A 001:
        align (0.03, -1.6)
    with dissolve
    voice "voice/chi/ich_a000007.ogg"
    ich "お礼の分くらい、お店で出すよ？"
    show chi01A 602:
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.1 xoffset 0
    with dissolve
    voice "voice/chi/chi_a000037.ogg"
    chi "いえ、自分から言ってチラシ配りをやらせてもらったのに、お店にご迷惑はかけられませんから"
    show ich02A 701:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000008.ogg"
    ich "もう、千絵莉ちゃんは頑固なんだから"
    window hide
    with dissolve
    scene white
    with dissolve
    pause 0.3
    scene ev201a:
        align (0.5, 0.5)
    show f_kaisou
    with dissolve
    "じゃあ、あのチラシ配りは自発的に始めたことなんだ。"
    "緊張してたし、１人でチラシ配りなんてきっと得意じゃないだろうに。"
    yx_no "（すごいな、千絵莉ちゃんは）"
    "僕より年下なのにしっかり者で、頑張り屋で、頭が下がるような思いだ。"
    scene bg02DAY:
        align (0.5, 0.5)
    with pixellate
    pause 2.0
    show nan01A 002:
        align (0.52, -0.2)
        alpha 0.0
        xpos 0.51
        parallel:
            linear 0.6 alpha 1.0
        parallel:
            easeout 0.6 xpos 0.52
    voice "voice/chi/nan_a000001.ogg"
    w "備品の整理、一通りやっといたぞー"
    scene bg02DAY_br:
        align (0.71, 0.45)
    with dissolve
    pause 0.5
    show nan11A 001 zorder 99:
        align (0.75, 0.3)
    with dissolve
    show white:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos -0.125
        yanchor 0
        linear 0.5 ypos 0
    show white_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 1.0
        yanchor 0
        linear 0.5 ypos 0.875
    "また店員さんが奥から出てきた。"
    "千絵莉ちゃんや苺華さんとは雰囲気が違って、どこか凛々しさも感じる面立ちだ。"
    show white:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0
        yanchor 0
        linear 0.5 ypos -0.125
    show white_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0.875
        yanchor 0
        linear 0.5 ypos 1.0
    hide nan11A
    with dissolve
    pause 0.5
    scene bg02DAY:
        align (0.5, 0.5)
    show ich01A 105:
        align (0.5, -0.85)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000009.ogg"
    ich "ありがとう、ナナちゃん"
    hide ich01A
    show chi01A 001:
        align (0.03, -1.6)
    show nan02A 702:
        align (0.91, -0.15)
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.1 xoffset 0
        pause 4.2
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000002.ogg"
    nan "ふぃ～、筋肉痛になりそうだぜ。……ん？　千絵莉、もうチラシ配り終わったのか"
    hide nan02A
    show nan02A 101:
        align (0.91, -0.15)
    show chi01A 302:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000038.ogg"
    chi "実は、トラブルがありまして……"
    hide nan02A
    show nan01A 103:
        align (0.9, -0.18)
    with dissolve
    voice "voice/chi/nan_a000002.ogg"
    nan "あははっ。だから付いてってやろーか、って言ったじゃねーか"
    hide chi01A
    show chi02A 702:
        align (0.17, -1.9)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_POYOYON.ogg"
    voice "voice/chi/chi_a000039.ogg"
    chi "チラシ配りなんてめんどくせー、って言ってたのはナナ先輩じゃないですか"
    hide nan01A
    show nan02A 001:
        align (0.91, -0.15)
        pause 1.7
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000004.ogg"
    nan "そうだっけ？　ま、細かいことは気にすんな"
    hide nan02A
    hide chi02A
    with dissolve
    pause 0.5
    scene bg02DAY_br:
        align (0.5, 0.5)
    show nan11A 102:
        align (0.75, 0.3)
    with dissolve
    "ナナさん……かな？"
    "先輩って呼ばれているけど、真面目な千絵莉ちゃんとは対照的な印象だ。"
    scene bg02DAY:
        align (0.5, 0.5)
    show nan01A 103:
        align (0.9, -0.18)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    show chi02A 702:
        align (0.17, -1.9)
    with dissolve
    voice "voice/chi/nan_a000005.ogg"
    nan "んじゃ、気ままにカフェメニューの練習でもするかね"
    show chi02A 703:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000040.ogg"
    chi "自分で飲みたいだけじゃないですか。それにお客様の前ですよ"
    hide chi02A
    hide nan01A
    show chi01A 602:
        align (0.03, -1.6)
    show nan02A 001:
        align (0.91, -0.15)
        pause 1.0
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000006.ogg"
    nan "え？　あ、ホントだ"
    show nan02A 002
    with dissolve
    "お客さんがいないと思っていたのか、今気付いたらしい。"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.5, 0.5)
    show nan12A 002:
        align (0.75, 0.25)
    with dissolve 
    yx "あ、お構いなく"
    show nan12A 702:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve 
    play sound "se/SE_POYOYON.ogg"
    voice "voice/chi/nan_a000007.ogg"
    nan "いや客だろ。構われろよ"
    yx "あはは……そうでした"
    "本日二度目のやりとり。僕にはお客さんの自覚が足りないのかもしれない。"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    show chi01A 201:
        align (0.03, -1.6)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    show nan02A 702:
        align (0.91, -0.15)
    with dissolve
    voice "voice/chi/chi_a000041.ogg"
    chi "ナナ先輩、お客様に失礼ですよっ"
    yx "別に大丈夫だよ。歳は近いみたいだし"
    hide chi01A with dissolve
    show nan02A 102 with dissolve:
        easeout 0.5 xpos 0.72
    voice "voice/chi/nan_a000008.ogg"
    nan "見たことない顔だな。学校どこ？"
    yx "今日からこの町に引っ越してきたんだ。学校は北の方の……"
    hide nan02A
    show nan01A 401:
        align (0.51, -0.18)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_COMEDY_a.ogg"
    voice "voice/chi/nan_a000009.ogg"
    nan "マジで？　偏差値けっこう高いじゃねーか"
    yx "そうなの？　転校だから、偏差値とかよくわからないんだけど"
    "転入試験はもちろん受けたけど、父さんにここに行けって言われただけだから、この辺の学校のことはよく知らない。"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.24, 0.45)
    show chi12A 401:
        align (-0.36, 0.25)
    with dissolve
    "だけど千絵莉ちゃんもちょっと驚いてるみたいだし、きっとナナさんの言ってることが正しいんだろう。"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    show chi01A 002:
        align (0.03, -1.6)
    show nan01A 401:
        align (0.9, -0.18)
    with dissolve
    yx "ちなみに学年は２年だよ"
    show nan01A 101:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_KIRAN.ogg"
    voice "voice/chi/nan_a000010.ogg"
    nan "お、じゃああたしと苺華と同じじゃねーか。ちなみに千絵莉は１つ下な"
    hide chi01A
    show chi02A 702:
        align (0.17, -1.9)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000042.ogg"
    chi "人の個人情報をさらっと漏らさないでください。まぁ、大丈夫だとは思いますけど"
    hide chi02A
    show chi01A 303:
        align (0.03, -1.6)
    show nan01A 001
    with dissolve
    voice "voice/chi/nan_a000011.ogg"
    nan "ちなみに苺華っていうのは向こうの――"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.705,0.45)
    show ich12A 001:
        align (0.5, 0.29)
    voice "voice/chi/ich_a000010.ogg"
    ich "ナナちゃん、どうかした？"
    "呼ばれた気配がしたのか、苺華さんまでこっちにやって来た。"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    show nan02A 103:
        align (0.56, -0.18)
    with dissolve
    show ich01A 101:
        align (0.97, -0.85)
        alpha 0.0
        xpos 0.98
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easeout 0.5 xpos 0.97
    pause 0.5
    voice "voice/chi/nan_a000012.ogg"
    nan "こいつ、今日引っ越してきて、あたしたちと学年同じだってさ"
    hide ich01A
    show ich02A 701:
        align (0.94, -0.7)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_KOKE_b.ogg"
    voice "voice/chi/ich_a000011.ogg"
    ich "こいつって、もう友達みたいに……"
    show ich02A 102:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000012.ogg"
    ich "ふふっ、でも奇遇ですね"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.705,0.45)
    show ich11A 102:
        align (0.7, 0.25)
    with dissolve
    play sound "se/SE_FLOWER_b.ogg"
    "苺華さんがにこりと笑うと、花が咲くようだ。"
    "苺華さん目当てで通う客がいてもおかしくないと、ちょっと思った。"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    show nan01A 103:
        align (0.13, -0.18)
    show ich01A 101:
        align (0.83, -0.85)
    with dissolve
    voice "voice/chi/nan_a000013.ogg"
    nan "ま、何の変哲もない喫茶店だが、ゆっくりしていってくれ"
    hide ich01A
    show ich02A 105:
        align (0.8, -0.7)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000013.ogg"
    ich "良かったらまた来てください"
    yx "うん、そうさせてもらうね"
    "ナナさんのざっくばらんな雰囲気のおかげで僕も話しやすい。"
    window hide
    with dissolve
    scene bg02DAY_ex with mask003a:
        align (0.25, 0.5)
    show chi01A 303:
        align (-0.2, -1.85)
    with dissolve
    "……千絵莉ちゃんは後ろで申し訳なさそうな顔をしているけど。"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.235, 0.45)
    show chi11A 301:
        align (0.5, 0.2)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000043.ogg"
    chi "すみません、ナナ先輩ったらお客様に……"
    yx "大丈夫、本当に気にしてないから。千絵莉ちゃんもそんなにかしこまらなくていいんだよ？"
    show chi11A 601:
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.1 xoffset 0
    with dissolve
    play sound "se/SE_KYUPIN.ogg"
    voice "voice/chi/chi_a000044.ogg"
    chi "いえ、ご迷惑おかけしましたし、そんなわけにはいきません"
    "出会ってちょっとしか経ってないけど、やっぱり千絵莉ちゃんは真面目だ。"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    with dissolve
    "千絵莉ちゃんはこっちが申し訳なくなるくらいペコペコ謝って、カウンターに戻っていった。"
    show black75
    with dissolve
    yx_no "（だけど、ナナさんもどこか違うような……）"
    hide black75
    with dissolve
    "店員さんの方が気になって、なんとなく見てしまう。"
    window hide
    with dissolve
    stop music
    scene bg03DAY_ex with mask024a:
        align (0.5, 0.5)
    pause 1.0
    play music "bgm/BGM103.ogg"
    show chi01A 001 zorder 99:
        align (-0.14, -1.6)
    show ich02A 001 zorder 99:
        align (0.94, -0.7)
    show nan01A 001 zorder 98:
        align (0.51, -0.18)
    with dissolve
    show black_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos -0.125
        yanchor 0
        linear 0.5 ypos 0
    show black:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 1.0
        yanchor 0
        linear 0.5 ypos 0.875
    voice "voice/chi/chi_a000045.ogg"
    chi2 "（こちらを見ていますね。何かあったんでしょうか？）"
    hide nan01A
    show nan02A 201 zorder 98:
        align (0.56, -0.15)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_KIIN.ogg"
    voice "voice/chi/nan_a000014.ogg"
    nan_no "（あぁん？　また苺華目当ての客なら追い出してやろうか）"
    show ich02A 701:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000014.ogg"
    ich_no "（ナナちゃんが追い払うから、お客さん来なくなるんじゃないのかな……？）"
    hide nan02A
    show nan01A 205 zorder 98:
        align (0.51, -0.18)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000015.ogg"
    nan_no "（苺華が優しい顔するから男どもがつけあがるんだよ）"
    show nan01A 601:
        pause 7.8
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_KYUPIN.ogg"
    voice "voice/chi/nan_a000016.ogg"
    nan_no "（特に学生の客はダメだ。金がないからって、コーヒー１杯で何時間も粘ろうとしやがる。注文しまくって居座るやつも厄介だけどな）"
    hide nan01A
    show nan02A 202 zorder 98:
        align (0.56, -0.15)
    show ich02A 701:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_KOKE_a.ogg"
    voice "voice/chi/ich_a000015.ogg"
    ich_no "（ナナちゃん手厳しい……）"
    show ich02A 001
    with dissolve
    voice "voice/chi/ich_a000016.ogg"
    ich_no "（でも誰かが目当てってことはないと思うよ。千絵莉ちゃんやナナちゃんのことも気になってるみたいだし）"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    with dissolve
    "いや、ジロジロ見るのは失礼だよね。それより注文を決めないと。"
    scene bg03DAY_ex:
        align (0.5, 0.5)
    show chi02A 001 zorder 99:
        align (0.035, -1.95)
    show ich02A 001 zorder 97:
        align (0.94, -0.7)
    show nan02A 701 zorder 98:
        align (0.56, -0.15)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    show black_bar:
        xsize 1.0
        ypos 0.0
        ysize 0.125
    show black:
        xsize 1.0
        ysize 0.125
        ypos 0.875
    with dissolve
    voice "voice/chi/nan_a000017.ogg"
    nan_no "（あれか？　注文は君たちだ、とか言ってくる気か？）"
    show chi02A 702:
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    play sound "se/SE_POYOYON.ogg"
    voice "voice/chi/chi_a000046.ogg"
    chi2 "（どこのヘンタイおじさんですか。優しそうな人ですし、それはないと思いますけど）"
    hide chi02A
    show chi01A 303 zorder 99:
        align (-0.14, -1.6)
    hide nan02A
    show nan01A 001 zorder 98:
        align (0.51, -0.18)
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10
        linear 0.1 xoffset 0
    with dissolve
    voice "voice/chi/nan_a000018.ogg"
    nan_no "（いやいや、人は見かけによらねぇぞ？　ああいうのが、いざという時ケモノになったりするんだ）"
    show nan01A 802
    hide chi01A 
    show chi02A 701 zorder 99:
        align (0.035, -1.95)
    with dissolve
    voice "voice/chi/chi_a000047.ogg"
    chi2 "（なんでそこで得意げになるんですか。それにケモノって、私たちが言います？）"
    show chi02A 601
    hide ich02A
    show ich01A 402 zorder 97:
        align (0.97, -0.85)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000017.ogg"
    ich_no "（ケモノ……もしかして）"
    hide nan01A
    show nan02A 002 zorder 98:
        align (0.56, -0.15)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset -20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000019.ogg"
    nan_no "（ん？　どうした？）"
    show ich01A 403 zorder 97:
        align (0.97, -0.85)
        pause 4.0
        xoffset 0
        yoffset 0
        parallel:
            linear 0.5 xoffset -74
        parallel:
            linear 0.1 yoffset -5
            linear 0.1 yoffset 5
            linear 0.05 yoffset 0
            linear 0.1 yoffset -5
            linear 0.1 yoffset 5
            linear 0.05 yoffset 0
        linear 0.1 yoffset -5
        linear 0.1 yoffset 5
        linear 0.05 yoffset 0
    with dissolve
    voice "voice/chi/ich_a000018.ogg"
    ich_no "（もしかして……もしかするとだけど……ごにょごにょ）"
    show nan02A 401:
        pause 0.5
        yoffset 0
        linear 0.05 yoffset -5 
        linear 0.05 yoffset 5
        linear 0.025 yoffset 0
    with dissolve
    play sound "se/SE_GAAN_a.ogg"
    voice "voice/chi/nan_a000020.ogg"
    nan_no "（えっ！？　マジで？）"
    hide chi02A
    show chi01A 302 zorder 99:
        align (-0.14, -1.6)
        pause 0.5
        yoffset 0
        linear 0.2 yoffset 20
        linear 0.2 yoffset 0
    with dissolve
    voice "voice/chi/chi_a000048.ogg"
    chi_no "（そ、そんなはずは……）"
    window hide
    with dissolve
    hide chi01A
    hide nan02A
    hide ich01A
    show black_bar:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0
        yanchor 0
        linear 0.5 ypos -0.125
    show black:
        xpos 0
        xanchor 0
        xsize 1.0
        ysize 0.125
        ypos 0.875
        yanchor 0
        linear 0.5 ypos 1.0
    with dissolve
    pause 1.0
    scene bg02DAY:
        align (0.5, 0.5)
    with dissolve
    yx "あんまり高いメニューにするのは気が引けるし……うん、オリジナルブレンドでいいかな"
    yx "すいま――"
    show chi02A 301:
        align (0.485, -1.95)
    with dissolve
    "店員さんを呼ぼうとすると、すでに千絵莉ちゃんが近くに来ていた。"
    "注文を聞きに来てくれたのかと思ったけど、それにしては表情が険しい。"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.5, 0.5)
    show chi11A 302:
        align (0.5, 0.25)
    with dissolve
    yx "千絵莉ちゃん？　何かあった？"
    show chi11A 303
    with dissolve
    voice "voice/chi/chi_a000049.ogg"
    chi "あの、変なことをお聞きするかもしれないんですけど……"
    camera:
        yoffset 0    # 初始：画面偏上（显示背景上半部分）
        linear 1.5 yoffset 200
    "そう言って、自分の頭を指さして――"
    hide chi11A
    show chi12A 301:
        align (0.35, 0.25)
    with dissolve
    stop music
    voice "voice/chi/chi_a000050.ogg"
    chi "もしかして、この耳、見えてますか……？"
    yx "……え？"
    "耳？　耳なんて普通は見えるものじゃ……"
    camera:
        align (0.5, 0.2)
        linear 0.6 zoom 1.15
    yx "……"
    "耳。……耳。"
    yx "…………"
    window hide
    with dissolve
    camera:
        reset
    scene bg02DAY:
        align (0.5, 0.5)
    with dissolve
    "うん、耳だ。"
    "見るからに触り心地が良さそうな猫の耳が、彼女の頭から生えていた。"
    play sound "se/SE_JAAN.ogg"
    scene bg02DAY:
        align (0.5, 0.5)
        xoffset 0
        yoffset 0
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
    yx "あああーーーーーーっ！！！"
    play music "bgm/BGM104.ogg"
    yx "耳！　耳だ！　耳がある！"
    "なんとなく感じていた違和感の正体がわかった。"
    "店員さんたちにはみんな耳があったんだ。犬や猫の、動物の耳が。"
    yx "何か引っかかってたけど……あぁ～っ、耳だったんだ！"
    show nan01A 201:
        align (0.515, -0.18)
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
    with dissolve
    play sound "se/SE_BISI_a.ogg"
    voice "voice/chi/nan_a000021.ogg"
    nan "気付くのおせーよ！"
    yx "ちょっと違うなって思ってたんだけど、気のせいかなって"
    show nan01A 204:
        pause 0.5
        xoffset 0
        yoffset 0
        linear 0.1 xoffset -5 yoffset 5
        linear 0.1 xoffset 5 yoffset -5
        linear 0.1 xoffset 0 yoffset 0
    with dissolve
    voice "voice/chi/nan_a000022.ogg"
    nan "ちょっとどころじゃねーだろ！"
    yx "いや～、鈍いって人からよく言われてて"
    show nan01A 203:
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
    with dissolve
    play sound "se/SE_COMEDY_e.ogg"
    voice "voice/chi/nan_a000023.ogg"
    nan "鈍すぎだろ！　見えてるのに気づかないとか、どんだけボーっとしてんだ"
    yx "あはは……面目ない"
    "我ながら驚きの鈍さに苦笑するしかない。"
    "でもまさか、動物の耳が付いてるなんて思わなかった。"
    window hide
    with dissolve
    scene bg02DAY_br:
        align (0.71, 0.45)
    show chi11A 402:
        align (0.5, 0.25)
        pause 0.5
        xoffset 0
        linear 0.2 xoffset -10
        linear 0.2 xoffset 10 
        linear 0.1 xoffset 0 
    with dissolve
    play sound "se/SE_GAAN_a.ogg"
    voice "voice/chi/chi_a000051.ogg"
    chi "まさか、本当に見えてたなんて……"
    "ショックを受けた様子で、信じられないものを見るような目で僕を見る千絵莉ちゃん。"
    "でも、耳が見えるのってそんなに大変なことなんだろうか？"
    window hide
    with dissolve
    scene bg02DAY:
        align (0.5, 0.5)
    show nan01A 201:
        align (0.515, -0.18)
    with dissolve
    yx "その耳……コスプレ？"
    show nan01A 204:
        pause 0.5
        yoffset 0
        linear 0.15 yoffset -20
        linear 0.15 yoffset 0
        pause 2.6
        linear 0.15 yoffset 20
        linear 0.15 yoffset 0
    with dissolve
    play sound "se/SE_BISI.ogg"
    voice "voice/chi/nan_a000024.ogg"
    nan "ちげーよ！　あたしらの耳をその辺のパーティーグッズと一緒にすんじゃねえ！"
    camera: 
        shake_xyw
    play sound "se/SE_COMEDY_e.ogg"
    yx "じゃあ本物！？"