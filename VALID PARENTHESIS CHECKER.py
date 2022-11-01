def para_check(s):
    loop = len(s)
    x = 0
    check_box = []
    while loop > 0:
        if s[x] == "(" or s[x] == ")" or s[x] == "[" or s[x] == "]" or s[x] == "{" or s[x] == "}":
            check_box.append(s[x])
            loop = loop-1
            x = x + 1
        else:
            loop = loop-1
            x = x+1
    return check_box


def checker(check_box):
    loop = len(check_box)
    x = 0
    checker = []
    while loop > 0:
        if check_box[x] == "(" or check_box[x] == "[" or check_box[x] == "{":
            checker.append(check_box[x])
            check_box.pop(x)
            loop = loop-1
        elif check_box[x] == ")" and "(" in checker:
            checker.pop()
            check_box.pop(x)
            loop = loop-1

        elif check_box[x] == "]" and "[" in checker:
            checker.pop()
            check_box.pop(x)
            loop = loop-1
        elif check_box[x] == "}" and "{" in checker:
            checker.pop()
            check_box.pop(x)
            loop = loop-1
        else:
            return False
    if len(check_box) == 0:
        return True

s="(Hi[He Said] i am {insert name})"
check_box = para_check(s)
checker(check_box)
