import eel
import numpy as np
import pandas as pd


# これを書くことでJSからアクセスができます
@eel.expose
# ここからがバックエンドで行う処理
# ここに鬼滅サーチの関数を入れる
def search (keyword,path):
    call = ''
    save_path = ''
    try:
        # CSVファイルをリストに変換
        df = pd.read_csv('./web/names.csv')
        names = list(df['キャラ名'])
        # names =df.values.tolist()
        call = keyword
        path = path
        if call in names:
            result = call + 'が見つかりました'
            print(result)
        else:
            result = call + 'が見つかりませんでした'
            print(result)
            names.append(call)

        df = pd.DataFrame(names,columns=['キャラ名'])
        save_path = path
        if save_path == "":
          df.to_csv('./web/namae.csv',index=False)
        # CSVファイル作成
        else:
          df.to_csv("{}/sourse.csv".format(save_path),encoding="utf_8-sig")
    finally:
        eel.run_js_from_python(result)

# ウエブコンテンツを持つフォルダー
eel.init("web")

# 最初に表示するhtmlページ
eel.start("index.html")
