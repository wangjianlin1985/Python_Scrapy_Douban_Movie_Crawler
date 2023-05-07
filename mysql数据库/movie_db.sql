/*
Navicat MySQL Data Transfer

Source Server         : mysql5.6
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : movie_db

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2020-07-16 18:58:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_admin`
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `username` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES ('a', 'a');

-- ----------------------------
-- Table structure for `t_leaveword`
-- ----------------------------
DROP TABLE IF EXISTS `t_leaveword`;
CREATE TABLE `t_leaveword` (
  `leaveWordId` int(11) NOT NULL AUTO_INCREMENT COMMENT '留言id',
  `leaveTitle` varchar(80) NOT NULL COMMENT '留言标题',
  `leaveContent` varchar(2000) NOT NULL COMMENT '留言内容',
  `userObj` varchar(30) NOT NULL COMMENT '留言人',
  `leaveTime` varchar(20) DEFAULT NULL COMMENT '留言时间',
  `replyContent` varchar(1000) DEFAULT NULL COMMENT '管理回复',
  `replyTime` varchar(20) DEFAULT NULL COMMENT '回复时间',
  PRIMARY KEY (`leaveWordId`),
  KEY `userObj` (`userObj`),
  CONSTRAINT `t_leaveword_ibfk_1` FOREIGN KEY (`userObj`) REFERENCES `t_userinfo` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_leaveword
-- ----------------------------
INSERT INTO `t_leaveword` VALUES ('1', '电影不错哦！', '这里我能查询各种类型电影，不错哦', 'user1', '2020-07-16 12:55:12', '--', '--');
INSERT INTO `t_leaveword` VALUES ('2', '你好啊', '多多爬些电影吧！', 'user2', '2020-07-16 18:49:10', '知道了', '2020-07-16 18:56:41');
INSERT INTO `t_leaveword` VALUES ('3', '222', '3333', 'user2', '2020-07-16 18:49:14', '--', '--');

-- ----------------------------
-- Table structure for `t_movie`
-- ----------------------------
DROP TABLE IF EXISTS `t_movie`;
CREATE TABLE `t_movie` (
  `movieId` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录id',
  `url` varchar(100) NOT NULL COMMENT '豆瓣地址',
  `title` varchar(80) NOT NULL COMMENT '电影名称',
  `director` varchar(50) NOT NULL COMMENT '导演',
  `screenwriter` varchar(50) NOT NULL COMMENT '编剧',
  `actors` varchar(800) NOT NULL COMMENT '主演',
  `category` varchar(50) NOT NULL COMMENT '类型',
  `country` varchar(20) NOT NULL COMMENT '国家',
  `langrage` varchar(50) NOT NULL COMMENT '语言',
  `initial` varchar(30) NOT NULL COMMENT '上映日期',
  `runtime` varchar(20) NOT NULL COMMENT '片长',
  `playUrl` varchar(100) DEFAULT NULL COMMENT '播放地址',
  `rate` varchar(20) NOT NULL COMMENT '豆瓣评分',
  `starPeople` varchar(20) NOT NULL COMMENT '评价人数',
  `preShowUrl` varchar(100) DEFAULT NULL COMMENT '预告地址',
  `intro` varchar(5000) DEFAULT NULL COMMENT '剧情简介',
  `icon` varchar(100) NOT NULL COMMENT '海报图片',
  PRIMARY KEY (`movieId`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_movie
-- ----------------------------
INSERT INTO `t_movie` VALUES ('19', 'https://movie.douban.com/subject/26340302/', '请点赞 좋아해줘', '朴贤真', '刘英雅', '刘亚仁|崔智友|李絮|姜河那|金柱赫|李美妍', '喜剧|爱情', ' 韩国', ' 韩语', '2016-02-17(韩国)', '120分钟', '/', '6.5', '6314', 'https://movie.douban.com/trailer/189872/#content', '《请点赞》围绕三对男女讲述了发生在社交网络和现实生活中的爱情故事。韩文中的“点赞”同时有“喜欢”之意。而片中的三段爱情故事都是由“点赞”这样一个简单的动作发展而来的。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2306039647.jpg');
INSERT INTO `t_movie` VALUES ('20', 'https://movie.douban.com/subject/26416169/', '纯情 순정', '李恩熙', '李恩熙', '都暻秀|金所泫|李大卫|朱多英|延俊锡', '剧情|爱情', ' 韩国', ' 韩语', '2016-02-24(韩国)', '113分钟', '/', '7.4', '11335', 'https://movie.douban.com/trailer/216359/#content', '电影《纯情》讲述了一封在音乐节目直播过程中收到的来自23年前的信所引发的故事，描述了超越过去与现在的初恋和5名朋友之间的友情。片中，都暻秀饰演性格木讷但一片丹心的范实，金所炫饰演拥有天籁美声的少女秀玉。\n                                    |\n                                　　据了解，《纯情》将在今年夏天拍摄，预计於2016年2月上映，拍摄地点在全罗南道高兴郡。此前都暻秀通过电影《Cart》、电视剧《没关系，是爱情啊》、《记得你》展现精湛演技。而童星出身的金所炫更有着丰富的戏剧经验，主演了电视剧《想你》《Reset》《Who Are You-学校2015》等热播韩剧。2014年金所炫主演KBS一集特别企划剧《不一样的哭泣》，并凭借此剧在年末KBS演技大赏中获得女子部独幕剧奖。此次电影中与EXO D.O.合作主演，是金所炫首次担纲女主角，金所炫也表示感觉演戏很幸福，只要跟着哥哥就对了 。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2314222118.jpg');
INSERT INTO `t_movie` VALUES ('21', 'https://movie.douban.com/subject/26602368/', '我的极品女神', '阚家伟|王光利', '王晶|何洁|阙玥', '郑伊健|周秀娜|何浩文|文凯玲|林子聪|郑欣宜|何佩瑜|任娇|钟采羲|刘敬雯|符晓薇|佘卓颖', '喜剧|爱情|科幻', ' 中国大陆', ' 粤语', '2016-03-17(中国香港)', '88分钟', '/', '4.1', '2818', 'https://movie.douban.com/photos/photo/2540979459/', '晓峰（郑伊健饰）、尊尼（何浩文饰）、和朱云（林子聪饰）是多年好友，三人同时被女朋友分手，却离奇遇见了三位情投意合、为各自量身打造的机器人女友（周秀娜等饰），进而展开了一系列啼笑皆非的爱情故事……', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2364844665.jpg');
INSERT INTO `t_movie` VALUES ('22', 'https://movie.douban.com/subject/26354526/', '睡在我上铺的兄弟', '张琦', '张琦|陈倩|赵犇|苏阳', '陈晓|秦岚|杜天皓|刘芮麟|李现|余心恬|蓝盈莹|蒋雪鸣|王啸坤|姚蜜|梁超|王宝江|孔琳|任正斌|高晓松|俞敏洪|甘薇|金玉倩|张琦', '剧情|爱情', ' 中国大陆', ' 汉语普通话', '2016-04-01(中国大陆)', '96分钟', 'https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3F', '5.4', '39934', 'https://movie.douban.com/trailer/193858/#content', '故事开始于沪都大学303宿舍内，个性大大咧咧无畏惧他人眼光的林向宇（陈晓 饰），虽然身为海归富二代但心中只惦记着自己的宠物羊驼的李大鹏（杜天皓 饰），身强体壮但心思细腻温柔的谢训（李现 饰），拥有高超智商但缺少女人缘的学霸管超（刘芮麟 饰），这四位来自天南地北的大男孩们相聚在此，成为了朝夕相处的室友，拉开了有笑有泪的大学生活的序幕。\n                                    |\n                                　　短暂的四年一晃眼就要过去，站在人生的十字路口前，四人会做出怎样的选择？林向宇是否能够追求到他一直心系的“丝帕女生”？谢川和女友高宝镜（蓝盈莹 饰）之间的感情又会迎来怎样的结局呢？', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2325669261.jpg');
INSERT INTO `t_movie` VALUES ('23', 'https://movie.douban.com/subject/26345736/', '女汉子真爱公式', '郭大雷', '美岩|熊嘉南|郭大雷', '赵丽颖|张翰|童飞|丁一宇|涂世旻|阿兰|许峰|何文辉|王译唯|牟丛|金士杰|宋轶', '喜剧|爱情', ' 中国大陆', ' 汉语普通话', '2016-03-18(中国大陆)', '93分钟', 'https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fwvu3jvge0yp2mue.html%3Fptag%3D', '5.2', '19595', 'https://movie.douban.com/trailer/192964/#content', '悉尼大学数学统计专业女学霸何修舞（赵丽颖 饰）在硕士论文中推导出了“真爱公式”，坚信自己公式绝对无误的何修舞，却接到了自己第一个实验对象失败自杀的噩耗……\n                                    |\n                                　　为了早点送走可怕的学霸女，叶思逸（张翰 饰）决定亲自帮助她寻觅她的真命天子，只是这个过程中，到底是哪里变的不对了，竟然有了奇怪的化学反应……', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2324372895.jpg');
INSERT INTO `t_movie` VALUES ('24', 'https://movie.douban.com/subject/26345159/', '半熟少女', '阿牛|赵宇|陈立谦', '李舒程', '黄灿灿|敖犬|南笙|王子豪|王子杰|黄诗棋|江倩龄|可晴|弯弯', '剧情|爱情', ' 中国大陆', ' 汉语普通话', '2016-03-25(中国大陆)', '98分钟', 'https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmlb0mu3kbprd34z.html%3Fptag%3D', '3.3', '2828', 'https://movie.douban.com/trailer/192442/#content', '半熟，是对青春期最合理的定义，它是梦开始的地方，没有深思熟虑，只有最单纯的坚定，然而，在这个充满意外的年纪，未来似乎变得很具体，又有着无限的可能性。这个故事里有女汉子与呆萌校草的啼笑初恋，有四朵姐妹花的袍泽之谊，也有学霸乖乖女与双胞胎才子的意乱情迷，他们躁动的热情在循规蹈矩的理智中突围，写成一首欢笑与痛，梦想与爱的青春禁曲。\n                                    |\n                                　　也许，半熟与成熟之间，只差那次铤而走险的“叛逆”。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2326378603.jpg');
INSERT INTO `t_movie` VALUES ('25', 'https://movie.douban.com/subject/26576793/', '我才不会对黑崎君说的话言听计从 黒崎くんの言いなりになんてならない', '月川翔', '松田裕子', '中岛健人|小松菜奈|千叶雄大|高月彩良|岸优太|川津明日香|鈴木裕乃|北村優衣|長谷川里桃|中村靖日|黒崎レイナ|山崎あみ|鈴木美羽', '爱情', ' 日本', ' 日语', '2016-02-27(日本)', '93分钟', '/', '5.7', '12050', 'https://movie.douban.com/photos/photo/2452660595/', '赤羽由宇（小松菜奈 饰）是一个非常平凡的女子高中生，由于父亲工作的原因，由宇需要住进宿舍开始和其他同学和合住生活。平日里，由宇性格内敛，寡言少语，她希望这次的合宿生活能够帮助她改变一下内向的性格。\n                                    |\n                                　　然而，由宇住进宿舍没多久，便招惹到了学校里著名的“黑恶魔”黑崎晴人（中岛健人 饰），在阴差阳错之下，由宇竟然变成了任凭晴人使唤的傀儡，让由宇感到头疼的是，晴人似乎特别喜欢作弄她。如果说由宇是黑恶魔的话，那么白河（千叶雄大 饰）就是由宇心目中温柔的白马王子，但随着时间的推移，由宇发现自己和晴人之间的关系产生了微妙的变化。', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2295161284.jpg');
INSERT INTO `t_movie` VALUES ('26', 'https://movie.douban.com/subject/26719781/', '他和她的故事 Ki & Ka', 'R·巴尔基', 'R·巴尔基|里希·维尔马尼', '阿琼·卡普尔|卡琳娜·卡普尔|贾雅·巴杜里|拉吉特·卡普尔|斯瓦普·桑帕特|阿米达普·巴强', '喜剧|爱情', ' 印度', ' 印地语 / 泰米尔语 / 泰卢固语', '2016-04-01(印度)', '126分钟', 'https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Ftcusggy2pouuep7.html%3Fptag%3D', '7.8', '4573', 'https://movie.douban.com/photos/photo/2497595365/', '在一架飞机上，基雅（卡琳娜·卡普尔 Kareena Kapoor 饰）邂逅了名为卡比尔（阿琼·卡普尔 Arjun Kapoor 饰）的男子。让基雅感到意外的是，这个看上去铁骨铮铮的硬汉，竟然眼泪汪汪的害怕的簌簌发抖。原来，卡比尔害怕坐飞机，每次坐飞机的时候都是母亲安抚着他的情绪，然而故人已逝，卡比尔不禁触景生情。\n                                    |\n                                　　为了安慰卡比尔，基雅紧紧的握住了他的手，一段浪漫的恋情就此拉开序幕。没过多久，基雅和卡比尔就决定携手步入婚姻的殿堂，可是，他们在家庭里所扮演的角色却仿佛调了个个儿，基雅每日出门工作赚钱养家，而卡比尔则坐镇家中主持家务。他们的朋友和家人们会怎样看待这段逆转的关系呢？', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2315574510.jpg');
INSERT INTO `t_movie` VALUES ('27', 'https://movie.douban.com/subject/30306597/', '黄金宝藏 Golden Treasure', 'Uranchimeg Urtnasan', 'Uranchimeg Urtnasan', 'Erdenetsetseg Bazarragchaa|Mendbayar Dagvadorj|Tuvshinjargal Sukh-Ochir|Enkhtuya Tangad|Erdnetsetseg Bazarragchaa|Uranchimeg Urtnasan|Erdenebat Yarinpil|Uyanga Ayanga|Damdin Sovd|Zolzaya Gantur|Naran-Khuslen Bor', '剧情|动作|爱情', ' 蒙古', ' 蒙古语', '2016-03-05(蒙古)', '110分钟', 'https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3F', '8.3', '2342', 'https://movie.douban.com/photos/photo/2566584398/', '有「巨人」称号的策本是那达慕节的摔跤冠军，尽管已获得无数次的胜利，年迈的他却没有儿子能继承这份荣耀，就在得知妻子生下的第四胎也是女儿的当下，策本决定把么女太文视为男孩来抚养，面对被迫放弃女儿身的太文，内心依旧渴望换上美丽的衣服，当个漂亮的女孩。就在某次意外中，她的死对头杭艾发现这个惊人的真相，两人的关系也因此产生微妙的变化，究竟这个家族秘密能否永远守住？太文是否注定一生都得当个男孩子？', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2578570322.jpg');
INSERT INTO `t_movie` VALUES ('28', 'https://movie.douban.com/subject/30395519/', '新闻记者 新聞記者', '藤井道人', '詩森ろば|高石明彦|藤井道人|望月衣塑子|河村光庸', '沈恩京|松坂桃李|本田翼|冈山天音|郭智博|长田成哉|宫野阳名|高桥努|西田尚美|高桥和也|北村有起哉|田中哲司', '剧情|悬疑|惊悚', ' 日本', ' 日语', '2019-06-28(日本)', '113分钟', '/', '6.6', '2742', 'https://movie.douban.com/trailer/253028/#content', '该片以东京新闻记者望月衣塑子的小说为原案，描绘了逼近政治权力黑暗下的女性记者和追求理想公务员之道的精英官僚间的对峙故事。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2554514093.jpg');
INSERT INTO `t_movie` VALUES ('29', 'https://movie.douban.com/subject/26652816/', '高跟鞋先生', '陆可', '金依萌|杨哲|辛菲', '杜江|薛凯琪|余心恬|陈学冬|王祖蓝|霍思燕|李媛|肖骁|陆翊', '喜剧|爱情', ' 中国大陆', ' 汉语普通话', '2016-02-14(中国大陆)', '94分钟', 'https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3F', '5.0', '15004', 'https://movie.douban.com/trailer/191673/#content', '宅男游戏设计师杭远（杜江 饰），从小就暗恋同校才女李若欣（薛凯琪 饰），可每次要表白的时候她都已进入了新恋情。李若欣最后一段感情被未婚夫背叛，不再相信男人，转而与闺蜜Sammi（李媛 饰）越走越近。杭远顿时万念俱灰，于是富二代“好基友”林森森（陈学冬 饰）提议他做最后一搏，想方设法接近若欣，大胆追求所爱。阴差阳错下，杭远竟成为了网络红人，一时间风光无限。 但是好景不长，若欣很快识破了他们的“计谋”。他该如何挽回和女神的破裂的关系，并成功和她在一起呢？', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2312412325.jpg');
INSERT INTO `t_movie` VALUES ('30', 'https://movie.douban.com/subject/30176393/', '误杀', '柯汶利', '杨薇薇|翟培|李鹏|范凯华|秦语谦|雷声', '肖央|谭卓|陈冲|姜皓文|秦沛|边天扬|许文姗|张熙然|施名帅|黄健玮|陈志朋', '剧情|悬疑|犯罪', ' 中国大陆', ' 汉语普通话', '2019-12-13(中国大陆)', '112分钟', 'https://www.douban.com/link2/?url=https%3A%2F%2Fwww.huanxi.com%2Fplay_44658.shtml%3Fsource%3D9%26fro', '7.7', '569700', 'https://movie.douban.com/trailer/256730/#content', '李维杰（肖央 饰）与妻子阿玉（谭卓 饰）来泰打拼17年，膝下育有两个女儿，年届四十的他靠开设网络公司为生，为人也颇得小镇居民的好感，而这一切美好却被突如其来的不速之客打破。这个充斥走私，贩毒活动的边陲小镇，各种权力交织碾压公平正义。李维杰的大女儿平平（许文珊 饰）被督察长拉韫（陈冲 饰）的儿子素察（边天扬 饰）迷奸，因反抗误杀对方。李维杰曾亲眼目睹督察长滥用私刑，深知法律无用，为了维护女儿，捍卫家人，李维杰埋尸掩盖一切证据，在时间与空间的交错缝隙中，与警方在身心层面，展开了殊死一搏的较量。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2576090251.jpg');
INSERT INTO `t_movie` VALUES ('31', 'https://movie.douban.com/subject/30414283/', '少年与海', '孙傲谦', '孙傲谦|安吉尔', '于坤杰|李蔓瑄|孙心福|兰海隆', '剧情|儿童|奇幻', ' 中国大陆', ' 东北方言', '2019-10-04(釜山电影节)', '106分钟', '/', '7.1', '694', 'https://movie.douban.com/photos/photo/2567901793/', '11岁的男孩小杰（于坤杰 饰）自幼便和经营公路旅店的大舅（孙心福 饰）一家共同生活。小杰为了完成学校作业——制作一副“大海”主题剪贴画，渴望得到一本《海洋百科》图书。表姐（李蔓瑄 饰）原本答应为弟弟买书，然而大舅突遭车祸，真凶拒不赔偿，全家陷入麻烦之中。 小杰不忍为家人再添烦忧，决心通过自己努力得到图书。他穿行在城镇和乡村之间，游荡在现实与幻想边缘，少年与海的秘密翻涌浮现……', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2570189281.jpg');
INSERT INTO `t_movie` VALUES ('32', 'https://movie.douban.com/subject/30331959/', '黑水 Dark Waters', '托德·海因斯', '纳撒尼尔·里奇|马里奥·科雷亚|马修·迈克尔·卡纳汉', '马克·鲁弗洛|安妮·海瑟薇|蒂姆·罗宾斯|比尔·坎普|维克多·加博|比尔·普尔曼|梅尔·温宁汉姆|威廉·杰克森·哈珀|路易莎·克劳瑟|凯文·克劳利|丹尼尔·R·希尔|王明|西尼·迈尔斯|马克·霍克尔|考特尼·德科斯基|斯嘉丽·希克斯|布莱恩·加拉格尔|约翰·纽伯格|莱曼·陈|丹妮丝·达·维拉|杰弗里·格罗弗|泰里·克拉克|杰夫·福尔克|温·赖克特|乔恩·奥斯贝克|理查德·杜恩|迈克尔·海尼|大卫·皮廷格', '剧情', ' 美国', ' 英语 / 韩语', '2019-11-22(美国点映)', '126分钟', '/', '8.5', '75854', 'https://movie.douban.com/trailer/253374/#content', '基于Nathaniel Rich在《纽约时报》上发表的文章《The Lawyer Who Became DuPont’s Worst Nightmare》，围绕罗伯特·比洛特展开，他担任辩护律师长达8年之久，他对化工巨头杜邦公司提起了环境诉讼，这场官司揭露了几十年来杜邦公司化学污染的历史。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2569450232.jpg');
INSERT INTO `t_movie` VALUES ('33', 'https://movie.douban.com/subject/33418492/', '家庭罗曼史有限公司 Family Romance, LLC.', '沃纳·赫尔佐格', '沃纳·赫尔佐格', 'Mahiro Tanimoto|Ishii Yuichi', '剧情', ' 美国', ' 日语', '2019-05-18(戛纳电影节)', '89分钟', '/', '7.1', '1196', 'https://movie.douban.com/trailer/247086/#content', '开设在日本的家庭罗曼史有限公司是一家通过角色扮演为客户定制“体验”的公司。在这里，你可以租借到陪伴自己的“父亲”，愿意顶罪的“同事”......公司员工石井裕一在一次次的倾情扮演中，也陷入了对自己职业的沉思。陪伴在身边的人可能是假的，生命中的美好回忆又有几分是真的呢？德国名导赫尔佐格视角独特，打破纪录与非纪录的界线，在演练好的剧本和真实故事的交错之中，观众也不免从电影延伸出对自己现实生活的思考。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2556917880.jpg');
INSERT INTO `t_movie` VALUES ('34', 'https://movie.douban.com/subject/30318240/', '季节与季节之间 계절과 계절 사이', '金準植', '金準植', '李英珍|尹惠利|吴荷妮|金永敏|郑恩京', '剧情|同性', ' 韩国', ' 韩语', '2019-10-03(韩国)', '98分钟', '/', '7.1', '2265', 'https://movie.douban.com/photos/photo/2533363136/', '从地方搬到城市的一个女人海秀，开一间咖啡厅开始新的生活。常来咖啡厅的女高中生艺珍，继而在咖啡厅打工，渐渐被海秀吸引。艺珍确信自己的感情是真的，向海秀告白。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2570192512.jpg');
INSERT INTO `t_movie` VALUES ('35', 'https://movie.douban.com/subject/34607890/', '宝莱坞双雄之战 War', '希达·阿南德', '希达·阿南德|阿迪提亚·乔普拉|什里达·拉加万|阿巴斯·特里瓦拉', '赫里尼克·罗斯汉|泰戈尔·什罗夫|瓦妮·卡普尔|阿舒托史.拉纳|阿努普瑞雅·戈恩卡|亚什·拉杰·辛格|马什霍尔·阿姆罗希|桑吉耶夫·瓦萨|迪帕尼塔·夏尔玛|索妮·拉兹丹|阿里夫·扎卡里亚|阿米特·高尔|伊姆兰·艾哈迈德|沙巴兹·阿克萨|纳吉姆丁·哈达德|蒂希塔·塞加尔|陈大卫|托雷尔·文森', '动作|惊悚', ' 印度', ' 印地语 / 泰米尔语 / 泰卢固语 / 西班牙语 / 法语 / 俄语 / 英语 / 日语 / 希伯', '2019-10-02(印度)', '154分钟', '/', '6.3', '1883', 'https://movie.douban.com/video/104189/', '哈立德的任务是消灭卡比尔，一个前士兵变成了流氓，因为他与他的导师进行了史诗般的战斗。', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2569921195.jpg');
INSERT INTO `t_movie` VALUES ('36', 'https://movie.douban.com/subject/30167633/', '谎言大师 The Good Liar', '比尔·康顿', '杰弗里·哈彻|尼古拉斯·希尔勒', '海伦·米伦|伊恩·麦克莱恩|拉塞尔·托维|马克·路易斯·琼斯|吉姆·卡特|约翰内斯·豪克尔·约翰内森|席琳·邦金斯|贝西·卡特|亚历山大·约瓦诺维奇|菲尔·邓斯特|迈克尔·卡尔金|劳里·戴维森|露丝·霍洛克斯|杰奎琳·拉姆娜莱恩|内尔·威廉姆斯|贾格·帕特尔|莉莉·多斯沃斯-埃文斯|斯特拉·斯托克尔|朱利安·费罗|马诺伊·阿南德|弗兰·塔格|斯派克·怀特|凯文·马塔迪恩', '剧情', ' 美国', ' 英语', '2019-11-15(美国)', '109分钟', '/', '6.9', '6263', 'https://movie.douban.com/trailer/253583/#content', '海伦·米伦与伊恩·麦克莱恩即将出演新线的剧情片《The Good Liar》（优秀的骗子，暂译）。影片将由比尔·康顿执导，他最近的作品，就是在全世界狂揽12亿美元的《美女与野兽》。\n                                    |\n                                　　在影片中，伊恩爵士饰演一名职业骗子，当他遇到海伦·米伦饰演的富裕寡妇时，简直不敢相信自己的运气。这位寡妇把自己的生活和家门都向骗子打开，骗子却发现自己是真的关心她，让这笔本该骗了就撤的买卖，变成了像走钢丝一样的危险关系。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2560819247.jpg');
INSERT INTO `t_movie` VALUES ('37', 'https://movie.douban.com/subject/30461808/', '抗拒：柳宽顺的故事 항거: 유관순 이야기', '赵民镐', '赵民镐', '高雅星|金玺碧|金艺恩|丁夏潭|柳京洙|金南珍|李英锡|崔武成| 金妍贞|朴贊佑', '剧情', ' 韩国', ' 韩语', '2019-02-27(韩国)', '105分钟', '/', '7.3', '434', 'https://movie.douban.com/trailer/244253/#content', '「革命無分性別、年齡與時代！電影取材自真實韓國獨立運動，以年輕革命女義士柳寬順為原型，見證一段鮮為人知的歷史。日佔時期，韓國爆發三一運動，十七歲少女上街帶領逾二百萬韓國民眾抗爭，卻被捕囚禁在女子地下監獄，受盡百般凌辱。她非但沒有噤若寒蟬，反而挺身感召其他囚犯打破沉默，從自我覺醒走向集體覺醒，在獄中共同高呼「大韓獨立萬歲」的口號。黑白鏡頭下的獄中景象格外銳利，眾人以堅毅的眼神明志：監獄的高牆囚得住肉體，卻困不住自由的靈魂。高我星從《韓流怪嚇》嶄露頭角，到《末世列車》已成氣候，是次飾演烈女同樣鏗鏘有力。在最壞的時代，讓我們為這位巾幗英雄及所有因抗爭犧牲的義士獻一闋輓歌。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2548355821.jpg');
INSERT INTO `t_movie` VALUES ('38', 'https://movie.douban.com/subject/33409114/', '撒旦的恐慌 Satanic Panic', 'Chelsea Stardust Peters', '泰德·盖根|Grady Hendrix', '丽贝卡·罗梅恩|杰瑞·奥康奈尔|乔丹·莱德', '喜剧|恐怖', ' 美国', ' 英语', '2019-09-06(美国)', '85分钟', '/', '5.1', '480', 'https://movie.douban.com/photos/photo/2572485297/', 'A pizza delivery girl at the end of her financial rope has to fight for her life - and her tips - when her last order of the night turns out to be high society Satanists in need of a virgin sacrifice.', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2564553821.jpg');
INSERT INTO `t_movie` VALUES ('39', 'https://movie.douban.com/subject/34441267/', '海面上漂过的奖杯', '雎安奇', '雎安奇', '王学兵|曹卫宇|王小欢|李沫颔', '剧情', ' 中国大陆', ' 汉语普通话', '2019-10-15(平遥国际电影展)', '90分钟', '/', '6.2', '335', 'https://movie.douban.com/photos/photo/2560431879/', '《海面上漂过的奖杯》讲述了一个失败的演员逃亡的故事——主角安鹏远是一个钓鱼爱好者，终于得到了一个钓鱼比赛的奖杯，却发现妻子和一个失败的导演出轨，一怒之下导演倒在了血泊之中，被警方追捕的安鹏远带着一个钓鱼包在逃亡的路上闯入了一个陌生女人的家中……', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2560431568.jpg');
INSERT INTO `t_movie` VALUES ('40', 'https://movie.douban.com/subject/30394535/', '被光抓走的人', '董润年', '董润年', '黄渤|王珞丹|谭卓|白客|黄璐|文淇|焦俊艳|宋春丽|李嘉琪|丁溪鹤|吕星辰|黄觉|李倩|王菊|李诞|金靖承|曹炳琨|张腾岳|田壮壮|刘頔', '剧情|爱情|科幻', ' 中国大陆', ' 汉语普通话', '2019-12-13(中国大陆)', '131分钟', 'https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3F', '7.0', '147172', 'https://movie.douban.com/trailer/256437/#content', '据说该片的创作灵感来源于董润年的一个脑洞：“如果有一道神秘的光把一部分人抓走，社会的平静与法则被打破，我们该怎么办？” 在导演的脑洞中，光代表什么？为什么人会被光抓走？谁会被光抓走？留下来的人要怎么办？这一系列疑问未来都需要在片中得到解答。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2575887979.jpg');
INSERT INTO `t_movie` VALUES ('41', 'https://movie.douban.com/subject/30163500/', '鬼影特攻：以暴制暴 6 Underground', '迈克尔·贝', '保罗·韦尼克|瑞特·里斯', '瑞恩·雷诺兹|本·哈迪|梅拉尼·罗兰|阿德里娅·阿霍纳|戴夫·弗兰科|科里·霍金斯|塞巴斯蒂安·罗奇|曼努埃尔·加西亚-鲁尔福|詹姆斯·莫瑞|利奥·拉兹|埃莱娜·卡多纳|佩曼·莫阿迪|尤里·科洛科利尼科夫|金·柯尔德|丹尼尔·阿德博伊加|詹姆斯·卡罗尔·乔丹|康斯坦丁·格雷戈里|彼得·阿佩塞拉|托多尔·乔丹诺夫|里纳特·希什马塔林|莉迪亚·佛朗哥|罗杰·内瓦雷斯|舒巴姆·沙拉夫', '动作|惊悚', ' 美国', ' 英语 / 土库曼语 / 粤语 / 意大利语 / 西班牙语 / 乌克兰语 / 法语', '2019-12-13(美国)', '127分钟', '/', '6.4', '25510', 'https://movie.douban.com/trailer/256634/#content', '来自世界各地的六人，个个都是各自领域的佼佼者。他们之所以被选中，不单是因为能力出众，还在于其独特的志向：他们想抹杀自己的过去以改变未来。一位神秘的领袖（瑞恩·雷诺兹饰）将他们召集到一起组成了这个团队，他毕生唯一的使命就是确保即使他和自己的同伴会被遗忘，但也要让人们永远铭记他们所做的一切。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2574329643.jpg');
INSERT INTO `t_movie` VALUES ('42', 'https://movie.douban.com/subject/30155105/', '燃烧 Burn', '迈克·甘', '迈克·甘', '蒂尔达·格哈姆-哈维|乔什·哈切森|苏琪·沃特豪斯|岑勇康|希罗·弗南德兹|基思·伦纳德|小安琪·威莱|约翰·D·希克曼|韦恩·派尔|温特·李·霍兰德|Rob Figueroa|道格·莫泰|吉姆·戴佛提|乔·詹姆斯|玛丽娜·莫耶', '惊悚', ' 美国', ' 英语', '2019-08-23(美国/中国台湾)', '88分钟', '/', '5.7', '572', 'https://movie.douban.com/trailer/250969/#content', '岑勇康、希罗·费尔南德斯加盟惊悚新片《羽毛》(Plume)，乔什·哈切森、苏琪·沃特豪斯、蒂尔达·格哈姆-哈维主演，华裔Mike Gan自编自导。故事围绕一个孤独、情绪不稳定的加油站服务员Melinda(哈维)展开，她受够了被更自信、外向的同事Sheila(沃特豪斯)所掩盖，当一个急需现金、绝望的男人Billy(哈切森)持枪劫持加油站时，Melinda找到了一个机会和他建立联系，不管是否有人受伤。\n                                    |\n                                　　岑勇康饰演刘警官，道德良好、正直，受到Melinda的迷恋。费尔南德斯饰演Sheila男友Perry，被无意中卷进了她的危险游戏中。\n                                    |\n                                　　这是Mike Gan执导的首部长片，此前他执导的短片《No Evil》曾亮相多伦多电影节和棕榈泉电影节。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2567071749.jpg');
INSERT INTO `t_movie` VALUES ('43', 'https://movie.douban.com/subject/26752997/', '戈梅拉岛 La Gomera', '柯内流·波蓝波宇', '柯内流·波蓝波宇', '弗拉德·伊凡诺夫|卡特里内尔·马龙|罗迪卡·拉泽尔|阿古斯丁·比利亚龙加|萨宾·塔布瑞亚|István Teglas|Cristóbal Pinto|Antonio Buíl|George Pistereanu|David Agranov|Andrei Barbu|Andrei Ciopec|Sergiu Costache|Julieta Szönyi', '喜剧|犯罪', ' 罗马尼亚 / 法国 / 德国 / 瑞典', ' 罗马尼亚语 / 英语 / 西班牙语', '2019-05-18(戛纳电影节)', '97分钟', '/', '6.4', '1838', 'https://movie.douban.com/trailer/256459/#content', '警察克斯蒂带着任务前往戈梅拉岛，打入黑帮学习口哨暗语。然而当他回到警局之后，昔日的同伴却站在了他的对立面。到底是谁被策反？又是谁在泄密？在表象的忠诚与信任下，一切都不是那么简单。尔虞我诈中，竟然还蔓生开来一场浪漫又富有幽默感的爱之博弈，且看有情人能否终成眷属？罗马尼亚导演波蓝波宇玩转剪辑，五彩缤纷地为观众呈现一出错综复杂的东欧谍战爱情好戏。', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2594821652.jpg');
INSERT INTO `t_movie` VALUES ('44', 'https://movie.douban.com/subject/30345198/', '要做两次吗？ 두번 할까요', '朴庸集', '朴庸集', '权相宇|李贞贤|李钟赫|成东日|郑尚勋|金贤淑|朴庆惠|高成焕|洪根泽|刘贞莱|郑多媛', '喜剧|爱情', ' 韩国', ' 韩语', '2019-10-17(韩国)', '112分钟', '/', '5.6', '801', 'https://movie.douban.com/photos/photo/2600803792/', '该片讲述了无法继续在一起的夫妇为了幸福而发生的喜剧故事，权相宇饰演内衣公司营业部科长赵贤宇，李贞贤饰演翻译朴善英，李钟赫饰演动物医院的医生安相哲，将真实的反应韩国成人男女的现实生活。', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2568881167.jpg');

-- ----------------------------
-- Table structure for `t_notice`
-- ----------------------------
DROP TABLE IF EXISTS `t_notice`;
CREATE TABLE `t_notice` (
  `noticeId` int(11) NOT NULL AUTO_INCREMENT COMMENT '公告id',
  `title` varchar(80) NOT NULL COMMENT '标题',
  `content` varchar(5000) NOT NULL COMMENT '公告内容',
  `publishDate` varchar(20) DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`noticeId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_notice
-- ----------------------------
INSERT INTO `t_notice` VALUES ('1', '电影网站成立了', '<p>同志们，这里可以搜索到各种电影哦！</p>', '2020-07-16 17:58:57');
INSERT INTO `t_notice` VALUES ('2', '11111', '<p>22222</p>', '2020-07-16 17:59:08');

-- ----------------------------
-- Table structure for `t_userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_userinfo`;
CREATE TABLE `t_userinfo` (
  `user_name` varchar(30) NOT NULL COMMENT 'user_name',
  `password` varchar(30) NOT NULL COMMENT '登录密码',
  `name` varchar(20) NOT NULL COMMENT '姓名',
  `gender` varchar(4) NOT NULL COMMENT '性别',
  `birthDate` varchar(20) DEFAULT NULL COMMENT '出生日期',
  `userPhoto` varchar(60) NOT NULL COMMENT '用户照片',
  `telephone` varchar(20) NOT NULL COMMENT '联系电话',
  `email` varchar(50) NOT NULL COMMENT '邮箱',
  `address` varchar(80) DEFAULT NULL COMMENT '家庭地址',
  `regTime` varchar(20) DEFAULT NULL COMMENT '注册时间',
  PRIMARY KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_userinfo
-- ----------------------------
INSERT INTO `t_userinfo` VALUES ('user1', '123', '李先涛', '男', '2020-07-02', 'img/9.jpg', '13980083423', 'xiantao@126.com', '四川成都红星路', '2020-07-16 12:43:06');
INSERT INTO `t_userinfo` VALUES ('user2', '123456', '张晓彤', '女', '2020-07-01', 'img/20.jpg', '13688886666', 'xiaotong@163.com', '四川南充滨江路', '2020-07-16 18:41:19');
