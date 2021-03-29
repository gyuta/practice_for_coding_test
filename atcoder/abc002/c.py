def main():
  N, M = [int(x) for x in stdin.readline().rstrip().split()]

  congressmen = [i for i in range(1, N+1)]
  global dic
  dic = {i: [] for i in congressmen}
  for _ in range(M):
    x, y = [int(x) for x in stdin.readline().rstrip().split()]
    dic[x].append(y)

  bfs = bitFullSearch(congressmen)
  _max = 0
  for member in bfs.search():
    if valid(member):
      _max = max(_max, len(member))
  print(_max)

def valid(member):
  for pair in combinations(member, 2):
    if not acquaint(pair):
      return False
  return True

def acquaint(pair):
  a = pair[0]
  b = pair[1]

  return b in dic[a] or a in dic[b]

from itertools import combinations
from sys import stdin

def getStrInput():
  return stdin.readline().rstrip()

class bitFullSearch:
  def __init__(self, _list):
    self._list = _list
    self.len = len(_list)

  def search(self, allowEmpty = True):
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


if __name__ == '__main__':
  main()
