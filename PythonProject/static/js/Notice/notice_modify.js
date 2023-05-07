$(function () {
    //实例化公告内容编辑器
    tinyMCE.init({
        selector: "#notice_content_modify",
        theme: 'advanced',
        language: "zh",
        strict_loading_mode: 1,
    });
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Notice/update/" + $("#notice_noticeId_modify").val(),
		type : "get",
		data : {
			//noticeId : $("#notice_noticeId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (notice, response, status) {
			$.messager.progress("close");
			if (notice) { 
				$("#notice_noticeId_modify").val(notice.noticeId);
				$("#notice_noticeId_modify").validatebox({
					required : true,
					missingMessage : "请输入公告id",
					editable: false
				});
				$("#notice_title_modify").val(notice.title);
				$("#notice_title_modify").validatebox({
					required : true,
					missingMessage : "请输入标题",
				});
				tinyMCE.editors['notice_content_modify'].setContent(notice.content);
				$("#notice_publishDate_modify").datetimebox({
					value: notice.publishDate,
					required: true,
					showSeconds: true,
				});
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#noticeModifyButton").click(function(){ 
		if ($("#noticeModifyForm").form("validate")) {
			$("#noticeModifyForm").form({
			    url:"Notice/update/" + $("#notice_noticeId_modify").val(),
			    onSubmit: function(){
					if($("#noticeEditForm").form("validate"))  {
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
                	var obj = jQuery.parseJSON(data);
                    if(obj.success){
                        $.messager.alert("消息","信息修改成功！");
                        $(".messager-window").css("z-index",10000);
                        //location.href="frontlist";
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    } 
			    }
			});
			//提交表单
			$("#noticeModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
