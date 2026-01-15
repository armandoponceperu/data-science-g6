use db_g6
-- sub consultas
select avg(salario) from empleado;
-- quiero saber todos los empleados que estan con un salario mayor al promedio
select nombre,salario from empleado
where salario > (select avg(salario) from empleado);

select pais,count(*) as total,avg(salario) as salario_promedio
from empleado
group by pais;

select nombre,salario,(select avg(salario) from empleado) as salario_promedio,
salario - (select avg(salario) from empleado) as diferencia_salario_promedio
from empleado
where salario > (select avg(salario) from empleado);
