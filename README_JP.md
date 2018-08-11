## BangScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/BangScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://github.com/yp05327/BangScoreMaker#)

[English](https://github.com/yp05327/BangScoreMaker/blob/master/README.md)
[中文](https://github.com/yp05327/BangScoreMaker/blob/master/README_CN.md)

# 紹介
これは Bang Dream! のため、作ったツールです。今そのツールの一部分が完成された。いいアイデアがあって、私に伝えたいなら、[ここ](https://github.com/yp05327/BangScoreMaker/issues)でissuesを追加してください。

完成した機能：
 ```
 自動的に譜面写真を導出する（公式譜面ファイルから）
```

# 更新記録
[こちら](https://github.com/yp05327/BangScoreMaker/blob/master/update_cn.md)

# 使い方
1、実行環境を導入する。このツールはPythonで作ったものだから、Pythonをインストールしてください。[ここ](https://www.python.org/downloads/)でPythonをダウンロードできる。バージョン3.6は推薦。

Pythonをインストールした後、コンソールでrequirementsをインストールする。

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、ソースコードをダウンロードする。

3、譜面ファイルを「musiccore」フォルダ（Folder。MARKDOWNなので、日本語は少し変になる）に入れる。

*4、テクスチャファイルを「images」。フォルダ（Folder）に入れる

ここで4タイプのノートがある：

```
note_flick.png
note_long.png
note_normal.png
note_skill.png
```

5、コンソールでソースコードのフォルダ（Folder）で、実行する：

```shell
python main.py (music score file's name)

for example: if the music score file's name is 'yes_bang_dream_expert.txt',

then

python main.py yes_bang_dream_expert.txt
```

注意事項:
1、ステップ4のところで、著作権のため、テクスチャファイルをアップロードしないようにする

2、導出されたのは一時フォルダー、保存機能を追加予定がないので、使用者は自分で保存する。

# 不具合レポートあるいは意見

[こちら](https://github.com/yp05327/BangScoreMaker/issues)