
# file: mypack/games/__init__.py

# 此列表确保在from mypack.games import *时导入
# contra 和tanks模块
__all__ = ['contra', 'tanks']

print("mypack.games子包被加载")

