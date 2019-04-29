USE RoomDrawTesting
DELIMITER //
CREATE OR REPLACE PROCEDURE GetStudent(IN sid INT)
BEGIN
	SELECT
	s.student_id AS Student_ID,
	s.first_name AS First_Name,
	s.last_name AS Last_Name,
	g.random_number AS Random_No,
	g.grade_level AS Grade_Level,
	s.sex AS Sex,
	s.group_id AS Group_ID,
	s.roommate_id AS Roommate_ID

	FROM Students s JOIN Groups g
	ON s.group_id = g.group_id
	WHERE s.student_id = sid;
END//
DELIMITER ;
