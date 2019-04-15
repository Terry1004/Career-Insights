DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Posts CASCADE;
DROP TABLE IF EXISTS Tags CASCADE;
DROP TABLE IF EXISTS Comments CASCADE;
DROP TABLE IF EXISTS Replies CASCADE;

CREATE TABLE Users (
    uni TEXT,
	password TEXT NOT NULL,
	email TEXT NOT NULL,
	personalDescription TEXT NOT NULL DEFAULT '',
    userName TEXT NOT NULL,
	major TEXT NOT NULL DEFAULT '',
	PRIMARY KEY (uni)
);

CREATE TABLE Posts (
	id SERIAL,
	uni TEXT,
	timePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title TEXT NOT NULL,
	content TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (uni) REFERENCES Users
);

CREATE TABLE Tags (
	id SERIAL,
	postId INT UNIQUE NOT NULL,
	postType TEXT NOT NULL,
	rate INT NOT NULL,
	position TEXT NOT NULL,
	company TEXT NOT NULL,
	hashtags TEXT[] NOT NULL DEFAULT '{}',
	domain TEXT NOT NULL DEFAULT '',
	CHECK (rate BETWEEN 1 AND 5),
	CHECK (postType IN (
		'Internship Experience', 'Full-time Experience', 'Interview Experience'
	)),
	PRIMARY KEY (id),
	FOREIGN KEY (postId) REFERENCES Posts
);

CREATE TABLE Comments (
	postId INT,
	commentId INT,
	uni TEXT,
	timePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	content TEXT NOT NULL,
	PRIMARY KEY (postId, commentId),
	FOREIGN KEY (uni) REFERENCES Users ON DELETE SET NULL,
	FOREIGN KEY (postId) REFERENCES Posts (id)
);

CREATE TABLE Replies (
	commentId INT,
	replyId INT,
	postId INT,
	PRIMARY KEY (postId, commentId, replyId),
	FOREIGN KEY (postId, commentId) REFERENCES Comments (postId, commentId) ON DELETE CASCADE,
	FOREIGN KEY (postId, replyId) REFERENCES Comments (postId, commentId) ON DELETE CASCADE
);
