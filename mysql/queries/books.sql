INSERT INTO books_schema.users
VALUES (1, 'Jane Amsden', NOW(), NOW()),
	   (2, 'Emily Dixon', NOW(), NOW()),
       (3, 'Theodore Dostoevsky', NOW(), NOW()),
       (4, 'William Shapiro', NOW(), NOW()),
       (5, 'Lao Xiu', NOW(), NOW())
;

insert into books_schema.books (id, title)
values (1, 'C Sharp'),
	   (2, 'Java'),
	   (3, 'Python'),
	   (4, 'PHP'),
	   (5, 'Ruby')
;

update books
set title = 'C#'
where id = 1
;

update users
set name = 'Bill Shapiro'
where id = 4
;

insert into favorites
values (1, 1, 1),
       (2, 1, 2),
       (3,2,1),
       (4,2,2),
       (5,2,3),
       (6, 3, 1),
       (7,3,2),
       (8,3,3),
       (9,3,4),
       (10,4,1),
       (11, 4, 2),
       (12,4,3),
       (13,4,4),
       (14,4,5)
;

select *
from users u
left join favorites f
on u.id = f.user_id
where book_id = 3
;

-- check for the first person who favorited 3
select min(id)
from favorites
where book_id = 3;

delete from favorites
where id = 5
;

select max(id)
from favorites;

insert into favorites (user_id, book_id)
value (5,2);

select b.title
from users u
join favorites f
on u.id = f.user_id
join books b
on f.book_id = b.id
where u.id = 3;

select u.*
from users u
left join favorites f
on u.id = f.user_id
where f.book_id = 5;