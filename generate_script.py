import whisper
import datetime
import sys 
import os
sys.stdout.reconfigure(encoding='utf-8')


def main():
    # ファイルの取り込み
    files = sys.argv[1:]
    # モデルのモード選び(精度が上がる)
    model_names = ["tiny", "base", "small", "medium", "large"]
    model_level = int(input("モデルのサイズを1~5で選択してください：")) - 1
    print("モデル読み込み中")
    model = whisper.load_model(model_names[model_level])
    print("モデル読み込み完了")

    # 全てのファイルに対して台本を生成
    for i, file in enumerate(files):
        # 読み込み(verbose=Trueにすると時刻のログが出る)
        print(f"台本生成中")
        result = model.transcribe(file, verbose=False, language='ja')
        print(f"台本生成完了 {i+1}/{len(files)}")
        # 台本ファイルの生成
        file_name = os.path.basename(file)
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        f = open(f"台本/{file_name}_{now.strftime('%Y%m%d%H%M%S')}.txt", 'x')
        for seg in result["segments"]:
            start = datetime.timedelta(seconds=int(seg["start"]))
            end = datetime.timedelta(seconds=int(seg["end"]))
            f.write(f'{start}-{end} {seg["text"]}\n')
        f.close()

if __name__ == "__main__":
    main()