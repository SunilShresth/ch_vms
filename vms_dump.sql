-- MySQL dump 10.14  Distrib 5.5.64-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: VMS
-- ------------------------------------------------------
-- Server version	5.5.64-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
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
  `checkin` datetime DEFAULT NULL,
  `checkout` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `checkin` (`checkin`),
  KEY `checkout` (`checkout`),
  KEY `mobile` (`phone`)
) ENGINE=MyISAM AUTO_INCREMENT=163 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitorinfo`
--

LOCK TABLES `visitorinfo` WRITE;
/*!40000 ALTER TABLE `visitorinfo` DISABLE KEYS */;
INSERT INTO `visitorinfo` VALUES (156,'static/photo/databasepng','sunil','shrestha','Mounting new server','Data Center','Cloud Himalaya','9812345678','sunil.shrestha@cloudhimalaya.com','2020-01-29 13:09:39','2020-01-29 14:50:19',0),(157,'static/photo/Screenshot_from_2019-03-11_17-27-10.png','Parash','Kafle','Install new Device','Data Center','Cloud Himalaya','9812345672','parash.kafle@cloudhimalaya.com','2020-01-29 14:51:19','2020-01-29 14:52:11',0),(158,'static/photo/Screenshot_from_2019-03-11_17-32-22.png','Prakash','Thapa','Install new Device','DC','Cloud Himalaya','9812345678','prakash.thapa@cloudhimalaya.com','2020-01-29 15:24:58','2020-01-31 08:27:06',0),(159,'static/photo/02.jpg','Safalta','Shrestha','Regular Visit','DC','Cloud Himalaya','9812345679','safalta.shrestha@cloudhimalaya.com','2020-01-29 15:54:33','2020-01-29 17:28:20',0),(160,'static/photo/02.jpg','Safalta','Shrestha','Regular Visit','DC','Cloud Himalaya','9812345679','safalta.shrestha@cloudhimalaya.com','2020-01-29 15:55:32','0000-00-00 00:00:00',1),(161,'static/photo/Screenshot_from_2019-03-29_14-05-31.png','Abhisek','Sunwar','Cable Taging ','DC','Cloud Himalaya','9812345672','abhisek.sunwar@cloudhimalaya.com','2020-01-30 18:40:14','2020-02-03 08:59:18',0),(162,'static/photo/Screenshot_from_2019-03-28_14-10-50.png','Ranjan','Regmi','Install new Device','DC','Cloud Himalaya','9812345679','ranjan.regmi@cloudhimalaya.com','2020-01-31 08:50:50','2020-01-31 08:51:37',0);
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

-- Dump completed on 2020-02-05 11:41:13
