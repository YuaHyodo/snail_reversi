# snail_reversi
カタツムリのようにとてもとても遅いリバーシのライブラリ

# 概要
- リバーシ(オセロ)を自力実装した。(未完成)
- Pythonの標準ライブラリさえimportしていない。(今のところは)
- 大変汚い実装・驚異的遅さ・そして低機能
- USI-Xプロトコル(オセロ版)でのmoveやsfenに対応している。
- USI-Xプロトコル(オセロ版)についてはこちらを参照の事: https://github.com/YuaHyodo/USI-X-protocol_othello_version
- 将棋版はこちら: https://github.com/YuaHyodo/snail_shogi
- チェス版はこちら: https://github.com/YuaHyodo/Katatsumuri_Chess

# 搭載されている機能
- 合法手生成などの基本的機能
- USI-Xプロトコル(オセロ版)のmoveで着手する機能
- USI-Xプロトコル(オセロ版)のsfenで盤をセットする機能、現在の盤面に対応するsfenを取得する機能
- print(Board)で盤面を簡易的に表示する機能

# 想定している使い道
- 探索部・機械学習のような速度が非常に重要な部分ではなく、対局サーバーやGUIでの合法手チェックなどの部分に使用する事を想定して設計している。
- 以上の理由から、高速化にリソースを費やす予定は無い。
- 速度が欲しい方は、creversi( https://github.com/TadaoYamaoka/creversi )あたりを使う事を強く推奨する。

# 皆さんのPCで使えるようにする方法
- snail_reversiは、Azisai_Othello_GUI( https://github.com/YuaHyodo/Azisai_Othello_GUI )、<br>
Ari-Othello-Server( https://github.com/YuaHyodo/Ari-Othello-Server )などの実行に必要です。
- 確認した環境: windows10, Python3.8

- 注意: 間違っているやり方の可能性が非常に高い
- 間違いの指摘を大募集

## 手順
- 1: ダウンロードする
- 2: コマンドプロンプトを開く
- 3: cdコマンドでsetup.pyがあるディレクトリまで移動する
- 4: "python setup.py install"と入力してエンターキーを押す
- 5: 終わり

# ライセンス
- snail_reversiはMITライセンスです。
- 詳しくはLICENSEファイルを参照のこと。
