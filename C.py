# 標準入力を受け付ける。
N, A, B = map(int, input().split())

P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    text = ''
    for j in range(R, S + 1):
        # 黒になる場合を考える。
        # <黒になる場合>
        # (A + k, B + k)が(i, j)である。もしくは(A + k, B − k)が(i, j)である。
        #
        # 上記の条件のもと、式を作成する。
        # A + k = i, B + k = j ⏩ k = i - A, k = j - B ⏩ i - A = j - B ⏩ i - j - A + B = 0の時、黒である。
        # A + k = i, B - k = j ⏩ k = i - A, k = B - j ⏩ i - A = B - j ⏩ i - A - B + j = 0の時、黒である。
        if (i - j - A + B == 0) or (i - A - B + j == 0):
            text += '#'
        else:
            text += '.'
    print(text)
