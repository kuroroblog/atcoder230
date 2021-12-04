# 標準入力を受け付ける。
S = input()

N = len(S)

# Sの文字列の長さが1の場合を考える。`x`が出ても`o`が出てもTの部分文字列になるので、`Yes`と出力する。
if N == 1:
    print('Yes')
    exit()

# Sの文字列の長さが2の場合を考える。Sの1文字目, 2文字目に`o`が出た場合に、Tの部分文字列にならないので、`No`と出力する。それ以外の場合は、`Yes`と出力する。
if N == 2:
    if S[0] == 'o' and S[1] == 'o':
        print('No')
        exit()
    else:
        print('Yes')
        exit()

# Sの文字列の長さが3以上の場合を考える。Sの1文字目の値に応じて、Sの2文字目, Sの3文字目が正しいかどうか検証する。
first = S[0]
second = S[1]
third = S[2]

# Sの1文字目が`o`の時、Sの2文字目, 3文字目のどちらかで`o`が出るとTの部分文字列にならないので、`No`と出力する。
if first == 'o' and (second == 'o' or third == 'o'):
    print('No')
    exit()

# Sの1文字目が`x`の時、Sの2文字目, 3文字目がどちらも`o`の場合、もしくはSの2文字目, 3文字目がどちらも`x`の場合に、Tの部分文字列にならないので、`No`と出力する。
if first == 'x' and ((second == 'o' and third == 'o') or (second == 'x' and third == 'x')):
    print('No')
    exit()

# Sの4文字目以降について考える。Sの1~3文字目の繰り返しになっているか確かめる。
for i in range(3, N):
    if i % 3 == 0 and first != S[i]:
        print('No')
        exit()

    if i % 3 == 1 and second != S[i]:
        print('No')
        exit()

    if i % 3 == 2 and third != S[i]:
        print('No')
        exit()

print('Yes')
