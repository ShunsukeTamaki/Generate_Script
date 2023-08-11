@echo off
rem この行の下に、generate_script.py のあるディレクトリに移動するコマンドを追加
cd /d C:\Github\Generate_Script

rem Python スクリプトの実行
pipenv run python generate_script.py %*

rem 画面を開いていて欲しくない場合は、以下の行をコメントアウトもしくは削除してください
pause
