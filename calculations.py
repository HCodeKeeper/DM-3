from enum import Enum

class Form(Enum):
    PDNF = 1
    PCNF = 0


def dual(func: list) -> list:
    dual_func = []
    for i, elem in enumerate(func):
        if elem == 1:
            dual_func.append(0)
        else:
            dual_func.append(1)
    for i in range(len(func)//2):
        temp = dual_func[i]
        dual_func[i] = dual_func[len(func) - i - 1]
        dual_func[len(func) - i - 1] = temp
    return dual_func


def _form(x: list, y: list, z: list, func: list, depend_value: int) -> str:
    result = ""
    
    for i, elem in enumerate(func):
        if elem == int(not bool(depend_value)):
            continue

        if x[i] == depend_value:
            result += "x"
        else:
            result += "x\'"
        if y[i] == depend_value:
            result += "y"
        else:
            result += "y\'"
        if z[i] == depend_value:
            result += "z"
        else:
            result += "z\'"
        if i != len(func) - 1:
            result += " v "
        
    return result


def PDNF(x: list, y: list, z: list, func: list) -> str:
    return _form(x,y,z,func, Form.PDNF.value)


def PCNF(x: list, y: list, z: list, func: list) -> str:
    return _form(x,y,z,func, Form.PCNF.value)


def polynomial(x: list, y: list, z: list, func: list) -> str:
    result = ""
    triangle = [[0 for _ in range(len(func) - i)] for i, _ in enumerate(func)] #[[8],[7]...]
    triangle[0] = func
    for i in range(1, len(triangle)):
        for j, _ in enumerate(triangle[i]):
            if triangle[i-1][j] != triangle[i-1][j+1]:
                triangle[i][j] = 1
            else:
                triangle[i][j] = 0

    coefs = [0 for i in range(len(func))]
    for i, _ in enumerate(coefs):
        coefs[i] = triangle[i][0]
    for i, _ in enumerate(func):
        if coefs[i] == 1:
            if i == 0:
                result += "1 + "
                continue
            if x[i] == 1:
                result += "x"
            if y[i] == 1:
                result += "y"
            if z[i] == 1:
                result += "z"
            if i != len(func) - 1:
                result += " + "
    
    if result == "1 + ":
        result = result[0]
    return result

def is_linear(polynomial):
    if polynomial == "" or polynomial == "1":
        return True
    return False

def is_self_dual(func: list, dual_func: list):
    for i, _ in enumerate(func):
        if func[i] != dual_func[i]:
            return False
    return True

def is_monotone(func: list):
    to_contionue = False
    for i, _ in enumerate(func):
        if to_contionue:
            to_contionue = False
            continue
        if func[i+1] < func[i]:
            return False
        if i != len(func) - 1:
            to_contionue = True
    return True

def does_contain_const0(x: list, y: list, z: list, func: list):
    for i, elem in enumerate(func):
        if elem == 0 and elem == x[i] and elem == y[i] and elem == z[i]:
            return True
    return False

def does_contain_const1(x: list, y: list, z: list, func: list):
    for i, elem in enumerate(func):
        if elem == 1 and all([x[i], y[i], z[i]]) == 1:
            return True
    return False