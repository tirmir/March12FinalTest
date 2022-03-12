select
	"Department",
	"Employee",
	"Salary"
from
(	
	select 
		employee.name as "Employee",
		salary as "Salary",
		department.name as "Department",
		dense_rank() over(partition by department.id order by salary desc) as rws
	from employee 
	left join department 
	on departmentId = department.id
) as  ranks
where rws<4;

