SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `vote_account`
-- ----------------------------
DROP TABLE IF EXISTS `vote_account`;
CREATE TABLE `vote_account` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(128) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sitename` varchar(200) NOT NULL,
  `priority` int(10) DEFAULT '0',
  `proxy` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uc_PersonID` (`login`,`sitename`),
  KEY `login_index` (`login`),
  KEY `sitename_index` (`sitename`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for `vote_vote`
-- ----------------------------
DROP TABLE IF EXISTS `vote_vote`;
CREATE TABLE `vote_vote` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sitename` varchar(255) NOT NULL,
  `account_id` int(10) unsigned NOT NULL,
  `date` varchar(255) NOT NULL,
  `top` varchar(255) NOT NULL,
  `ip` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_date` (`date`),
  KEY `index_sitename` (`sitename`),
  KEY `index_top` (`top`),
  KEY `fk_account` (`account_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

