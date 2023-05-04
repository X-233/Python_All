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
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
SET
character_set_client = utf8mb4 ;
CREATE TABLE `article`
(
    `id`        int(11) NOT NULL AUTO_INCREMENT,
    `title`     varchar(255) DEFAULT NULL,
    `body`      text,
    `author_id` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK
TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article`
VALUES (1, '剑来', '...', 1),
       (2, '雪中悍刀行', '...', 1),
       (3, '星辰变', '...', 2),
       (4, '沧元图', '...', 2),
       (5, '飞剑问道', '...', 2),
       (6, '圣墟', '...', 3),
       (7, '遮天', '...', 3),
       (8, '完美世界', '...', 3),
       (9, 'python开发', '...', 5);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
SET
character_set_client = utf8mb4 ;
CREATE TABLE `author`
(
    `id`    int(11) NOT NULL AUTO_INCREMENT,
    `name`  varchar(50) NOT NULL,
    `phone` varchar(11) NOT NULL,
    `hobby` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `phone` (`phone`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK
TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author`
VALUES (1, '烽火戏诸侯', '110110', '吃饭'),
       (2, '我吃西红柿', '110111', '睡觉'),
       (3, '辰东', '110112', '打豆豆'),
       (4, '正心', '110119', '写代码');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK
TABLES;

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

-- Dump completed on 2023-03-15 21:42:12
