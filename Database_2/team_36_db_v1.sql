
CREATE DATABASE IF NOT EXISTS `knowledgebase` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `knowledgebase`;


CREATE TABLE IF NOT EXISTS `Organisation` (
  `ID` int NOT NULL,
  `ORG_NAME` varchar(255) DEFAULT NULL,
  `PDF_NAME` varchar(255) DEFAULT NULL
  PRIMARY KEY (ANCSSC_ID)
);

