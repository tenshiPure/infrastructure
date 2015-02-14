#fabric
##インストール
```Bash
$ sudo eash_install fabric
$ fab -V
Fabric 1.10.1
Paramiko 1.15.2
```
##主なメソッド
```Python
# ローカルでsh実行
local('echo hello')

# リモートでsh実行
run('whoami')

# リモートでsh実行
sudo('whoami')

# ファイル転送
get('from', 'to')
```
##主なコマンド
###実行
```Bash
$ fab {task, [task...]}
```
###タスク一覧
```Bash
$ fab -l
Available commands:

    setup
    deploy
    test
```
##主なメソッド
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
#envassert
##インストール
```Bash
$ sudo pip install envassert
```
#ディレクトリ構成
```Bash
$ tree

.
├── README.md
├── fabfile
│   ├── __init__.py         => ルートfabfile.py　各クラスのインポート
│   ├── modules             => 部品群　基本的にはconstruct, deploy, testと対
│   │   ├── __init__.py
│   │   ├── construct.py
│   │   ├── decorator.py
│   │   ├── deploy.py
│   │   └── test.py
│   ├── vagrant_1           => サーバ単位　基本的にはconstruct, deploy, test
│   │   ├── __init__.py     => サーバのSSH設定等
│   │   ├── construct.py
│   │   ├── deploy.py
│   │   └── test.py
│   └── vagrant_2
│       ├── __init__.py     => サーバのSSH設定等（ポートが違う）
│       └── construct.py    => 環境その２は手抜き
├── sample-src
│   └── index.php           => デプロイするダミープログラム
├── vagrant_1               => 試運転環境の作成（その１）
│   ├── Vagrantfile
│   └── setup.sh
└── vagrant_2               => 試運転環境の作成（その２）
    └── Vagrantfile
```
```Bash
$ fab -l                                                                                                                                                                                             master
Available commands:

    vagrant_1.construct.full
    vagrant_1.construct.minimum
    vagrant_1.deploy.php
    vagrant_1.test.full
    vagrant_1.test.minimum
    vagrant_2.construct.dev
    vagrant_2.construct.test
    vagrant_2.construct.prod
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
