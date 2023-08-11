import whisper
import datetime
import sys 


# ファイルの取り込み
path = sys.argv[1]
# モデルのモード選び(精度が上がる)
model_names = ["tiny", "base", "small", "medium", "large"]
model = whisper.load_model(model_names[0])
# 読み込み(verbose=Trueにすると時刻のログが出る)
result = model.transcribe(path, verbose=False, language='ja')

# 会話ログをtxtファイルに書き出し(タイムスタンプ有)
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
f = open(f"台本/{now.strftime('%Y%m%d%H%M%S')}.txt", 'x')
for seg in result["segments"]:
  start = datetime.timedelta(seconds=int(seg["start"]))
  end = datetime.timedelta(seconds=int(seg["end"]))
  f.write(f'{start}-{end} {seg["text"]}\n')
f.close()