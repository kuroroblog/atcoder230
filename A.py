# 標準入力を受け付ける。
N = int(input())

if N >= 42:
    N += 1

# zfill参考 : https://note.nkmk.me/python-zero-padding/
print('AGC' + str(N).zfill(3))
