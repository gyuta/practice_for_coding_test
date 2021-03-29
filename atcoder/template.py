def main():
  pass()

from sys.stdin import readline

def getStrInput():
  return readline().rstrip()

def bitFullSearch(_list, allowEmpty = True):
  """ bit全探索
   _list の可能な組み合わせを全て列挙する
   各要素について選ぶか選ばないかの 2 通りあるため、リストの長さをnとすると 2^n 個返す

   allowEmpty が False なら全ての要素を選ばない物を省く。つまり、2^n -1 個になる
  """

  n = len(_list)
  start = 0 if allowEmpty else 1
  for bit in range(start, 2**n):
    container = []
    for i in range(n):
      if bit & 1 << i:
        container.append(_list[i])
    yield container

if __name__ == '__main__':
  main()

