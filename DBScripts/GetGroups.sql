USE RoomDrawTesting

DELIMITER //
CREATE OR REPLACE PROCEDURE GetGroup(IN gid INT)
BEGIN
	SELECT * FROM Students WHERE group_id = gid;
END//
DELIMITER ;
