
CREATE DATABASE IF NOT EXISTS `ancssc` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `ancssc`;


SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `NGO`;
DROP TABLE IF EXISTS `Statistics`;
DROP TABLE IF EXISTS `Participating_Organisation`;
DROP TABLE IF EXISTS `Projects`;
DROP TABLE IF EXISTS `Contact_Info`;
DROP TABLE IF EXISTS `Country`;
DROP TABLE IF EXISTS `Coordinates`;
DROP TABLE IF EXISTS `Geo_Info`;
DROP TABLE IF EXISTS `Tags`;
DROP TABLE IF EXISTS `Classifications`;
DROP TABLE IF EXISTS `Currency`;
DROP TABLE IF EXISTS `Budget`;
DROP TABLE IF EXISTS `Project_Impact`;
DROP TABLE IF EXISTS `Challanges_And_Solutions`;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE IF NOT EXISTS `Partial_Signup` (
	`ID` int NOT NULL,
	`NGO_NAME` varchar(40) NOT NULL,
	`USERNAME` varchar(20) NOT NULL,
  	`PASSWORD` varchar(40) NOT NULL,

  	PRIMARY KEY (ID)
);


CREATE TABLE IF NOT EXISTS `NGO` (
  `NGO_ID` int NOT NULL,
  `IATI_ID` varchar(255) DEFAULT NULL,
  `REPORTING_ORG` varchar(255) DEFAULT NULL,
  `NGO_NAME` varchar(40) NOT NULL,

  `NGO_SINCE` varchar(45) NOT NULL,
  `USERNAME` varchar(20) NOT NULL,
  `PASSWORD` varchar(40) NOT NULL,

  `REGION` varchar(45) NOT NULL,
  `STREET_ADDRESS` varchar(40) NOT NULL,
  `POST_OR_ZIP` varchar(40) DEFAULT NULL,

  `PHONE` varchar(20) NOT NULL,
  `CONTACT_NAME` varchar(40) NOT NULL,
  `MEMBER_SINCE` varchar(40) NOT NULL,

  `COMPLETED_PROJECTS` INT DEFAULT NULL,
  `TOTAL_PROJECTS` INT NOT NULL,
  `HEADCOUNT` INT NOT NULL,
  `PROJECT_LOCATION` varchar(45) DEFAULT NULL,
  `FOCUS_AREA` varchar(45) NOT NULL,



  PRIMARY KEY (NGO_ID)

);


CREATE TABLE IF NOT EXISTS `Statistics` (
	`ID` int NOT NULL,
	`NGO_ID` int NOT NULL,
	`AVG_PROJECT_BUDGET` varchar(40) NOT NULL,
	`AVERAGE_COMPLETION` varchar(40) DEFAULT NULL,
	`PER_REGION` int NOT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (NGO_ID) REFERENCES NGO(NGO_ID)

);



CREATE TABLE IF NOT EXISTS `Participating_Organisation` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`NAME` varchar(255) DEFAULT NULL,
	`NGO_NAME` int NOT NULL,
	`ROLE` int NOT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES Projects(ID)
);

CREATE TABLE IF NOT EXISTS `Projects` (
	`ID` int NOT NULL,
	`NGO_ID` int NOT NULL,
	`TITLE` varchar(255) NOT NULL,
	`DESCRIPTION` varchar(255) DEFAULT NULL,
	`STATUS` int NOT NULL,
	`START_DATE` date NOT NULL,
	`END_DATE` date NOT NULL,
	`SCOPE` int NOT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (NGO_ID) REFERENCES NGO(NGO_ID)
);

CREATE TABLE IF NOT EXISTS `Contact_Info` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`NAME` varchar(255) NOT NULL,
	`DEPARTMENT` varchar(255) DEFAULT NULL,
	`PERSON_NAME` varchar(255) NOT NULL,
	`JOB_TITLE` varchar(255) NOT NULL,
	`TEL` varchar(255) DEFAULT NULL,
	`EMAIL` varchar(255) NOT NULL,
	`WEBSITE` varchar(255) DEFAULT NULL,
	`MAILING_ADDRESS` varchar(255) NOT NULL,
	

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID)
);


CREATE TABLE IF NOT EXISTS `Coordinates` (
	`ID` int NOT NULL,
	`LAT` int NOT NULL,
	`LONG` int NOT NULL,

	PRIMARY KEY (ID)
);


CREATE TABLE IF NOT EXISTS `Geo_Info` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`COUNTRY` varchar(40) NOT NULL,
	`RECIPIENT_REGION` int NOT NULL,
	`COORDINATES_ID` int NOT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID),
	FOREIGN KEY (COORDINATES_ID) REFERENCES Coordinates(ID)

);

DROP TABLE IF EXISTS `Classifications`;
CREATE TABLE IF NOT EXISTS `Classifications` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`SECTOR` int NOT NULL,
	

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID)
);


CREATE TABLE IF NOT EXISTS `Tags` (
	`ID` int NOT NULL,
	`CLASSIFICATIONS_ID` int NOT NULL,
	`TAG` int NOT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (CLASSIFICATIONS_ID) REFERENCES Classifications(ID)
);





CREATE TABLE IF NOT EXISTS `Budget` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`TYPE` int DEFAULT NULL,
	`STATUS` int DEFAULT NULL,
	`PERIOD_START` date DEFAULT NULL,
	`PERIOD_END` date DEFAULT NULL,
	`VALUE` varchar(255) DEFAULT NULL,
	`CURRENCY` varchar(40) DEFAULT NULL,
	`VALUE_DATE` date DEFAULT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID)

);



CREATE TABLE IF NOT EXISTS `Project_Impact` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`PROJECT_REACH_UNIT` varchar(255) DEFAULT NULL,
	`PROJECT_REACH_TARGET` varchar(255) DEFAULT NULL,
	`PROJECT_REACH_ACTUAL` varchar(255) DEFAULT NULL,
	`TARGET_GROUPS` varchar(255) DEFAULT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID)


);

CREATE TABLE IF NOT EXISTS `Challanges_And_Solutions` (
	`ID` int NOT NULL,
	`PROJECT_ID` int NOT NULL,
	`CHALLANGE_TITLE` varchar(255) NOT NULL,
	`CHALLENGE_STATUS` int NOT NULL,
	`CHALLENGE_TYPE` int NOT NULL,
	`CHALENGE_DESCRIPTION` varchar(255) NOT NULL,
	`SOLUTION_TYPE` int DEFAULT NULL,
	`SOLUTION_DESCRIPTION` varchar(255) DEFAULT NULL,
	`CAN_BE_CONTRACTED` boolean DEFAULT NULL,

	PRIMARY KEY (ID),
	FOREIGN KEY (PROJECT_ID) REFERENCES  Projects(ID)

);





















