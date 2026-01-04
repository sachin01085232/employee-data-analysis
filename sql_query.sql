		SELECT * FROM public.newemp
		
		--- Dept-wise avg salary
		
		Select dept_id,
		avg(salary) as avg_salary
		from newemp
		group by dept_id
		
		--Top earners per department
		
		select *
from
(select *,
 DENSE_RANK()OVER(PARTITION  BY dept_id order by salary desc) as Rank
from newemp
) X

where rank <=3

		--Employees without department
		SELECT *
FROM employees
WHERE dept_id IS NULL
   OR dept_id = 'Unknown';

		
		--Salary vs company average
		SELECT
			emp_name,
			salary,
			AVG(salary) OVER () AS company_avg_salary,
			salary - AVG(salary) OVER () AS diff_from_avg
		FROM
			employees;
		
		--Join employees + departments
		SELECT e.emp_id,
       e.emp_name,
       e.salary,
       d.dept_name
FROM newemp e
LEFT JOIN department d
ON e.dept_id = d.dept_id;

		
