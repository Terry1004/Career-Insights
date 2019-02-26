DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Posts CASCADE;
DROP TABLE IF EXISTS Tags CASCADE;

CREATE TABLE Users (
    uni TEXT,
	email TEXT NOT NULL,
	personalDescription TEXT,
    userName TEXT,
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
