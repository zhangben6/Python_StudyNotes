L = [1, 2]

def fn(a, lst=[]):
    lst.append(a)
    print(lst)

fn(3, L)  # [1, 2, 3]
fn(4, L)  # [1, 2, 3, 4]
fn(5)  # [5]
fn(6)  # [5, 6]
fn(7)  # [5, 6, 7]
