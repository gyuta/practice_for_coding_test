# def separate(target string) -> list<string>:
#   separated = []
#   while target.length > 0:
#     char = target[0]
#     if isChar(char): #mock
#       separated.append(char)
#       target = target[1:]
#     else 
#       num, target = getNum(target)
#       contained_str, target = get_contained_str(target)

# def print():
#   string = array_reduce()

def decompress(target):
  string = ""
    while target.len > 0:
      top = target[0]
      if top.islower():
        string += top
        target = target[1:]
      else:
        index = 0
        while true:
          index += 1
          break if not target[index].isdigit()
        num = target[:i] #check
        target = target[i:]

        left_num = 0
        right_num = 0
        index = 0
        while left_num > 0 and left_num == right_num:
          char = target[index]
          left_num += 1 if char == '['
          right_num += 1 if char == ']'
          i += 1
        new_target = gjoe
        result = decompress(new_target)
        string += result*num

        target = 

        
        
  return string





if __name__ == '__main__':
  input_str = 'a4[bc]d1[e]2[fg]'

  # separate
    
