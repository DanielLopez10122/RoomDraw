USE RoomDrawTesting

DELIMITER //
CREATE OR REPLACE PROCEDURE GetGroupInfo(IN gid INT)
BEGIN
	SELECT
	group_id AS Group_ID,
	random_number AS Random_Number,
	grade_level AS Grade_Level

	FROM Groups WHERE group_id = gid;
END//

CREATE OR REPLACE PROCEDURE GetGroupMembers(IN gid INT)
BEGIN
	SELECT
	student_id AS Student_ID,
	first_name AS First_Name,
	last_name AS Last_Name,
	random_number AS Random_Number,
	grade_level AS Grade_Level,
	sex AS Sex,
	group_id AS Group_ID,
	roommate_id AS Roommate_ID

	FROM Students WHERE group_id = gid;
END//

CREATE OR REPLACE PROCEDURE LeaveGroup(IN sid INT)
BEGIN
	SET @old_gid = (SELECT group_id FROM Students WHERE student_id = sid);

	UPDATE Students
	SET group_id = sid
	WHERE student_id = sid;

	SET @new_gid = (SELECT student_id FROM Students WHERE group_id = @old_gid AND student_id <> sid LIMIT 1);
	-- SET @grade   = (SELECT grade_level FROM Students WHERE group_id = @old_gid);

	UPDATE Groups
	SET group_id = @new_gid
	WHERE group_id = @old_gid;

	UPDATE Students
	SET group_id = @new_gid
	WHERE group_id = @old_gid AND student_id <> sid;

	SET @rand    = (SELECT random_number FROM Students WHERE group_id = @new_gid ORDER BY random_number LIMIT 1);

	UPDATE Groups
	SET random_number = @rand
	WHERE group_id = @new_gid;
END//

CREATE OR REPLACE PROCEDURE InviteToGroup(IN sid INT, IN gid INT)
BEGIN
	INSERT INTO GroupInvites
	(student_id, group_id) VALUES (sid, gid);
END//

CREATE OR REPLACE PROCEDURE GetInvitations(IN sid INT)
BEGIN
	SELECT group_id FROM GroupInvites
	WHERE student_id = sid;
END//

CREATE OR REPLACE PROCEDURE AcceptInvitation(IN sid INT, IN gid INT)
BEGIN
	DELETE FROM GroupInvites
	WHERE student_id = sid;

	UPDATE Students
	SET group_id = gid
	WHERE student_id = sid;

	SET @rand = (SELECT random_number FROM Students WHERE group_id = gid ORDER BY random_number LIMIT 1);

	UPDATE Groups SET random_number = @new_rand WHERE group_id = gid;
END//

CREATE OR REPLACE PROCEDURE DeclineInvitation(IN sid INT, IN gid INT)
BEGIN
	DELETE FROM GroupInvites
	WHERE student_id = sid AND group_id = gid;
END//
DELIMITER ;
