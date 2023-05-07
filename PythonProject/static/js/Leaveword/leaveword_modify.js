$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Leaveword/update/" + $("#leaveword_leaveWordId_modify").val(),
		type : "get",
		data : {
			//leaveWordId : $("#leaveword_leaveWordId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (leaveword, response, status) {
			$.messager.progress("close");
			if (leaveword) { 
				$("#leaveword_leaveWordId_modify").val(leaveword.leaveWordId);
				$("#leaveword_leaveWordId_modify").validatebox({
					required : true,
					missingMessage : "请输入留言id",
					editable: false
				});
				$("#leaveword_leaveTitle_modify").val(leaveword.leaveTitle);
				$("#leaveword_leaveTitle_modify").validatebox({
					required : true,
					missingMessage : "请输入留言标题",
				});
				$("#leaveword_leaveContent_modify").val(leaveword.leaveContent);
				$("#leaveword_leaveContent_modify").validatebox({
					required : true,
					missingMessage : "请输入留言内容",
				});
				$("#leaveword_userObj_user_name_modify").combobox({
					url:"/UserInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"user_name",
					textField:"name",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#leaveword_userObj_user_name_modify").combobox("select", leaveword.userObjPri);
						//var data = $("#leaveword_userObj_user_name_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#leaveword_userObj_user_name_edit").combobox("select", data[0].user_name);
						//}
					}
				});
				$("#leaveword_leaveTime_modify").datetimebox({
					value: leaveword.leaveTime,
					required: true,
					showSeconds: true,
				});
				$("#leaveword_replyContent_modify").val(leaveword.replyContent);
				$("#leaveword_replyTime_modify").datetimebox({
					value: leaveword.replyTime,
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

	$("#leavewordModifyButton").click(function(){ 
		if ($("#leavewordModifyForm").form("validate")) {
			$("#leavewordModifyForm").form({
			    url:"Leaveword/update/" + $("#leaveword_leaveWordId_modify").val(),
			    onSubmit: function(){
					if($("#leavewordEditForm").form("validate"))  {
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
			$("#leavewordModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
