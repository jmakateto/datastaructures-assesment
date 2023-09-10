

def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack
