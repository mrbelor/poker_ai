import time

def display(var_name:str, nomber = None):
    nomber = str(nomber)
    
    value = globals()[var_name]
    
    print (f'[disp{nomber}]{var_name}: {value}' if nomber is not None and nomber.isdigit() else f'[disp]{var_name}: {value}')



if __name__ == '__main__':
    
    start = time.time()

    for i in range(0, 100):
        print(i, end = '')
    print()

    end = time.time()

    display('start', 1)
    display('end')
    print(end-start)


