INSERT INTO Users
VALUES 
(
    'yh3065',
    'pbkdf2:sha256:50000$KPBejYUx$a4568de871443efb78989fc252c0874d99b1e25f98f97e32c1a785f4af055729',
    'yh3065@columbia.edu',
    'Hello World!',
    'Yiming Huang',
    'Data Science'
),
(
    'av2845',
    'pbkdf2:sha256:50000$GpGpqYZY$446bfeff09c59b3d779eba51c8cc37941a5d88718393ce837246c1cf715e9f5a',
    'av2845@columbia.edu',
    'Crazy Data Science Grad',
    'Aishwarya',
    'Data Science'
),
(
    'rfc2117',
    'pbkdf2:sha256:50000$njqxec25$f77849137c0521673449393710706e32f387f4aba1f8ced6ae72098e9d615822',
    'rfc2117@columbia.edu',
    'Assistant Director of Student Services',
    'Rachel Fuld Cohen',
    'Psychology'
),
(
    'aj2839',
    'pbkdf2:sha256:50000$VGR6oNcY$5ecb3a614b4f9fe06f64f402a5111d929a5945f2dcc6bca37e5a5b81bd1b2843',
    'aj2839@columbia.edu',
    'MS in DS',
    'Aastha Joshi',
    'Data Science'
),
(
    'alk2225',
    'pbkdf2:sha256:50000$mqSwVOPk$8248dbcf37af443324d4ee4891d308254ecca891fb20164158abff93dc7f5c80',
    'alk2225@columbia.edu',
    'Data for good',
    'Alex Kong',
    'Data Science'
),
(
    'yw3201',
    'pbkdf2:sha256:50000$YADAwbr2$6c3f661c44e358187119f121a39ffa02827f62108b4ffdc12624b4993b9a0dcd',
    'yw3201@columbia.edu',
    'Cool Data Scientist',
    'Yiran Wang',
    'Data Science'
),
(
    'xh2389',
    'pbkdf2:sha256:50000$T3Lbtps8$90cd8138b4b7c3f3a572996e2a0b30153b45dc3a28afb16d47e94f725b3e1c27',
    'xh2389@columbia.edu',
    'Nice Data Scientist',
    'Xinxin Huang',
    'Data Science'
),
(
    'yz3453',
    'pbkdf2:sha256:50000$ilUBkXVC$e2730df6d99be0ef2e38d0d5e2a533b1a62d5638bd6e44cb309f19bc21987e3a',
    'yz3453@columbia.edu',
    'Smart Data Scientist',
    'Yufan Zhuang',
    'Data Science'
),
(
    'cb3441',
    'pbkdf2:sha256:50000$ywmz0tOO$14ec2eb67a18d8978b6372587816c32fb5a9a0eeb77a035c11d416f4fed1fd74',
    'cb3441@columbia.edu',
    'Student Council Member: DSI Studnet Council',
    'Anirudh',
    'Data Science'
),
(
    'nr2409',
    'pbkdf2:sha256:50000$tTLepLgw$0095810e900349c0afa94156a71792b9855ac8a9189800b6c9af7625ae3066c0',
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
),
(
	6,
	17,
	'nr2409',
	'I wanna get started at NLP. Can I contact you privately?'
),
(
	6,
	18,
	'yw3201',
	'Sure, here is my email id - yw3201@columbia.edu'
),
(
	7,
	19,
	'xh2389',
	'Nope. Interest is what matters!!'
),
(
	7,
	20,
	'cb3441',
	'Is prior knowledge in finance required to apply for the company you are working for?'
),
(
	7,
	21,
	'cb3441',
	'Are there any openings for entry level data science internships in your company?'
),
(
	7,
	22,
	'xh2389',
	'I am not sure at this point, I shall get back once I check with my team'
),
(
	7,
	23,
	'cb3441',
	'Thanks a lot for the information and please let me know if any opening is available'
),
(
	7,
	25,
	'av2845',
	'Please let me also know if there are openings. I am also interested'
);

INSERT INTO Replies (commentId, replyId, postId) VALUES
(1, 15, 1),
(2,	14, 2),
(3, 4, 3),
(16, 5, 4),
(26, 6, 5),
(17, 18, 6),
(20, 19, 7),
(21, 22, 7),
(22, 23, 7),
(22, 25, 7);
