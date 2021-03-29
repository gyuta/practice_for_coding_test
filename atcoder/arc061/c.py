def main():
  S = getStrInput()
  bfs = bitFullSearch(list(S))
  _sum = 0
  for container in bfs.search_with_partition():
    nums = [int(reduce(lambda acc, cur: acc + str(cur), item, '')) for item in container]

    # print(container, nums)
    _sum += sum(nums)
  print(_sum)

from sys import stdin
from functools import reduce

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
    返り値は container(選んだもの), out(選んでないもの) の順番

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
  
  def search_with_partition(self, allowFull = True): # -> list[list] atcoderだとエラーになるのでコメントアウト
    """ リストの可能な区切り方をbit探索で得る
    要素数がnだとすると各要素間のn-1箇所に仕切りを入れるか入れないかの2通りあるため、2^(n-1)通りのパターンを列挙する

    入力が [1,2,3] なら [[1,2,3]] -> [[1],[2,3]] -> [[1,2],[3]] -> ... のように二重リストを返す
    """
    n = self.len - 1 
    start = 0 if allowFull else 1
    for bit in range(start, 2**n):
      container = []
      item = []
      for i in range(n):
        item.append(self._list[i])
        if bit & 1 << i: # 右からi番目のビットが1
          container.append(item)
          item = []

      # 一番最後の要素は上のループじゃチェックされないので常にitemに追加する
      item.append(self._list[n]) 
      container.append(item)

      yield container

if __name__ == '__main__':
  main()
