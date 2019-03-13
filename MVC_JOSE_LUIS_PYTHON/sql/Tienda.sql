create database Tienda;                 //creacion de la base de datos 

use Tienda;
create table clientes(                                      //creacion de la tabla clientes 
    id_clientes int(4) not null auto_increment primary key , //definicion de la primary key 
    nombre      varchar(20)not null,
    num_cel     varchar(30) not null,
    correo_electronico varchar (30) not null,
    sexo        varchar(30) not null);

create table productos(                                      // creacion de la tabla productos
    id_producto int(4) not null auto_increment primary key,
    nombre      varchar(20) not null,
    existencia  varchar(10) not null,
    tipo        varchar(20) not null,
    precio      int(7) not null);

insert into clientes(nombre,num_cel,correo_electronico,sexo)values  //insercion de datos a la tabla clientes
('JoseLuis','7757423895','luis@luis','hombre'),
('Rogger','7752016038','rog@rog''hombre'),
('Jaziel','7751695314','jaz@jaz''hombre');

insert into productos (nombre,existencia,tipo,precio)values  // insercion de datos a la tabla productos
('boing','11','Bebida','10'),
('sabritas','20','Botana','11'),
('atun','10','Latas','15');

show tables;

select * from clientes;                     //consulta de datos de la tabla clientes 
describe clientes;                          //muestra la tabla y sus tipod de dato 

select * from productos;                     //consulta de datos de la tabla productos
describe productos;                          //muestra la tabla y sus tipos de datos 

create user 'luis'@'localhost' IDENTIFIED BY 'luis.2019';  // creacion de un usuario y contraseña
Grant ALL PRIVILEGES ON Tienda.* TO'luis'@'localhost';      //otorgacion de privilegios al usuario 
FLUSH PRIVILEGES;