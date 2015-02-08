#fabric
##インストール
```Bash
$ sudo eash_install fabric
$ fab -V
Fabric 1.10.1
Paramiko 1.15.2
```
##主なコマンド
```Python
# ローカルでsh実行
local('echo hello')

# リモートでsh実行
run('whoami')

# リモートでsh実行
sudo('whoami')

# ファイル転送
put('from', 'to')

# ファイル転送
get('from', 'to')
```
##雑記
###pycファイルを作らない
```Bash
$ export PYTHONDONTWRITEBYTECODE=1
```
###pycファイルを消す
```Bash
$ find . -name “*.pyc” -exec rm {} \;
```
###pycファイルを消す（zsh）
```Bash
$ rm **/*.pyc
```
