-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
SET
character_set_client = utf8mb4 ;
CREATE TABLE `student`
(
    `id`      int(11) NOT NULL AUTO_INCREMENT,
    `name`    varchar(255) DEFAULT NULL,
    `chinese` float        DEFAULT NULL,
    `math`    float        DEFAULT NULL,
    `english` float        DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK
TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student`
VALUES (1, '胡秀英', 77, 75, 51),
       (2, '李玉珍', 58, 40, 72),
       (3, '王超', 78, 96, 56),
       (4, '宋婷', 99, 64, 84),
       (5, '吴桂香', 75, 92, 43),
       (6, '范鹏', 94, 93, 95),
       (7, '钟淑兰', 70, 80, 46),
       (8, '刘桂芝', 49, 59, 94),
       (9, '王畅', 66, 64, 96),
       (10, '谢秀华', 78, 63, 59),
       (11, '王宇', 59, 66, 94),
       (12, '陈兰英', 67, 44, 71),
       (13, '杜刚', 44, 82, 92),
       (14, '鲁超', 62, 85, 59),
       (15, '陈静', 53, 51, 81),
       (16, '郑玉梅', 51, 72, 57),
       (17, '郭丹丹', 40, 44, 81),
       (18, '李玉兰', 94, 68, 74),
       (19, '高刚', 95, 89, 74),
       (20, '张成', 96, 52, 78);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK
TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-15 21:38:45
