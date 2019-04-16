$(function (){
	countItem();
	//1. 全选和取消全选
	var isChecked = false;
	$("#checkAll").click(function (){
		isChecked = !isChecked;
		if(isChecked){
			//获取商品信息中的按钮,更改选中状态
			$("[name=check]").prop("checked","true");
		}else{
			//取消全选
			$("[name=check]").removeAttr("checked");		
		}
		countItem();
	})
	//2. 反选-商品选择状态改变全选按钮
	$("[name=check]").change(function (){
		//onchange 监听按钮状态改变
		//商品按钮如果全选中,修改全选按钮
		//只要有一个商品按钮未被选中,全选也不能选中
		//未被选中的按钮数量 == 0 -> 全选
		//input:checked 表示被选中的按钮
		//size() 获取元素数量 length
		if($("[name=check]").not("input:checked").size() == 0){
			//全选
			$("#checkAll").prop("checked","true");
			isChecked = true;
		}else{
			$("#checkAll").removeAttr("checked");
			isChecked = false;
		}
		countItem();
	})
	
	//3. 数量加减
	$('.add').click(function (){
		//取前一个兄弟元素的文本内容
		var value = Number($(this).prev().val());
		//var res = value ++;
		$(this).prev().val(++value);
		//价格联动
		//单价
		var priceStr = $(this).parent().prev().html(); //$188
		//数值
		var price = Number(priceStr.substring(1));
		//小计 <b>&yen;188</b>
		$(this).parent().next().html("<b>&yen;"+value*price+"</b>");
		countItem();
	})
	$(".minus").click(function (){
		//取后一个兄弟元素
		var value = Number($(this).next().val());
		//value > 1才能做减法
		if(value > 1){
			$(this).next().val(--value);
		}
		//价格联动
		//单价
		var priceStr = $(this).parent().prev().html(); //$188
		//数值
		var price = Number(priceStr.substring(1));
		//小计 <b>&yen;188</b>
		$(this).parent().next().html("<b>&yen;"+value*price+"</b>");
		countItem();
	})
	//输入数量,失去焦点时价格联动
	$(".count input").blur(function (){
		//数量
		var value = Number($(this).val());
		//单价
		var priceStr = $(this).parent().prev().html(); //$188
		//数值
		var price = Number(priceStr.substring(1));
		//小计 <b>&yen;188</b>
		$(this).parent().next().html("<b>&yen;"+value*price+"</b>");
		countItem();
	})
	//4. 移除商品
	$(".g-item .action").click(function (){
		//点击哪个商品栏,移除当前信息
		$(this).parent().remove();
		countItem();
	})
	
	//5. 总价格和总数量计算
	function countItem(){
		var sum = 0;
		var sumPrice = 0;
		//1. 获取被选中的商品
		$("[name=check]:checked").each(function (){
			//获取当前商品的数量和小计
			//.g-item ->.count .sum
			sum += Number($(this).parents(".g-item").find(".count input").val());
			var priceStr = $(this).parents(".g-item").find(".sum b").html();
			var price = Number(priceStr.substring(1));
			sumPrice += price;
		})
		//2. 显示在工具栏
		$(".submit-count span").html(sum);
		$(".submit-price span").html("&yen;"+sumPrice);
	}
})