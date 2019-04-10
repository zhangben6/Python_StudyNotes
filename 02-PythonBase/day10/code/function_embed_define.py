# function_embed_define.py

# 此示例示意在函数内部创建函数，在函数内部来调用
def fn_outer():
    print("fn_outer被调用")

    def fn_inner():
        print("fn_inner被调用")

    fn_inner()
    fn_inner()
    fn_inner()

    print("fn_outer调用结束")

fn_outer()
# fn_inner()  # 调用出错