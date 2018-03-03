--[USER]--
--User Table--
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id serial NOT NULL PRIMARY KEY,
  username varchar(50) NOT NULL,
  password varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  deleted boolean default 'false'
);

--[ITEMS]--
--Item Table--
DROP TABLE IF EXISTS items;
CREATE TABLE items (
  itemId serial primary key,
  name text Not Null,
  itype text,
  price int,
  imgurl text,
  deleted boolean default 'false'
);

drop table if exists logs;
create table logs(
  logId serial primary key,
  logFoo text,
  fooVal text,
  logDate text,
  logReturn text,
  deleted boolean default False
);

--Stored Procs
--addPost
create or replace function add_item(p_price int, p_name text, p_itype text, p_imgurl text)
	returns text as
$$
declare
	v_itemId int;
begin
	select into v_itemId itemId from items
		where price = p_price and name = p_name and itype = p_itype and p_imgurl = imgurl;

		if v_itemId isnull then
			insert into items(price, name, itype, imgurl)
				values (p_price, p_name, p_itype, p_imgurl);
			return 'OK';
		else
			update items
				set price = p_price, name = p_name, itype = p_itype, imgurl = p_imgurl
					where itemId = v_itemId;
				return 'OK';
		end if;
	end;
$$
	language 'plpgsql';
--

--getAllPost
create or replace function get_all_items(out int, out text, out text, out int, out text)
	returns setof record as
$$
	select itemId, name, itype, price, imgurl from items
		where deleted = False;
$$
	language 'sql';
--

--getPostSection
create or replace function get_item_section(in int, in int, out int, out text, out text, out int, out text)
	returns setof record as
$$
	select itemId, name, itype, price, imgurl from items
		where itemId >= $1 and itemId <= ($1+$2);
$$
	language 'sql';
--

--getPost
create or replace function get_item(in int, out int, out text, out text, out int, out text)
	returns setof record as
$$
	select itemId, name, itype, price, imgurl from items
		where itemId = $1 and deleted = False;
$$
	language 'sql';
--

--updatePost
create or replace function update_item(p_itemId int, p_new_name text, p_new_type text, p_new_price int, p_new_imgurl text)
	returns text as
	$$
	begin
	update items
		set name = p_new_name,
		itype = p_new_type,
    price = p_new_price,
    imgurl = p_new_imgurl
		where itemId = p_itemId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--

--deletePost
create or replace function delete_item(p_itemId int)
	returns text as
	$$
	begin
	update items
		set deleted = True
		where itemId = p_itemId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--

--addUser
create or replace function add_user(p_userName text, p_userPass text, p_userEmail text)
	returns text as
$$
declare
	v_userId int;
begin
	select into v_userId id from users
		where username = p_userName and password = p_userPass and email = p_userEmail;

		if v_userId isnull then
			insert into users(username, password, email)
				values (p_userName, p_userPass, p_userEmail);
			return 'OK';
		else
			update users
				set username = p_userName, password = p_userPass, email = p_userEmail
					where userId = v_userId;
				return 'OK';
		end if;
	end;
$$
	language 'plpgsql';
--

--getUser
create or replace function get_user(in int, out int, out text, out text)
	returns setof record as
$$
	select id, username, email from users
		where id = $1 and deleted = False;
$$
	language 'sql';
--

--getUserFromName
create or replace function get_userName(in text, out int, out text, out text)
	returns setof record as
$$
	select id, username, email from users
		where username = $1 and deleted = False;
$$
	language 'sql';
--

--getPass
create or replace function get_pass(in text, out text)
	returns text as
$$
	select password from users
		where username = $1 and deleted = False;
$$
	language 'sql';

--deleteUser
create or replace function delete_user(p_userId int)
	returns text as
	$$
	begin
	update users
		set deleted = True
		where id = p_userId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--


--addLog
create or replace function add_log(p_logFoo text, p_fooVal text, p_logDate text, p_logReturn text)
	returns text as
$$
declare
	v_logId int;
