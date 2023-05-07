$(function () {
    //实例化剧情简介编辑器
    tinyMCE.init({
        selector: "#movie_intro_modify",
        theme: 'advanced',
        language: "zh",
        strict_loading_mode: 1,
    });
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Movie/update/" + $("#movie_movieId_modify").val(),
		type : "get",
		data : {
			//movieId : $("#movie_movieId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (movie, response, status) {
			$.messager.progress("close");
			if (movie) { 
				$("#movie_movieId_modify").val(movie.movieId);
				$("#movie_movieId_modify").validatebox({
					required : true,
					missingMessage : "请输入记录id",
					editable: false
				});
				$("#movie_url_modify").val(movie.url);
				$("#movie_url_modify").validatebox({
					required : true,
					missingMessage : "请输入豆瓣地址",
				});
				$("#movie_title_modify").val(movie.title);
				$("#movie_title_modify").validatebox({
					required : true,
					missingMessage : "请输入电影名称",
				});
				$("#movie_director_modify").val(movie.director);
				$("#movie_director_modify").validatebox({
					required : true,
					missingMessage : "请输入导演",
				});
				$("#movie_screenwriter_modify").val(movie.screenwriter);
				$("#movie_screenwriter_modify").validatebox({
					required : true,
					missingMessage : "请输入编剧",
				});
				$("#movie_actors_modify").val(movie.actors);
				$("#movie_actors_modify").validatebox({
					required : true,
					missingMessage : "请输入主演",
				});
				$("#movie_category_modify").val(movie.category);
				$("#movie_category_modify").validatebox({
					required : true,
					missingMessage : "请输入类型",
				});
				$("#movie_country_modify").val(movie.country);
				$("#movie_country_modify").validatebox({
					required : true,
					missingMessage : "请输入国家",
				});
				$("#movie_langrage_modify").val(movie.langrage);
				$("#movie_langrage_modify").validatebox({
					required : true,
					missingMessage : "请输入语言",
				});
				$("#movie_initial_modify").val(movie.initial);
				$("#movie_initial_modify").validatebox({
					required : true,
					missingMessage : "请输入上映日期",
				});
				$("#movie_runtime_modify").val(movie.runtime);
				$("#movie_runtime_modify").validatebox({
					required : true,
					missingMessage : "请输入片长",
				});
				$("#movie_playUrl_modify").val(movie.playUrl);
				$("#movie_rate_modify").val(movie.rate);
				$("#movie_rate_modify").validatebox({
					required : true,
					missingMessage : "请输入豆瓣评分",
				});
				$("#movie_starPeople_modify").val(movie.starPeople);
				$("#movie_starPeople_modify").validatebox({
					required : true,
					missingMessage : "请输入评价人数",
				});
				$("#movie_preShowUrl_modify").val(movie.preShowUrl);
				tinyMCE.editors['movie_intro_modify'].setContent(movie.intro);
				$("#movie_icon_modify").val(movie.icon);
				$("#movie_icon_modify").validatebox({
					required : true,
					missingMessage : "请输入海报图片",
				});
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#movieModifyButton").click(function(){ 
		if ($("#movieModifyForm").form("validate")) {
			$("#movieModifyForm").form({
			    url:"Movie/update/" + $("#movie_movieId_modify").val(),
			    onSubmit: function(){
					if($("#movieEditForm").form("validate"))  {
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
			$("#movieModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
