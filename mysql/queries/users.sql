insert into users
values (1, 'John', 'Fu', 'fohnju@gmail.com', NOW(), NOW()),
	   (2, 'Amy', 'Santiago', 'amysanti@gmail.com', NOW(), NOW()),
       (3, 'Ray', 'Holt', 'captainholt@yahoo.com', NOW(), NOW())
;
       
select * from users
;

select *
from users
where email = 'fohnju@gmail.com'
;

select *
from users
where id = 3
;

update users
set last_name = 'Pancakes'
where id = 3
;

delete from users
where id = 2
;

select *
from users
order by first_name
;

-- first name descending order
select *
from users
order by first_name desc
;

