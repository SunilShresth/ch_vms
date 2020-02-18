-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: vms
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `visitorinfo`
--

DROP TABLE IF EXISTS `visitorinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `visitorinfo` (
  `id` bigint(12) NOT NULL AUTO_INCREMENT,
  `photo` varchar(500) DEFAULT NULL,
  `firstname` varchar(128) DEFAULT NULL,
  `lastname` varchar(128) DEFAULT NULL,
  `purpose` varchar(128) DEFAULT NULL,
  `sent_department` varchar(64) DEFAULT NULL,
  `organization` varchar(128) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `emailid` varchar(128) DEFAULT NULL,
  `ch_personnel` varchar(200) DEFAULT NULL,
  `checkin` datetime DEFAULT NULL,
  `checkout` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `checkin` (`checkin`),
  KEY `checkout` (`checkout`),
  KEY `mobile` (`phone`)
) ENGINE=MyISAM AUTO_INCREMENT=181 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitorinfo`
--

LOCK TABLES `visitorinfo` WRITE;
/*!40000 ALTER TABLE `visitorinfo` DISABLE KEYS */;
INSERT INTO `visitorinfo` VALUES (156,'static/photo/databasepng','sunil','shrestha','Mounting new server','Data Center','Cloud Himalaya','9812345678','sunil.shrestha@cloudhimalaya.com',NULL,'2020-01-29 13:09:39','2020-01-29 14:50:19',0),(157,'static/photo/Screenshot_from_2019-03-11_17-27-10.png','Parash','Kafle','Install new Device','Data Center','Cloud Himalaya','9812345672','parash.kafle@cloudhimalaya.com',NULL,'2020-01-29 14:51:19','2020-01-29 14:52:11',0),(158,'static/photo/Screenshot_from_2019-03-11_17-32-22.png','Prakash','Thapa','Install new Device','DC','Cloud Himalaya','9812345678','prakash.thapa@cloudhimalaya.com',NULL,'2020-01-29 15:24:58','2020-02-13 15:27:51',0),(159,'static/photo/02.jpg','Safalta','Shrestha','Regular Visit','DC','Cloud Himalaya','9812345679','safalta.shrestha@cloudhimalaya.com',NULL,'2020-01-29 15:54:33','2020-01-29 17:28:20',0),(160,'static/photo/02.jpg','Safalta','Shrestha','Regular Visit','DC','Cloud Himalaya','9812345679','safalta.shrestha@cloudhimalaya.com',NULL,'2020-01-29 15:55:32','2020-02-13 15:27:55',0),(161,'static/photo/Screenshot_from_2019-03-29_14-05-31.png','Abhisek','Sunwar','Cable Taging ','DC','Cloud Himalaya','9812345672','abhisek.sunwar@cloudhimalaya.com',NULL,'2020-01-30 18:40:14','2020-02-03 08:59:18',0),(162,'static/photo/Screenshot_from_2019-03-28_14-10-50.png','Ranjan','Regmi','Install new Device','DC','Cloud Himalaya','9812345679','ranjan.regmi@cloudhimalaya.com',NULL,'2020-01-31 08:50:50','2020-01-31 08:51:37',0),(163,'static/photo\\WIN_20181105_17_10_12_Pro.jpg','Sahan','Shrestha','Cable Tagg','DC','Cloud Himalaya','9812345678','sahan.shrestha@cloudhimalaya.com',NULL,'2020-02-10 16:07:17',NULL,1),(164,'static/photo\\Screenshot_14.png','Sirjan','Shrestha','Configuring vms server','DC','Cloud Himalaya','9812345678','sirjan.shrestha@cloudhimalaya.com',NULL,'2020-02-16 20:33:16',NULL,1),(165,'static/photo/Screenshot_14.png','Sirjan','Shrestha','removing cisco switch','DC','Cloud Himalaya','9812345678','sirjan.shrestha@cloudhimalaya.com',NULL,'2020-02-16 21:40:39',NULL,1),(166,'static/photo/Screenshot_1.png','Ayush','Ghimire','Mounting Server','DC','Cloud Himalaya','9812345678','ayush.ghimire@cloudhimalaya.com',NULL,'2020-02-16 21:47:22','2020-02-16 21:58:32',0),(167,'static/photo/Screenshot_1.png','Ayush','Ghimire','Mounting Server','DC','Cloud Himalaya','9812345678','ayush.ghimire@cloudhimalaya.com',NULL,'2020-02-16 21:58:22',NULL,1),(168,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Manu','Shrestha','Mounting Server','DC','Cloud Himalaya','9812345678','manu.shrestha@cloudhimalaya.com',NULL,'2020-02-17 10:51:18','2020-02-17 11:14:35',0),(169,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Manu','Shrestha','Cable Tagg','DC','Cloud Himalaya','9812345678','manu.shrestha@cloudhimalaya.com',NULL,'2020-02-17 13:35:13',NULL,1),(170,'static/photo/databasepng','sunil','shrestha','Mounting new server','Data Center','Cloud Himalaya','9812345678','sunil.shrestha@cloudhimalaya.com',NULL,'2020-02-17 13:39:41',NULL,1),(171,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Manu','Shrestha','Cable Tagg','DC','Cloud Himalaya','9812345678','manu.shrestha@cloudhimalaya.com',NULL,'2020-02-17 13:40:33',NULL,1),(172,'static/photo/WIN_20200217_14_14_51_Pro.jpg','Ayush','Ghimire','Regular visit','DC','Cloud Himalaya','9812345678','ayush.ghimire@cloudhimalaya.com',NULL,'2020-02-17 14:15:14','2020-02-17 14:15:44',0),(173,'static/photo/WIN_20200217_14_14_51_Pro.jpg','Ayush','Ghimire','Cable Tagg','DC','Cloud Himalaya','9812345678','ayush.ghimire@cloudhimalaya.com',NULL,'2020-02-17 14:16:20',NULL,1),(174,'static/photo/WIN_20200217_14_18_47_Pro.jpg','Ranjan','Regmi','He is bored','DC','Cloud Himalaya','9812345678','ranjan.regmi@cloudhimalya.com',NULL,'2020-02-17 14:18:58','2020-02-17 14:19:26',0),(175,'static/photo/WIN_20200217_14_18_47_Pro.jpg','Ranjan','Regmi','Mounting Server','DC','Cloud Himalaya','9812345678','ranjan.regmi@cloudhimalya.com',NULL,'2020-02-17 14:20:03','2020-02-17 22:21:35',0),(176,'static/photo/WIN_20200217_14_18_47_Pro.jpg','Vinaya','Shakya','Mounting New servers','DC','Vianet','9812345678','vinaya.shakya@vianet.com',NULL,'2020-02-17 22:18:54','2020-02-17 22:19:06',0),(177,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Niranjan','Bohora','Cisco Switch Configuration','DC','Black and Green','9812345678','niranjan.bohora@bng.com',NULL,'2020-02-17 22:21:04','2020-02-17 22:21:37',0),(178,'static/photo/uploading_progress.PNG','Ram Parsad','Yadav','Cable Tag','DC','Blue and White','9812345678','ram.prasad.yadav@blueandwhite.com',NULL,'2020-02-17 22:23:37',NULL,1),(179,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Anil','Tamang','replacing juniper router','DC','Broadlink','9812345678','anil.tamang@broadlink.com',NULL,'2020-02-17 23:17:38',NULL,1),(180,'static/photo/WIN_20200217_10_50_55_Pro.jpg','Anil','Tamang','replacing juniper router','DC','Broadlink','9812345678','anil.tamang@broadlink.com','Aayush Ghimire','2020-02-17 23:33:20',NULL,1);
/*!40000 ALTER TABLE `visitorinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-18 14:44:48
