USE RoomDrawTesting
DELIMITER //
CREATE OR REPLACE PROCEDURE GetStudent(IN sid INT)
BEGIN
	SELECT
	student_id AS Student_ID,
	first_name AS First_Name,
	last_name AS Last_Name,
	random_number AS Random_No,
	grade_level AS Grade_Level,
	sex AS Sex,
	group_id AS Group_ID,
	roommate_id AS Roommate_ID

	FROM Students WHERE student_id = sid;
END//
DELIMITER ;
