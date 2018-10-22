CREATE DATABASE RoomDrawTesting;

USE RoomDrawTesting;

CREATE TABLE Students(

	student_id INT NOT NULL,
	first_name VARCHAR(64) NOT NULL,
	last_name VARCHAR(64) NOT NULL,
	random_number INT NOT NULL,
	grade_level INT NOT NULL,
	sex ENUM('M', 'F') NOT NULL,
	group_id INT,
	roommate_id INT,

	PRIMARY KEY(student_id)
);

CREATE TABLE Groups(
	group_id INT NOT NULL,
	radom_number INT NOT NULL,
	grade_level INT NOT NULL,
	sex ENUM('M', 'F') NOT NULL,

	PRIMARY KEY(group_id)
);

CREATE TABLE Dorms(
	dorm_id INT NOT NULL,
	dorm_code VARCHAR(3) NOT NULL,
	dorm_name VARCHAR(64) NOT NULL,
	sex ENUM('M', 'F') NOT NULL,

	PRIMARY KEY(dorm_id)
);

CREATE TABLE Rooms(
	room_id INT NOT NULL,
	dorm_id INT NOT NULL,
	capacity INT NOT NULL,
	available_spots INT NOT NULL,
	description VARCHAR(200),
	floor INT NOT NULL,

	PRIMARY KEY(room_id)
);

CREATE TABLE GroupWishlists(
	group_id INT NOT NULL,
	rank INT NOT NULL,
	dorm_id INT NOT NULL,
	room_id INT,
	floor INT
);

CREATE TABLE StudentWishlists(
	student_id INT NOT NULL,
	rank INT NOT NULL,
	dorm_id INT NOT NULL,
	room_id INT,
	floor INT
);


CREATE DATABASE RoomDraw2018;
