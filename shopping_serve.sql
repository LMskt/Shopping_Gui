/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 8.0.26 : Database - shopping_serve
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopping_serve` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `shopping_serve`;

/*Table structure for table `commodity` */

DROP TABLE IF EXISTS `commodity`;

CREATE TABLE `commodity` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `NAME` varchar(255) NOT NULL COMMENT '名字',
  `price` int NOT NULL COMMENT '价格',
  `number` int NOT NULL COMMENT '数量',
  `img` varchar(255) DEFAULT NULL COMMENT '照片',
  `introduce` varchar(255) DEFAULT NULL COMMENT '商品介绍',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

/*Data for the table `commodity` */

insert  into `commodity`(`id`,`NAME`,`price`,`number`,`img`,`introduce`) values 
(1,'辣条',300,23,'asdasd','无敌好吃'),
(2,'卫龙',122,12,'asdasdas','还可以');

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `userid` int NOT NULL COMMENT '用户id',
  `commodityid` int NOT NULL COMMENT '商品id',
  `NUMBER` int NOT NULL COMMENT '数量',
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '购买时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

/*Data for the table `orders` */

insert  into `orders`(`id`,`userid`,`commodityid`,`NUMBER`,`time`) values 
(1,2,2,2,'2021-12-23 03:04:20'),
(2,2,2,5,NULL),
(3,2,2,5,'2021-12-23 03:11:40');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(255) NOT NULL COMMENT '账号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `name` varchar(255) NOT NULL COMMENT '名字',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`name`) values 
(1,'123','123','龙庆'),
(3,'asda','asda','asdas');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
