
def function_len(object):
    # if type(object)==dict or type(object)==list or type(object)== str:
    a = 1
    print(type(a))
    if type(object)==dict:
        if object/2==0:
            print("True")
        else:
            print("False")
    else:
        print("请输入数值！")
object1 = print(input().format())
function_len(object1)