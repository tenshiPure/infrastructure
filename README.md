##fabricのインストール
```Bash
$ sudo eash_install fabric
$ fab -V
Fabric 1.10.1
Paramiko 1.15.2
```
##雑記
###pycファイルを作らない
```Bash
$ export PYTHONDONTWRITEBYTECODE=1
```
###pycファイルを消す
```Bash
find . -name “*.pyc” -exec rm {} \;
```
###pycファイルを消す（zsh）
```Bash
rm **/*.pyc
```
