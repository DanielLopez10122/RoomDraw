USE RoomDrawTesting
DELIMITER //

CREATE OR REPLACE PROCEDURE GetStudentWishlist(IN sid INT)
BEGIN
	SELECT
	rank AS Rank,
	dorm_id AS Dorm_ID,
	room_id AS Room_ID,
	floor AS Floor

	FROM StudentWishlists WHERE student_id = sid;
END//

CREATE OR REPLACE PROCEDURE DeleteStudentWishlist(IN sid INT, IN pRank INT)
BEGIN
	DELETE FROM StudentWishlists
	WHERE student_id = sid AND rank = pRank;

	UPDATE StudentWishlists
	SET rank = rank - 1
	WHERE student_id = sid AND rank > pRank;
END//

CREATE OR REPLACE PROCEDURE AddStudentWishlist(IN sid INT, IN pRank INT, IN dorm INT, IN room INT, IN pFloor INT)
BEGIN
	-- avoid duplicate key updates.  Whoever came up with this solution
	-- is an absolute genius
	UPDATE StudentWishlists
	SET rank = -rank
	WHERE student_id = sid AND rank >= pRank;

	UPDATE StudentWishlists
	SET rank = -rank + 1
	WHERE student_id = sid AND rank < 0;

	INSERT INTO StudentWishlists
	(student_id, rank, dorm_id, room_id, floor) VALUES
	
	(sid, pRank, dorm, room, pFloor);
END//

DELIMITER ;
