INSERT INTO Users
VALUES 
(
    'yh3065',
    'yh3065@columbia.edu',
    'Hello World!',
    'Yiming Huang',
    'Data Science'
),
(
    'av2845',
    'av2845@columbia.edu',
    'Crazy Data Science Grad',
    'Aishwarya',
    'Data Science'
),
(
    'rfc2117',
    'rfc2117@columbia.edu',
    'Assistant Director of Student Services',
    'Rachel Fuld Cohen',
    'Psychology'
),
(
    'aj2839',
    'aj2839@columbia.edu',
    'MS in DS',
    'Aastha Joshi',
    'Data Science'
),
(
    'alk2225',
    'alk2225@columbia.edu',
    'Data for good',
    'Alex Kong',
    'Data Science'
),
(
    'yw3201',
    'yw3201@columbia.edu',
    'Cool Data Scientist',
    'Yiran Wang',
    'Data Science'
),
(
    'xh2389',
    'xh2389@columbia.edu',
    'Nice Data Scientist',
    'Xinxin Huang',
    'Data Science'
),
(
    'yz3453',
    'yz3453@columbia.edu',
    'Smart Data Scientist',
    'Yufan Zhuang',
    'Data Science'
),
(
    'cb3441',
    'cb3441@columbia.edu',
    'Student Council Member: DSI Studnet Council',
    'Anirudh',
    'Data Science'
),
(
    'nr2409',
    'nr2409@columbia.edu',
    'Product Manager at Wayfair',
    'Nikhil Raman',
    'Data Science'
);

INSERT INTO Posts (uni, title, content)
VALUES
(
    'yh3065',
    'Software Engineer Intern',
    'During the software engineer internship, I have gained a lot of hands-on practice on production level coding with the help of my mentor. It is a great place to work!'
),
(
    'av2845',
	'Senior Software Engineer',
    'As a big data engineer at Ericsson, I had good hands-on exposure to all the cutting edge big data distributed systems. Ericsson is a fun place to work.'
),
(
    'rfc2117',
	'Assistant Director of Student Services',
    'Columbia DSI is a great place to work. I enjoy working with DSIers. They are cool.'
),
(
    'aj2839',
	'Software Developer Intern',
    'Developed AAC app for children with Cerebral palsy, Autism & speech difficulty. It was great.'
),
(
    'alk2225',
	'Data Scientist at INCITE',
    'Working on setting an index for educational institutions. The lab provides great opportunities.'
),
(
    'yw3201',
	'Research assistant at stackNLP',
    'Great NLP work !!!'
),
(
    'xh2389',
    'Assistant data analyst',
    'Collaborated with product management team of Ping An Bank to identify, verify and assemble financial data for analysis to identify target customers.'
),
(
    'yz3453',
	'Research assistant',
    'Google''s interview is very difficult, but I finally made it. Hurray!' 
),
(
    'nr2409',
	'Product Manager',
    'The inerviewer is very nice!'
),
(
    'cb3441',
	'Deep learning Researcher',
    'Involved in deep learning research at columbia. The opportunity is fantastic!'
);

INSERT INTO Tags (
    postId, postType, rate, position, company, hashtags, domain
) VALUES
(
    1,
    'Internship Experience',
    4,
    'Software Engineer',
    'iFlytek Toycloud Ltd Co.',
    '{"developer","helloworld"}',
    'Software Engineer'
),
(
    2,
    'Full-time Experience',
    3,
    'Senior Software Engineer',
    'Ericsson India',
    '{"bigdatalife"}',
    'Big Data'
),
(
    3,
    'Full-time Experience',
    5,
    'Assistant Director',
    'Columbia University',
    '{"columbia","DSI"}',
    'Management'
),
(
    4,
    'Internship Experience',
    3,
    'Software Engineer',
    'Industrial Design Centre',
    '{"mobile development"}',
    'Software Engineer'
),
(
    5,
    'Full-time Experience',
    4,
    'Data Scientist',
    'INCITE',
    '{"data","research"}',
    'Data Science'
),
(
    6,
    'Full-time Experience',
    3,
    'Research Assistant',
    'stackNLP',
    '{"NLP","research","startup"}',
    'Data Science'
),
(
    7,
    'Full-time Experience',
    5,
    'Data Analyst',
    'Ping An Bank',
    '{"finance","bigdata"}',
    'Finance'
),
(
    8,
    'Interview Experience',
    4,
    'Research Assistant',
    'Google',
    '{"NLP","datatheworld"}',
    'Data Science'
),
(
    9,
    'Interview Experience',
    5,
    'Product Manager',
    'Wayfair',
    '{"bussiness","nicewayfair"}',
    'Management'
),
(
    10,
    'Intenrship Experience',
    4,
    'Research Assistant',
    'Columbia University',
    '{"columbia","deep learning", "research"}',
    'Data Science'
);

INSERT INTO Comments (postId, commentId, uni, content) VALUES
(
	1,
	1,
	'av2845',
	'Can you share one specific use case that you implemented for the business?'
),
(
	2,
	2,
	'alk2225',
	'How was the work life balance at Ericsson?'
),
(
	3,
	3,
	'yh3065',
	'What is different about columbia compared to other universities?'
),
(
	1,
	15,
	'yh3065',
	'I developed a web application and designed the front of our product. It was well brainstormed and appreciated.'
),
(
	2,
	14,
	'av2845',
	'Work life balance is awesome. All you need to do is get the job done on time. No one really bothers you about your ways of working'
),
(
	4,
	16,
	'av2845',
	'What was the most motivational part about your job?'
),
(
	3,
	4,
	'rfc2117',
	'Columbia got the brightest students from across the world. It is fun and interesting to help them get great jobs!!'
),
(
	4,
	5,
	'aj2839',
	'Motivation came from being helpful to the differently abled children'
),
(
	5,
	26,
	'yw3201',
	'What was the most exciting thing about your job?'
),
(
	5,
	6,
	'alk2225',
	'Researching on educational institutions is great because it uncovers a lot of truth.'
);

INSERT INTO Replies (commentId, replyId, postId) VALUES
(1, 1, 1),
(2, 2, 2),
(6, 3, 5),
(26, 4, 5),
(5, 5, 4),
(4, 6, 3),
(16, 7, 4),
(14, 8, 2),
(15, 9, 1),
(3, 10, 3);
