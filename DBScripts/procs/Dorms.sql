USE RoomDrawTesting

DELIMITER //
CREATE OR REPLACE PROCEDURE GetDorm(IN id INT)
BEGIN
	SELECT
	dorm_id AS Dorm_ID,
	dorm_code AS Dorm_Code,
	dorm_name AS Dorm_Name,
	sex AS Sex,
	photo AS Photo

	FROM Dorms WHERE dorm_id = id;
END//
DELIMITER ;

DELIMITER //
CREATE OR REPLACE PROCEDURE GetDorms()
BEGIN
	SELECT
	dorm_id as Dorm_ID,
	dorm_code AS Dorm_Code,
	dorm_name AS Dorm_Name,
	sex AS Sex,
	photo AS Photo

	FROM Dorms;
END//
DELIMITER ;