begin
	select into v_logId logId from logs
		where logFoo = p_logFoo and fooVal = p_fooVal and logDate = p_logDate and logReturn = p_logReturn;

		if v_logId isnull then
			insert into logs(logFoo, fooVal, logDate, logReturn)
				values (p_logFoo, p_fooVal, p_logDate, p_logReturn);
			return 'OK';
		else
			update logs
				set logFoo = p_logFoo, fooVal = p_fooVal, logDate = p_logDate, logReturn = p_logReturn
					where logId = v_logId;
				return 'OK';
		end if;
	end;
$$
	language 'plpgsql';
--

--getLog
create or replace function get_log(in int, out int, out text, out text, out text, out text)
	returns setof record as
$$
	select logId, logFoo, fooVal, logDate, logReturn from logs
		where logId = $1 and deleted = False;
$$
	language 'sql';
--

--deleteLog
create or replace function delete_log(p_logId int)
	returns text as
	$$
	begin
	update logs
		set deleted = True
		where logId = p_logId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--
--Post Board
--Tables
drop table if exists posts;
create table posts(
	postId serial primary key,
	username text,
	post text,
	postDate text,
	deleted boolean default False
);

drop table if exists logs;
create table logs(
  logId serial primary key,
  logFoo text,
  fooVal text,
  logDate text,
  logReturn text,
  deleted boolean default False
);

--Stored Procs
--addPost
create or replace function add_post(p_username text, p_post text, p_postDate text)
	returns text as
$$
declare
	v_postId int;
begin
	select into v_postId postId from posts
		where username = p_username and post = p_post and postDate = p_postDate;

		if v_postId isnull then
			insert into posts(username, post, postDate)
				values (p_username, p_post, p_postDate);
			return 'OK';
		else
			update posts
				set username = p_username, post = p_post, postDate = p_postDate
					where postId = v_postId;
				return 'OK';
		end if;
	end;
$$
	language 'plpgsql';
--

--getAllPost
create or replace function get_all_posts(out int, out text, out text, out text)
	returns setof record as
$$
	select postId, username, post, postDate from posts
		where deleted = False;
$$
	language 'sql';
--

--get_post_section
create or replace function get_post_section(in int, in int, out int, out text, out text, out text)
	returns setof record as
$$
	select postId, username, post, postDate from posts
		where postId >= $1 and postId <= ($1+$2) and deleted = False;
$$
	language 'sql';


--getPost
create or replace function get_post(in int, out int, out text, out text, out text)
	returns setof record as
$$
	select postId, username, post, postDate from posts
		where postId = $1 and deleted = False;
$$
	language 'sql';
--

--updatePost
create or replace function update_post(p_postId int, p_new_post text, p_postDate text)
	returns text as
	$$
	begin
	update posts
		set post = p_new_post
		and postDate = p_postDate
		where postId = p_postId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--

--deletePost
create or replace function delete_post(p_postId int)
	returns text as
	$$
	begin
	update posts
		set deleted = True
		where postId = p_postId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--

--addLog
create or replace function add_log(p_logFoo text, p_fooVal text, p_logDate text, p_logReturn text)
	returns text as
$$
declare
	v_logId int;
begin
	select into v_logId logId from logs
		where logFoo = p_logFoo and fooVal = p_fooVal and logDate = p_logDate and logReturn = p_logReturn;

		if v_logId isnull then
			insert into logs(logFoo, fooVal, logDate, logReturn)
				values (p_logFoo, p_fooVal, p_logDate, p_logReturn);
			return 'OK';
		else
			update logs
				set logFoo = p_logFoo, fooVal = p_fooVal, logDate = p_logDate, logReturn = p_logReturn
					where logId = v_logId;
				return 'OK';
		end if;
	end;
$$
	language 'plpgsql';
--

--getPost
create or replace function get_log(in int, out int, out text, out text, out text, out text)
	returns setof record as
$$
	select logId, logFoo, fooVal, logDate, logReturn from logs
		where logId = $1 and deleted = False;
$$
	language 'sql';
--

--deletePost
create or replace function delete_log(p_logId int)
	returns text as
	$$
	begin
	update logs
		set deleted = True
		where logId = p_logId;
		return 'OK';
		end;
	$$
		language 'plpgsql';
--
