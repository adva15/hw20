#example 1:
def example(input_s:str) -> bool:
    input_1= {')': '(', '}': '{', ']': '['}
    examples=[]

    for char in input_s:
        if char in input_1.values():
            examples.append(char)
        elif char in input_1.keys():
            if examples and  examples[0]==input_1[char]:
                examples.pop()
                return True
            else:
                return False

print(example("()"))
print(example("{}"))
print(example("[]"))
print(example("(}"))
print(example("{]"))
print(example("()[]{}"))


