scrapy 获取彩票信息
1 安装方法 （ scrapy安装）
2 mysql表数据

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for caipiao
-- ----------------------------
DROP TABLE IF EXISTS `caipiao`;
CREATE TABLE `caipiao` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `openward_time` date NOT NULL COMMENT '开奖时间',
  `issue_number` int(11) NOT NULL COMMENT '期号',
  `number1` int(11) DEFAULT NULL COMMENT '蓝球1',
  `number2` int(11) NOT NULL COMMENT '蓝球2',
  `number3` int(11) DEFAULT NULL COMMENT '蓝球3',
  `number4` int(11) DEFAULT NULL COMMENT '蓝球4',
  `number5` int(11) DEFAULT NULL COMMENT '蓝球5',
  `number6` int(11) DEFAULT NULL COMMENT '蓝球6',
  `number7` int(11) DEFAULT NULL COMMENT 'red',
  `numbers` varchar(256) DEFAULT NULL COMMENT 'json',
  `createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`,`openward_time`,`issue_number`)
) ENGINE=MyISAM AUTO_INCREMENT=2433 DEFAULT CHARSET=utf8;
3 运行 caipiao.py
4 TODO 图形展示数据及预测数据