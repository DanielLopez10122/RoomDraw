CREATE DATABASE IF NOT EXISTS RoomDrawTesting;

USE RoomDrawTesting;

CREATE TABLE IF NOT EXISTS Students(

	student_id INT NOT NULL,
	first_name VARCHAR(64) NOT NULL,
	last_name VARCHAR(64) NOT NULL,
	random_number INT NOT NULL,
	grade_level INT NOT NULL,
	sex ENUM('M', 'F') NOT NULL,
	group_id INT NOT NULL,
	roommate_id INT,

	PRIMARY KEY(student_id)
);

CREATE TABLE IF NOT EXISTS Groups(
	group_id INT NOT NULL,
	random_number INT NOT NULL,
	grade_level INT NOT NULL,
	sex ENUM('M', 'F') NOT NULL,

	PRIMARY KEY(group_id)
);

CREATE TABLE IF NOT EXISTS GroupInvites(
	student_id INT NOT NULL,
	group_id INT NOT NULL,

	PRIMARY KEY (student_id, group_id)
);

CREATE TABLE IF NOT EXISTS Dorms(
	dorm_id INT NOT NULL,
	dorm_code VARCHAR(3) NOT NULL,
	dorm_name VARCHAR(64) NOT NULL,
	sex ENUM('M', 'F') NOT NULL,
	photo BLOB,

	PRIMARY KEY(dorm_id)
);

CREATE TABLE IF NOT EXISTS Rooms(
	room_number INT NOT NULL,
	dorm_id INT NOT NULL,
	capacity INT NOT NULL,
	available_spots INT NOT NULL,
	description VARCHAR(200),
	floor INT NOT NULL,

	PRIMARY KEY(room_number, dorm_id)
);

CREATE TABLE IF NOT EXISTS GroupWishlists(
	group_id INT NOT NULL,
	rank INT NOT NULL,
	dorm_id INT NOT NULL,
	room_id INT,
	floor INT,

	PRIMARY KEY(group_id, rank)
);

CREATE TABLE IF NOT EXISTS StudentWishlists(
	student_id INT NOT NULL,
	rank INT NOT NULL,
	dorm_id INT NOT NULL,
	room_id INT,
	floor INT,

	PRIMARY KEY(student_id, rank)
);

CREATE DATABASE IF NOT EXISTS RoomDraw2018;
