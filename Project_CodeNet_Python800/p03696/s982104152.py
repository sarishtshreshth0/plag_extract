def abc064_d():
  _ = int(input())
  s = str(input())
  # 後ろから見ていく
  srev = s[::-1]
  # 開きカッコ閉じカッコの個数(追加分を含む)
  op, cl = 0, 0
  # 追加したものを入れる
  f, r = '', ''
  for c in srev:
    if c == '(': op += 1
    else: cl += 1
    # 開きカッコが先行したら、都度、閉じカッコを末尾に追加
    if op > cl:
      r += ')'
      cl += 1
  else:
    # 先頭に開きカッコを足す
    f += '(' * (cl - op)
  # 元の文字列sにfとrを足す
  ans = f + s + r
  print(ans)

abc064_d()