SELECT name FROM names.names;

SET SQL_SAFE_UPDATES = 0;

delete from names.names;

insert into names.names
values(1, 'John Fu', NOW(), NOW()),
	  (2, 'Jane Doe', NOW(), NOW()),
      (3, 'Jake Peralta', NOW(), NOW());
      
update names.names
set name = 'Charles Boyle'
where id = 2;

select * from names;