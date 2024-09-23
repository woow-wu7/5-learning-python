dataList = [1, 2, 3, 4, 5]

def fn():
    datas = [1, 2, 3, 4,5]
    for (index, value) in enumerate(datas):
        if index > 3:
            print(value)
        elif index < 1:
            print(value)
        else:
            print('other')

fn()