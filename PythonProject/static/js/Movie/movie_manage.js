var movie_manage_tool = null; 
$(function () { 
	initMovieManageTool(); //建立Movie管理对象
	movie_manage_tool.init(); //如果需要通过下拉框查询，首先初始化下拉框的值
	$("#movie_manage").datagrid({
		url : '/Movie/list',
		queryParams: {
			"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
		},
		fit : true,
		fitColumns : true,
		striped : true,
		rownumbers : true,
		border : false,
		pagination : true,
		pageSize : 5,
		pageList : [5, 10, 15, 20, 25],
		pageNumber : 1,
		sortName : "movieId",
		sortOrder : "desc",
		toolbar : "#movie_manage_tool",
		columns : [[
			{
				field : "title",
				title : "电影名称",
				width : 140,
			},
			{
				field : "director",
				title : "导演",
				width : 140,
			},
			{
				field : "screenwriter",
				title : "编剧",
				width : 140,
			},
			{
				field : "actors",
				title : "主演",
				width : 140,
			},
			{
				field : "category",
				title : "类型",
				width : 140,
			},
			{
				field : "country",
				title : "国家",
				width : 140,
			},
			{
				field : "langrage",
				title : "语言",
				width : 140,
			},
			{
				field : "initial",
				title : "上映日期",
				width : 140,
			},
			{
				field : "rate",
				title : "豆瓣评分",
				width : 140,
			},
			{
				field : "icon",
				title : "海报图片",
				width : 140,
			},
		]],
	});

	$("#movieEditDiv").dialog({
		title : "修改管理",
		top: "10px",
		width : 1000,
		height : 600,
		modal : true,
		closed : true,
		iconCls : "icon-edit-new",
		buttons : [{
			text : "提交",
			iconCls : "icon-edit-new",
			handler : function () {
				if ($("#movieEditForm").form("validate")) {
					//验证表单 
					if(!$("#movieEditForm").form("validate")) {
						$.messager.alert("错误提示","你输入的信息还有错误！","warning");
					} else {
						$("#movieEditForm").form({
						    url:"/Movie/update/" + $("#movie_movieId_edit").val(),
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
						    	console.log(data);
			                	var obj = jQuery.parseJSON(data);
			                    if(obj.success){
			                        $.messager.alert("消息","信息修改成功！");
			                        $("#movieEditDiv").dialog("close");
			                        movie_manage_tool.reload();
			                    }else{
			                        $.messager.alert("消息",obj.message);
			                    } 
						    }
						});
						//提交表单
						$("#movieEditForm").submit();
					}
				}
			},
		},{
			text : "取消",
			iconCls : "icon-redo",
			handler : function () {
				$("#movieEditDiv").dialog("close");
				$("#movieEditForm").form("reset"); 
			},
		}],
	});
});

