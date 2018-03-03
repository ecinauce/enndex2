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

--getAllLog
create or replace function get_all_logs(out int, out text, out text, out text, out text)
	returns setof record as
$$
	select logId, logfoo, logval, logdate, logreturn from logs
		where deleted = False;
$$
	language 'sql';
--
