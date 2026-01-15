--FILTROS
select * from empleado where pais ='peru';
select * from empleado where salario > 5000;
select * from empleado where salario > 5000 and pais = 'peru';
select * from empleado
where salario > 5000
and (pais = 'peru' or pais = 'colombia');
select * from empleado
where pais in ('Chile','Argentina');
select * from empleado
where salario between 10000 and 15000;