function initMovieManageTool() {
	movie_manage_tool = {
		init: function() {
			//实例化编辑器
			tinyMCE.init({
				selector: "#movie_intro_edit",
				theme: 'advanced',
				language: "zh",
				strict_loading_mode: 1,
			});
		},
		reload : function () {
			$("#movie_manage").datagrid("reload");
		},
		redo : function () {
			$("#movie_manage").datagrid("unselectAll");
		},
		search: function() {
			var queryParams = $("#movie_manage").datagrid("options").queryParams;
			queryParams["title"] = $("#title").val();
			queryParams["director"] = $("#director").val();
			queryParams["screenwriter"] = $("#screenwriter").val();
			queryParams["actors"] = $("#actors").val();
			queryParams["category"] = $("#category").val();
			queryParams["country"] = $("#country").val();
			queryParams["langrage"] = $("#langrage").val();
			queryParams["initial"] = $("#initial").val();
			queryParams["csrfmiddlewaretoken"] = $('input[name="csrfmiddlewaretoken"]').val();
			$("#movie_manage").datagrid("options").queryParams=queryParams; 
			$("#movie_manage").datagrid("load");
		},
		exportExcel: function() {
			$("#movieQueryForm").form({
			    url:"/Movie/OutToExcel?csrfmiddlewaretoken" + $('input[name="csrfmiddlewaretoken"]').val(),
			});
			//提交表单
			$("#movieQueryForm").submit();
		},
		remove : function () {
			var rows = $("#movie_manage").datagrid("getSelections");
			if (rows.length > 0) {
				$.messager.confirm("确定操作", "您正在要删除所选的记录吗？", function (flag) {
					if (flag) {
						var movieIds = [];
						for (var i = 0; i < rows.length; i ++) {
							movieIds.push(rows[i].movieId);
						}
						$.ajax({
							type : "POST",
							url : "/Movie/deletes",
							data : {
								movieIds : movieIds.join(","),
								"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
							},
							beforeSend : function () {
								$("#movie_manage").datagrid("loading");
							},
							success : function (data) {
								if (data.success) {
									$("#movie_manage").datagrid("loaded");
									$("#movie_manage").datagrid("load");
									$("#movie_manage").datagrid("unselectAll");
									$.messager.show({
										title : "提示",
										msg : data.message
									});
								} else {
									$("#movie_manage").datagrid("loaded");
									$("#movie_manage").datagrid("load");
									$("#movie_manage").datagrid("unselectAll");
									$.messager.alert("消息",data.message);
								}
							},
						});
					}
				});
			} else {
				$.messager.alert("提示", "请选择要删除的记录！", "info");
			}
		},
		edit : function () {
			var rows = $("#movie_manage").datagrid("getSelections");
			if (rows.length > 1) {
				$.messager.alert("警告操作！", "编辑记录只能选定一条数据！", "warning");
			} else if (rows.length == 1) {
				$.ajax({
					url : "/Movie/update/" + rows[0].movieId,
					type : "get",
					data : {
						//movieId : rows[0].movieId,
					},
					beforeSend : function () {
						$.messager.progress({
							text : "正在获取中...",
						});
					},
					success : function (movie, response, status) {
						$.messager.progress("close");
						if (movie) { 
							$("#movieEditDiv").dialog("open");
							$("#movie_movieId_edit").val(movie.movieId);
							$("#movie_movieId_edit").validatebox({
								required : true,
								missingMessage : "请输入记录id",
								editable: false
							});
							$("#movie_url_edit").val(movie.url);
							$("#movie_url_edit").validatebox({
								required : true,
								missingMessage : "请输入豆瓣地址",
							});
							$("#movie_title_edit").val(movie.title);
							$("#movie_title_edit").validatebox({
								required : true,
								missingMessage : "请输入电影名称",
							});
							$("#movie_director_edit").val(movie.director);
							$("#movie_director_edit").validatebox({
								required : true,
								missingMessage : "请输入导演",
							});
							$("#movie_screenwriter_edit").val(movie.screenwriter);
							$("#movie_screenwriter_edit").validatebox({
								required : true,
								missingMessage : "请输入编剧",
							});
							$("#movie_actors_edit").val(movie.actors);
							$("#movie_actors_edit").validatebox({
								required : true,
								missingMessage : "请输入主演",
							});
							$("#movie_category_edit").val(movie.category);
							$("#movie_category_edit").validatebox({
								required : true,
								missingMessage : "请输入类型",
							});
							$("#movie_country_edit").val(movie.country);
							$("#movie_country_edit").validatebox({
								required : true,
								missingMessage : "请输入国家",
							});
							$("#movie_langrage_edit").val(movie.langrage);
							$("#movie_langrage_edit").validatebox({
								required : true,
								missingMessage : "请输入语言",
							});
							$("#movie_initial_edit").val(movie.initial);
							$("#movie_initial_edit").validatebox({
								required : true,
								missingMessage : "请输入上映日期",
							});
							$("#movie_runtime_edit").val(movie.runtime);
							$("#movie_runtime_edit").validatebox({
								required : true,
								missingMessage : "请输入片长",
							});
							$("#movie_playUrl_edit").val(movie.playUrl);
							$("#movie_rate_edit").val(movie.rate);
							$("#movie_rate_edit").validatebox({
								required : true,
								missingMessage : "请输入豆瓣评分",
							});
							$("#movie_starPeople_edit").val(movie.starPeople);
							$("#movie_starPeople_edit").validatebox({
								required : true,
								missingMessage : "请输入评价人数",
							});
							$("#movie_preShowUrl_edit").val(movie.preShowUrl);
							tinyMCE.editors['movie_intro_edit'].setContent(movie.intro);
							$("#movie_icon_edit").val(movie.icon);
							$("#movie_icon_edit").validatebox({
								required : true,
								missingMessage : "请输入海报图片",
							});
						} else {
							$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
						}
					}
				});
			} else if (rows.length == 0) {
				$.messager.alert("警告操作！", "编辑记录至少选定一条数据！", "warning");
			}
		},
	};
}
