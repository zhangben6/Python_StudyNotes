
# file : mypack/games/contra.py

def play():
    print("正在玩魂斗罗....")

def gameover():
    # 调用mypack/menu.py里的show_menu

    # 1. 用绝对导入方式导入
    # from mypack.menu import show_menu
    # show_menu() 

    # 2. 用相对导入方式导入
    from ..menu import show_menu
    show_menu()

    # 调用mypack/games/tanks.py 里的play()
    # 1. 绝对导入
    # from mypack.games.tanks import play
    # 2. 相对导入
    # from .tanks import play
    from ..games.tanks import play
    # from ...mypack.games.tanks import play # 出错

    play()


print("魂斗罗模块被加载")


