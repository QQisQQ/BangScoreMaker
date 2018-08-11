## BangScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/BangScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://github.com/yp05327/BangScoreMaker#)

[中文](https://github.com/yp05327/BangScoreMaker/blob/master/README_CN.md)

[日本語](https://github.com/yp05327/BangScoreMaker/blob/master/README_JP.md)

# Introduction 
This is a tool for Bang Dream! Now i just finished one part of it. If you have some good ideas, and want to share to me, you can add issues at [here](https://github.com/yp05327/BangScoreMaker/issues).

Support Features:
 ```
auto make score pictures(from official score files)
```

# Update Record
[Click here](https://github.com/yp05327/BangScoreMaker/blob/master/update.md)

# How to use
1、You need to install the running environment.This program is written by Python, so you need to install Python first.You can get Python [here](https://www.python.org/downloads/). Version 3.6 is recommended.

And after installed Python, open the console, install requirements.

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、Download source code. 

3、Put the music score file into 'musiccore' folder.

*4、Put textures into 'images' folder.

There are 4 types of notes:

```
note_flick.png
note_long.png
note_normal.png
note_skill.png
```

5、Open the console and turn to the folder of the source code, run:

```shell
python main.py (music score file's name)

for example: if the music score file's name is 'yes_bang_dream_expert.txt',

then

python main.py yes_bang_dream_expert.txt
```

Note:
1、In step 4, to avoid copyright infringement, I won't upload the textures.

2、Output is a temp file, i won't add any save features. So if you want to save it, please do that by yourself.

# Bug report or advise

[Click here](https://github.com/yp05327/BangScoreMaker/issues)