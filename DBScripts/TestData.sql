USE RoomDrawTesting

REPLACE INTO Students (student_id, first_name, last_name, random_number, grade_level, sex, group_id, roommate_id) VALUES
(0,  "alex",     "maese",    928,    3,  'M',  0,  NULL),
(1,  "denton",   "luns",     94819,  3,  'M',  1,  NULL),
(2,  "eli",      "pruneda",  1,      3,  'M',  2,  NULL),
(3,  "michael",  "grimmig",  491,    3,  'M',  3,  NULL);

REPLACE INTO Groups (group_id, random_number, grade_level, sex) VALUES
(0,  928,    3,  'M'),
(1,  94819,  3,  'M'),
(2,  1,      3,  'M'),
(3,  491,    3,  'M');

REPLACE INTO Dorms (dorm_id, dorm_code, dorm_name, sex, photo) VALUES
(0,  "STJ",  "St. Joseph Hall",     'M',  NULL),
(1,  "MIK",  "St. Michael Hall",    'M',  NULL),
(2,  "TUR",  "Turner Hall",         'M',  NULL),
(3,  "NEW",  "Newman",              'M',  NULL),
(4,  "LIZ",  "St. Elizabeth Hall",  'F',  NULL),
(5,  "KRE",  "Kremeter Hall",       'F',  NULL);

REPLACE INTO Rooms (room_number, dorm_id, capacity, available_spots, description, floor) VALUES
(1, 0, 2, 2, NULL, 1),
(2, 0, 2, 2, NULL, 1),
(3, 0, 2, 2, NULL, 1),
(1, 1, 2, 2, NULL, 1);
