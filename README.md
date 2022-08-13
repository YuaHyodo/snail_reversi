# snail_reversi
カタツムリのようにとてもとても遅いリバーシのライブラリ

# 概要
- リバーシ(オセロ)を自力実装した。(未完成)
- Pythonの標準ライブラリさえimportしていない。(今のところは)
- 大変汚い実装・驚異的遅さ・そして低機能

# 想定している使い道
- 探索部・機械学習のような速度が非常に重要な部分ではなく、対局サーバーやGUIでの合法手チェックなどの部分に使用する事を想定して設計している。
- 速度が欲しい方は、creversi( https://github.com/TadaoYamaoka/creversi )あたりを使う事を強く推奨する。

# 皆さんのPCで使えるようにする方法
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
