for _ in range(int(input())):
    in_string = input()
    out_string = ''
    char_stack = []
    opr_stack = []
    for i in in_string:
        if i >= 'a' and i <= 'z':
            char_stack.append(i)
        elif i == ')':
            char_stack.append(opr_stack.pop())
        else:
            if i == '(':
                continue
            opr_stack.append(i)
    print(''.join(x for x in char_stack))