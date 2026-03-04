weight = float(input("失礼ですが、体重はkgですか？\n"))
gram = input("生の鶏むね肉を何g食べましたか？\n")
print("-"*40)
print("体重は"+str(weight)+"kgですね。")
#一日に必要なタンパク質摂取量を計算
target_p = round(weight*2)
print("あなたの体重から計算すると、")
print("筋肉を合成するために必要な一日のタンパク質量は"+str(target_p)+"gです。")
print("現在の生の鶏むね肉の摂取量は"+gram+"gですね。")
print("-"*40)
#鶏むね肉の摂取量からカロリーを計算して表示
cal = round(int(gram)*1.08)
print("総摂取カロリーは"+str(cal)+"kcalです。")
#摂取量からタンパク質量を計算
protein = round(int(gram)*0.22)
print("総タンパク質量は"+str(protein)+"gです。")
#残りのタンパク質量を計算
rest = round((target_p - protein)/0.22)
#目標達成か判定
if protein < 120:
    print("生の鶏むね肉が目標まで残り"+str(rest)+"g必要です。")
else:
    print("一日の目標を達成しました！おめでとうございます！！")
