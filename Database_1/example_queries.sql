USE `ancssc`;

BEGIN;
INSERT INTO NGO (NGO_NAME, NGO_SINCE, USERNAME, PASSWORD, REGION, STREET_ADDRESS, PHONE, CONTACT_NAME, MEMBER_SINCE, TOTAL_PROJECTS, HEADCOUNT, FOCUS_AREA)
	VALUES('example ngo', '2014', 'example_ngo', 'hunter2', 'west', '44 fake street', '+440394034834', 'mary', '2015', 5, 5, 'focused');
COMMIT;



BEGIN;
INSERT INTO PROJECTS (NGO_ID, TITLE, STATUS, START_DATE, END_DATE, SCOPE)
	VALUES(1, 'teaching people with diabetes to do handstands', 1, '2019-01-01', '2021-01-01', 2);
COMMIT;

BEGIN;
INSERT INTO PROJECTS (NGO_ID, TITLE, STATUS, START_DATE, END_DATE, SCOPE)
	VALUES(1, 'teaching disabled dogs to roll over', 2, '2016-05-03', '2022-01-01', 2);
COMMIT;


BEGIN;
INSERT INTO Contact_Info (PROJECT_ID, CONTACT_ORG_NAME, PERSON_NAME, JOB_TITLE, EMAIL, MAILING_ADDRESS)
	VALUES(1, 'example ngo - us headquarters', 'mary', 'head of communications', 'mary@examplengo.net', 'example ngo headquarters, 44 fake street, los angeles, texas, US')
COMMIT;


SELECT proj.`TITLE`
	from Projects proj
	join NGO ngo on ngo.`NGO_ID` = proj.`NGO_ID`
	where ngo.`NGO_NAME` = 'example ngo'


SELECT c.PERSON_NAME, c.DETAILS
	from Contact_Info c 
	join Projects p on p.`ID` = c.`PROJECT_ID`
	where p.`TITLE` = 'teaching people with diabetes to do handstands'



BEGIN;
INSERT INTO Partial_Signup (NGO_ID, TITLE, STATUS, START_DATE, END_DATE, SCOPE)
	VALUES(1, 'teaching people with diabetes to do handstands', 1, '2019-01-01', '2021-01-01', 2);
COMMIT;
