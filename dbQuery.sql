CREATE TABLE Users (
	Id int identity(1,1) PRimary key,
	username nvarchar(30) NOT NULL,
	password_hash BINARY(64) NOT NULL,
	email nvarchar(100) NOT NULL
);

INSERT INTO dbo.[Users] (username, password_hash, email)
	VALUES('wanjing', HASHBYTES('SHA2_512', 'wj923'), 'lwj@gmail.com')
