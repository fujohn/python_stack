insert into dojos
values (1, 'Seattle', NOW(), NOW()),
	   (2, 'San Jose', NOW(), NOW()),
	   (3, 'Los Angeles', NOW(), NOW());
       
delete from dojos;

insert into dojos
values (1, 'Austin', NOW(), NOW()),
	   (2, 'Chicago', NOW(), NOW()),
	   (3, 'New York', NOW(), NOW());
       
insert into ninjas
values (1, 'John', 'Fu', 26, 1, NOW(), NOW()),
	   (2, 'Jake', 'Peralta', 35, 1, NOW(), NOW()),
	   (3, 'Amy', 'Santiago', 29, 1, NOW(), NOW()),
	   (4, 'Rosa', 'Diaz', 32, 2, NOW(), NOW()),
	   (5, 'Raymond', 'Holt', 54, 2, NOW(), NOW()),
	   (6, 'Terry', 'Jeffords', 43, 2, NOW(), NOW()),
	   (7, 'Charles', 'Boyle', 38, 3, NOW(), NOW()),
	   (8, 'Gina', 'Linetti', 35, 3, NOW(), NOW()),
	   (9, 'Norman', 'Scully', 53, 3, NOW(), NOW())
;
       
SELECT *
FROM ninjas AS n
LEFT JOIN dojos AS d
	ON n.dojo_id = d.id
WHERE n.dojo_id = 1
;
       
SELECT *
FROM ninjas AS n
LEFT JOIN dojos AS d
	ON n.dojo_id = d.id
WHERE n.dojo_id = 3
;
       
select id, name
from dojos
where id = (select dojo_id 
			from ninjas 
            order by id desc
            limit 1)
;
