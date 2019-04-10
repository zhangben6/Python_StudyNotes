L = [1, 2]

def fn(a, lst=None):
    if lst is None:
        lst = []  # 新创建全新的列表
    lst.append(a)
    print(lst)

fn(3, L)  # [1, 2, 3]
fn(4, L)  # [1, 2, 3, 4]
fn(5)  # [5]
fn(6)  # [6]
fn(7)  # [7]
