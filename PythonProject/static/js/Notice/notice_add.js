$(function () {
	//实例化公告内容编辑器
    tinyMCE.init({
        selector: "#notice_content",
        theme: 'advanced',
        language: "zh",
        strict_loading_mode: 1,
    });
	$("#notice_title").validatebox({
		required : true, 
		missingMessage : '请输入标题',
	});

	$("#notice_publishDate").datetimebox({
	    required : true, 
	    showSeconds: true,
	    editable: false
	});

	//单击添加按钮
	$("#noticeAddButton").click(function () {
		if(tinyMCE.editors['notice_content'].getContent() == "") {
			alert("请输入公告内容");
			return;
		}
		//验证表单 
		if(!$("#noticeAddForm").form("validate")) {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		} else {
			$("#noticeAddForm").form({
			    url:"/Notice/add",
				queryParams: {
			    	"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
				},
			    onSubmit: function(){
					if($("#noticeAddForm").form("validate"))  { 
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
                        $("#noticeAddForm").form("clear");
                        tinyMCE.editors['notice_content'].setContent("");
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    }
			    }
			});
			//提交表单
			$("#noticeAddForm").submit();
		}
	});

	//单击清空按钮
	$("#noticeClearButton").click(function () { 
		//$("#noticeAddForm").form("clear"); 
		location.reload()
	});
});
