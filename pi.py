text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

splited_list = text.split()                                    # "text"を空白で分割

char_list = [None] * len(splited_list)                         # リスト"splited_list"の要素数(len(splited_list))と同じ要素数のリストを用意

for i in range(len(splited_list)):
    char_list[i] = splited_list[i].strip(",").strip(".")       # カンマとピリオドを削除

char_num_list = list(map(len, char_list))           # char_listの各要素の文字数を取得

char_num_list_str = [str(a) for a in char_num_list] # .join()を使うために、リスト内の値をint値からstr値に変換

char_num_line = "".join(char_num_list_str)          # .join()を用いてリストの要素を並べて表示

print(type(char_num_line))                          # 出力されたものが文字列(str値)であるか確認
print(char_num_line)                                # 文字数を並べた文字列を出力
