

'''def safe_divide(a,b):
    if b == 0:
        return "Error"
    
    return a/b

print(safe_divide(1000,100))

def maximum(a,b):
    try:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return a
    except:
        ValueError

print(maximum(1,1))
print(maximum(2,3))'''
"""
def check(a,b):
    if a > 0:
        if b > 0:
            return "both positive"
        else:
            return "a positive only"
    else:
        if b > 0:
            return "b positive only"
        else:
            return "both negative"

print(check(1,-1))
"""

"""
def large_x(x):
    if x > 10:
        if x % 2 == 0:
            print("large even")
        else:
            print("large odd")
    else:
        print("small")
"""

def password_length(x):
    if len(x) >= 8:
        return "valid"
    else:
        return "not valid"

"""   
temp > 100
60 < temp <= 100
temp <= 60 """