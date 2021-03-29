def main():
  pass

from sys.stdin import readline

def getStrInput():
  return readline().rstrip()

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
