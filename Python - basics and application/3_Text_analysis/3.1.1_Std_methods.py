
def replace_str(line, sub_old, sub_new):
    count = 0
    i = 0
    if sub_old not in line:
        return count

    line_tmp = line
    while i < 1001:
        line_new = line_tmp.replace(sub_old, sub_new)
        if line_tmp != line_new:
            line_tmp = line_new
            count += 1
        elif line_tmp == line_new and sub_old not in line_tmp:
            return count

        i += 1
    else:
        return "Impossible"



s, a, b = input(), input(), input()
print(replace_str(s, a, b))


# print("c" in "abc")