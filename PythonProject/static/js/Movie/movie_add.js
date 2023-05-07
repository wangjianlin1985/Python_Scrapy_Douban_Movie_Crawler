$(function () {
	//实例化剧情简介编辑器
    tinyMCE.init({
        selector: "#movie_intro",
        theme: 'advanced',
        language: "zh",
        strict_loading_mode: 1,
    });
	$("#movie_url").validatebox({
		required : true, 
		missingMessage : '请输入豆瓣地址',
	});

	$("#movie_title").validatebox({
		required : true, 
		missingMessage : '请输入电影名称',
	});

	$("#movie_director").validatebox({
		required : true, 
		missingMessage : '请输入导演',
	});

	$("#movie_screenwriter").validatebox({
		required : true, 
		missingMessage : '请输入编剧',
	});

	$("#movie_actors").validatebox({
		required : true, 
		missingMessage : '请输入主演',
	});

	$("#movie_category").validatebox({
		required : true, 
		missingMessage : '请输入类型',
	});

	$("#movie_country").validatebox({
		required : true, 
		missingMessage : '请输入国家',
	});

	$("#movie_langrage").validatebox({
		required : true, 
		missingMessage : '请输入语言',
	});

	$("#movie_initial").validatebox({
		required : true, 
		missingMessage : '请输入上映日期',
	});

	$("#movie_runtime").validatebox({
		required : true, 
		missingMessage : '请输入片长',
	});

	$("#movie_rate").validatebox({
		required : true, 
		missingMessage : '请输入豆瓣评分',
	});

	$("#movie_starPeople").validatebox({
		required : true, 
		missingMessage : '请输入评价人数',
	});

	$("#movie_icon").validatebox({
		required : true, 
		missingMessage : '请输入海报图片',
	});

	//单击添加按钮
	$("#movieAddButton").click(function () {
		//验证表单 
		if(!$("#movieAddForm").form("validate")) {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		} else {
			$("#movieAddForm").form({
			    url:"/Movie/add",
				queryParams: {
			    	"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
				},
			    onSubmit: function(){
					if($("#movieAddForm").form("validate"))  { 
	                	$.messager.progress({
							text : "正在提交数据中...",
						}); 
	                	return true;
	                } else {
	                    return false;
	                }
			    },
			    success:function(data){
			    	$.messager.progress("close");
                    //此处data={"Success":true}是字符串
                	var obj = jQuery.parseJSON(data); 
                    if(obj.success){ 
                        $.messager.alert("消息","保存成功！");
                        $(".messager-window").css("z-index",10000);
                        $("#movieAddForm").form("clear");
                        tinyMCE.editors['movie_intro'].setContent("");
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    }
			    }
			});
			//提交表单
			$("#movieAddForm").submit();
		}
	});

	//单击清空按钮
	$("#movieClearButton").click(function () { 
		//$("#movieAddForm").form("clear"); 
		location.reload()
	});
});
