-- MySQL dump 10.13  Distrib 8.0.46, for Linux (x86_64)
--
-- Host: localhost    Database: dam1
-- ------------------------------------------------------
-- Server version	8.0.46-0ubuntu0.24.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `nombre` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `Identificador` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Identificador`),
  CONSTRAINT `chk_clientes_email` CHECK (regexp_like(`email`,_utf8mb4'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}$'))
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES ('Alejandro','García López','alejandro.garcia@example.com',1),('María','Martínez Sánchez','maria.martinez@example.com',2),('Carlos','Rodríguez Pérez','carlos.rodriguez@example.com',3),('Laura','Fernández Gómez','laura.fernandez@example.com',4),('David','López Martín','david.lopez@example.com',5),('Ana','Sánchez Ruiz','ana.sanchez@example.com',6),('Javier','Pérez Moreno','javier.perez@example.com',7),('Lucía','Gómez Muñoz','lucia.gomez@example.com',8),('Daniel','Martín Álvarez','daniel.martin@example.com',9),('Elena','Ruiz Romero','elena.ruiz@example.com',10),('Pablo','Hernández Navarro','pablo.hernandez@example.com',11),('Sara','Jiménez Torres','sara.jimenez@example.com',12),('Miguel','Díaz Domínguez','miguel.diaz@example.com',13),('Carmen','Moreno Vázquez','carmen.moreno@example.com',14),('Sergio','Muñoz Ramos','sergio.munoz@example.com',15),('Paula','Álvarez Gil','paula.alvarez@example.com',16),('Alberto','Romero Serrano','alberto.romero@example.com',17),('Marta','Alonso Molina','marta.alonso@example.com',18),('Rubén','Gutiérrez Castro','ruben.gutierrez@example.com',19),('Cristina','Navarro Ortiz','cristina.navarro@example.com',20),('Adrián','Torres Rubio','adrian.torres@example.com',21),('Isabel','Domínguez Sanz','isabel.dominguez@example.com',22),('Víctor','Vázquez Iglesias','victor.vazquez@example.com',23),('Natalia','Ramos Medina','natalia.ramos@example.com',24),('Álvaro','Gil Garrido','alvaro.gil@example.com',25),('Patricia','Serrano Cortés','patricia.serrano@example.com',26),('Raúl','Molina Castillo','raul.molina@example.com',27),('Silvia','Castro Santos','silvia.castro@example.com',28),('Óscar','Ortiz Guerrero','oscar.ortiz@example.com',29),('Beatriz','Rubio Lozano','beatriz.rubio@example.com',30),('Iván','Sanz Cano','ivan.sanz@example.com',31),('Rocío','Iglesias Prieto','rocio.iglesias@example.com',32),('Héctor','Medina Méndez','hector.medina@example.com',33),('Noelia','Garrido Cruz','noelia.garrido@example.com',34),('Guillermo','Cortés Calvo','guillermo.cortes@example.com',35),('Andrea','Castillo Gallego','andrea.castillo@example.com',36),('Marcos','Santos Vidal','marcos.santos@example.com',37),('Alicia','Guerrero León','alicia.guerrero@example.com',38),('Fernando','Lozano Márquez','fernando.lozano@example.com',39),('Irene','Cano Peña','irene.cano@example.com',40),('Roberto','Prieto Cabrera','roberto.prieto@example.com',41),('Eva','Méndez Flores','eva.mendez@example.com',42),('Jorge','Cruz Campos','jorge.cruz@example.com',43),('Claudia','Calvo Nieto','claudia.calvo@example.com',44),('Manuel','Gallego Reyes','manuel.gallego@example.com',45),('Nuria','Vidal Pascual','nuria.vidal@example.com',46),('Antonio','León Herrero','antonio.leon@example.com',47),('Sofía','Márquez Montero','sofia.marquez@example.com',48),('Diego','Peña Hidalgo','diego.pena@example.com',49),('Teresa','Cabrera Lorenzo','teresa.cabrera@example.com',50);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `fecha` date DEFAULT NULL,
  `numerodepedido` int DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  `producto_id` int DEFAULT NULL,
  `Identificador` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES ('2026-01-05',1001,3,12,1),('2026-01-08',1002,7,4,2),('2026-01-12',1003,15,23,3),('2026-01-15',1004,2,8,4),('2026-01-20',1005,21,17,5),('2026-01-25',1006,9,31,6),('2026-02-02',1007,14,5,7),('2026-02-06',1008,4,42,8),('2026-02-10',1009,28,19,9),('2026-02-14',1010,11,7,10),('2026-02-18',1011,3,26,11),('2026-02-22',1012,35,13,12),('2026-03-01',1013,18,45,13),('2026-03-05',1014,6,22,14),('2026-03-09',1015,24,3,15),('2026-03-14',1016,41,38,16),('2026-03-18',1017,12,16,17),('2026-03-22',1018,7,29,18),('2026-03-27',1019,30,10,19),('2026-04-01',1020,16,48,20),('2026-04-05',1021,5,2,21),('2026-04-10',1022,22,35,22),('2026-04-14',1023,39,14,23),('2026-04-19',1024,10,41,24),('2026-04-24',1025,27,6,25),('2026-04-28',1026,1,33,26),('2026-05-03',1027,19,21,27),('2026-05-08',1028,33,9,28),('2026-05-12',1029,8,50,29),('2026-05-17',1030,44,27,30),('2026-05-21',1031,13,18,31),('2026-05-26',1032,25,39,32),('2026-06-01',1033,3,11,33),('2026-06-06',1034,37,24,34),('2026-06-11',1035,20,46,35),('2026-06-16',1036,7,1,36),('2026-06-21',1037,46,32,37),('2026-06-26',1038,17,20,38),('2026-07-02',1039,29,43,39),('2026-07-07',1040,5,15,40),('2026-07-12',1041,40,28,41),('2026-07-17',1042,23,37,42),('2026-07-22',1043,32,25,43),('2026-07-27',1044,14,49,44),('2026-08-02',1045,48,34,45),('2026-08-08',1046,2,44,46),('2026-08-14',1047,31,30,47),('2026-08-20',1048,9,47,48),('2026-09-01',1049,36,36,49),('2026-09-15',1050,7,12,50);
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `nombre` varchar(100) DEFAULT NULL,
  `precio` decimal(8,2) DEFAULT NULL,
  `Identificador` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES ('Ordenador portátil',899.99,1),('Monitor 24 pulgadas',159.90,2),('Teclado mecánico',79.95,3),('Ratón inalámbrico',34.50,4),('Auriculares Bluetooth',59.99,5),('Disco SSD 1TB',89.90,6),('Memoria USB 64GB',12.95,7),('Webcam Full HD',44.99,8),('Micrófono USB',69.50,9),('Altavoces 2.1',49.90,10),('Impresora láser',189.00,11),('Router WiFi 6',119.95,12),('Switch Ethernet 8 puertos',39.99,13),('Cable HDMI 2 metros',9.95,14),('Cable USB-C',8.50,15),('Cargador USB-C 65W',29.99,16),('Batería externa 20000mAh',39.95,17),('Soporte para portátil',24.90,18),('Alfombrilla para ratón',14.50,19),('Hub USB-C',42.99,20),('Tarjeta gráfica',499.90,21),('Procesador',289.99,22),('Placa base',179.95,23),('Memoria RAM 16GB',64.90,24),('Fuente de alimentación 750W',89.99,25),('Caja ATX',74.50,26),('Ventilador CPU',39.90,27),('Disco duro 2TB',69.95,28),('Adaptador WiFi USB',19.99,29),('Adaptador Bluetooth USB',14.95,30),('Tablet 10 pulgadas',249.90,31),('Smartphone',399.99,32),('Reloj inteligente',129.95,33),('Lector de tarjetas',11.50,34),('Proyector Full HD',449.00,35),('Pantalla de proyección',99.90,36),('Silla de oficina',179.99,37),('Mesa de escritorio',149.95,38),('Lámpara LED escritorio',32.50,39),('Regleta 6 enchufes',18.90,40),('SAI 900VA',109.99,41),('Servidor NAS',349.90,42),('Disco NAS 4TB',119.95,43),('Cámara IP',59.90,44),('Punto de acceso WiFi',84.99,45),('Adaptador USB Ethernet',21.50,46),('Docking station USB-C',139.90,47),('Monitor 27 pulgadas',249.99,48),('Teclado inalámbrico',44.95,49),('Ratón gaming',54.90,50);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vista_completa`
--

DROP TABLE IF EXISTS `vista_completa`;
/*!50001 DROP VIEW IF EXISTS `vista_completa`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_completa` AS SELECT 
 1 AS `fecha del pedido`,
 1 AS `numero de pedido`,
 1 AS `nombre del cliente`,
 1 AS `apellidos del cliente`,
 1 AS `nombre del producto`,
 1 AS `precio del producto`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vista_completa`
--

/*!50001 DROP VIEW IF EXISTS `vista_completa`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_completa` AS select `pedidos`.`fecha` AS `fecha del pedido`,`pedidos`.`numerodepedido` AS `numero de pedido`,`clientes`.`nombre` AS `nombre del cliente`,`clientes`.`apellidos` AS `apellidos del cliente`,`productos`.`nombre` AS `nombre del producto`,`productos`.`precio` AS `precio del producto` from ((`pedidos` left join `clientes` on((`pedidos`.`cliente_id` = `clientes`.`Identificador`))) left join `productos` on((`pedidos`.`producto_id` = `productos`.`Identificador`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-25 12:06:19
