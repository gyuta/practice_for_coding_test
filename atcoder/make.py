# コンテスト用にフォルダを生成するスクリプト
from os import mkdir
from sys import exit

def main():
  contest_name = getStrInput()
  makeDir(contest_name)

  problems = getStrListInput()
  makeFiles(contest_name, problems)


def makeDir(name: str) -> None:
  try:
    mkdir(name)
  except FileExistsError:
    print('the directory already exists!')
    exit(1)
  return None

def makeFiles(dir: str ,names: list[str]) -> None:
  for name in names:
    with open(dir + '/' + name + '.py', 'w') as f:
      pass
  return None

def formatInput(expr):
  def decorator(func):
    def inner():
      print(expr)
      tmp = func()
      print()
      return tmp
    return inner
  return decorator

@formatInput('Input contest title. ex) abc197 agc116')
def getStrInput():
  return input().strip()

@formatInput('Input problem names you will solve. if you input \'a b c\', a.py b.py c.py will be created.')
def getStrListInput():
  return list(input().split())

if __name__ == '__main__':
  main()

