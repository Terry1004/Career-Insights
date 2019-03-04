DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Posts CASCADE;
DROP TABLE IF EXISTS Tags CASCADE;
DROP TABLE IF EXISTS Comments CASCADE;
DROP TABLE IF EXISTS Replies CASCADE;

CREATE TABLE Users (
    uni TEXT,
	email TEXT NOT NULL,
	personalDescription TEXT,
    userName TEXT NOT NULL,
	major TEXT,
	PRIMARY KEY (uni)
);

CREATE TABLE Posts (
	id SERIAL,
	uni TEXT,
	timePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title TEXT NOT NULL,
	content TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (uni) REFERENCES Users
);

CREATE TABLE Tags (
	id SERIAL,
	postId INT UNIQUE NOT NULL,
	postType TEXT,
	rate INT,
	position TEXT,
	company TEXT,
	hashtags TEXT[],
	domain TEXT,
	CHECK (rate BETWEEN 0 AND 5),
	PRIMARY KEY (id),
	FOREIGN KEY (postId) REFERENCES Posts
);

CREATE TABLE Comments (
	postId INT,
	commentId INT,
	uni TEXT NOT NULL,
	timePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	content TEXT,
	PRIMARY KEY (postId, commentId),
	FOREIGN KEY (uni) REFERENCES Users,
	FOREIGN KEY (postId) REFERENCES Posts (id) ON DELETE CASCADE
);

CREATE TABLE Replies (
	commentId INT,
	replyId INT,
	postId INT,
	PRIMARY KEY (postId, commentId, replyId),
	FOREIGN KEY (postId, commentId) REFERENCES Comments (postId, commentId),
	FOREIGN KEY (postId, replyId) REFERENCES Comments (postId, commentId)
);
