create database Tienda;
use Tienda;
create table clientes(
    id_clientes int(4) not null auto_increment primary key ,
    nombre      varchar(20)not null,
    num_cel     varchar(30) not null,
    correo_electronico varchar (30) not null,
    sexo        varchar(30) not null);

create table productos(
    id_producto int(4) not null auto_increment primary key,
    nombre      varchar(20) not null,
    existencia  varchar(10) not null,
    tipo        varchar(20) not null,
    precio      int(7) not null);

insert into clientes(nombre,num_cel,correo_electronico,sexo)values
('JoseLuis','7757423895','luis@luis','hombre'),
('Rogger','7752016038','rog@rog''hombre'),
('Jaziel','7751695314','jaz@jaz''hombre');

insert into productos (nombre,existencia,tipo,precio)values
('boing','11','Bebida','10'),
('sabritas','20','Botana','11'),
('atun','10','Latas','15');

show tables;

select * from clientes;
describe clientes;

select * from productos;
describe productos;

create user 'luis'@'localhost' IDENTIFIED BY 'luis.2019';
Grant ALL PRIVILEGES ON Tienda.* TO'luis'@'localhost';
FLUSH PRIVILEGES;