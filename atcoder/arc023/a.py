def main():
  N = int(getStrInput())
  t = [int(getStrInput()) for i in range(N)]

  bfs = bitFullSearch(t)
  _min = sum(t)
  for container, out in bfs.search_with_out(distinguish=False):
    _max = max(sum(container), sum(out))
    _min = min(_min,_max)
  
  print(_min)

from sys import stdin

def getStrInput():
  return stdin.readline().rstrip()

class bitFullSearch:
  def __init__(self, _list):
    self._list = _list
    self.len = len(_list)

  def search(allowEmpty = True):
    """ 基本的なbit全探索
    可能な組み合わせのリストを返すジェネレータ
    各要素について選ぶか選ばないかの 2 通りあるため、リストの長さをnとすると 2^n 個返す

    例えば _list = [1, 2, 3] なら [], [1], [2], [1, 2], [3], ... のように値が帰っていく

    allowEmpty が False なら [] を省く
    """

    n = self.len
    start = 0 if allowEmpty else 1
    for bit in range(start, 2**n):
      container = []
      for i in range(n):
        if bit & 1 << i:
          container.append(self._list[i])
      yield container
  
  def search_with_out(self, allowEmpty = True, distinguish = True) -> (list, list):
    """ 通常のbit探索に加えて、選んでない組み合わせのリストも返す
    帰り値は container(選んだもの), out(選んでないもの) の順番

    allowEmpty が False なら [] を省く
    distinguish が False なら container と out を区別しない。つまり半分でループを終える
    """

    n = self.len
    start = 0 if allowEmpty else 1
    end = 2**n if distinguish else 2**(n-1)
    for bit in range(start, 2**n):
      container = []
      out = []
      for i in range(n):
        if bit & 1 << i:
          container.append(self._list[i])
        else:
          out.append(self._list[i])
      yield container, out


if __name__ == '__main__':
  main()
