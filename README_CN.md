## BangScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/BangScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://github.com/yp05327/BangScoreMaker#)

[English](https://github.com/yp05327/BangScoreMaker/blob/master/README.md)

[日本語](https://github.com/yp05327/BangScoreMaker/blob/master/README_JP.md)

# 介绍 
这是一个为 Bang Dream! 而写的一个工具。现在我只完成了一个部分。如果你有什么好的想法，并且愿意与我分享，你可以在[这里](https://github.com/yp05327/BangScoreMaker/issues)添加issues.

支持功能：
 ```
自动生成铺面图片（从官方的铺子文件）
```

# 更新记录
[点此查看](https://github.com/yp05327/BangScoreMaker/blob/master/update_cn.md)

# 如何使用
1、你需要安装运行环境。这个软件是用Python写的，所以你需要先安装Python。你可以在[这里](https://www.python.org/downloads/)下载Python。推荐使用3.6版本。

在安装完Python之后，打开控制台，安装requirements。

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、下载源代码。

3、把谱子文件放进 “musiccore” 文件夹。

*4、把贴图放进 'images' 文件夹。

这里有4种note文件：

```
note_flick.png
note_long.png
note_normal.png
note_skill.png
```

5、打开控制台，转到源代码所在目录下，运行：

```shell
python main.py (music score file's name)

for example: if the music score file's name is 'yes_bang_dream_expert.txt',
then
python main.py yes_bang_dream_expert.txt
```

提示:
1、在第四步，为了避免侵权，我不会上传贴图文件。

2、输出是一个临时文件，我不会添加任何保存的功能。所以如果你想要保存它，请你自己去完成。

# 问题反馈或建议

[点击此处](https://github.com/yp05327/BangScoreMaker/issues)