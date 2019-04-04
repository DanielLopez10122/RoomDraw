USE RoomDrawTesting
DELIMITER //

CREATE OR REPLACE PROCEDURE GetGroupWishlist(IN gid INT)
BEGIN
	SELECT
	rank AS Rank,
	dorm_id AS Dorm_ID,
	room_id AS Room_ID,
	floor AS Floor

	FROM GroupWishlists WHERE group_id = gid;
END//

CREATE OR REPLACE PROCEDURE DeleteGroupWishlist(IN gid INT, IN pRank INT)
BEGIN
	DELETE FROM GroupWishlists
	WHERE group_id = gid AND rank = pRank;

	UPDATE GroupWishlists
	SET rank = rank - 1
	WHERE group_id = gid AND rank > pRank;
END//

CREATE OR REPLACE PROCEDURE AddGroupWishlist(IN gid INT, IN pRank INT, IN dorm INT, IN room INT, IN pFloor INT)
BEGIN
	-- avoid duplicate key updates.  Whoever came up with this solution
	-- is an absolute genius
	UPDATE GroupWishlists
	SET rank = -rank
	WHERE group_id = gid AND rank >= pRank;

	UPDATE GroupWishlists
	SET rank = -rank + 1
	WHERE group_id = gid AND rank < 0;

	INSERT INTO GroupWishlists
	(group_id, rank, dorm_id, room_id, floor) VALUES

	(gid, pRank, dorm, room, pFloor);
END//

DELIMITER ;
