USE RoomDrawTesting

DELIMITER //
CREATE OR REPLACE PROCEDURE GetRooms(IN dormid INT,
	IN rnumber INT, IN spots_left INT, IN floor INT)
BEGIN
	SELECT
	room_number as Room_Number,
	dorm_id AS Dorm_ID,
	capacity AS Capacity,
	available_spots AS Available_Spots,
	description AS Description,
	floor AS Floor

	FROM Rooms WHERE dorm_id = id;
END//
DELIMITER ;
