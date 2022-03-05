import wrap
from wrap import exec as pr

def exec(*funcs):
    if len(funcs) == 0:
        return None
    elif len(funcs) == 1:
        return funcs[0]
    elif len(funcs) == 2:
        a = pr(funcs[0])
        b = pr(funcs[1])

        return lambda x: b(a(x))
    else:
        return exec([exec(funcs[:2])].extend(funcs[2:]))