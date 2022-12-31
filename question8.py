#Write a program to check if all the brackets are closed in a given code snippet.

def areBracketsBalanced():
    expr = input('enter the code:')
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True



if areBracketsBalanced():
    print("All bracket closed")
else:
    print("Not Closed")