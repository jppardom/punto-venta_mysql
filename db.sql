-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-07-2026 a las 02:47:37
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `punto_venta`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `cedula` varchar(10) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `genero` enum('Masculino','Femenino') NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `correo` varchar(250) NOT NULL,
  `direccion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `cedula`, `nombres`, `apellidos`, `genero`, `telefono`, `correo`, `direccion`) VALUES
(1, '1111111111', 'Juan pablo', 'Pardo Montero', 'Masculino', '0999999999', 'juan@gmail.com', 'Cariamanga'),
(3, '2222222222', 'María Jose', 'Rodríguez Álvarez', 'Femenino', '0999999999', 'maria@gmail.com', 'Loja'),
(4, '3333333333', 'Jessica María', 'Pérez Perez', 'Femenino', '999999999', 'jessica@hotmail.com', 'Quito'),
(5, '4444444444', 'Carlos José', 'Pérez Jiménez', 'Masculino', '9999999', 'carlos@ejemplo.com', 'Quito'),
(6, '555555555', 'Paola', 'Castro', 'Femenino', '099999999', 'paola@ejemplo.com', 'Guayaquil');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `stock` int(10) NOT NULL,
  `precio` decimal(3,2) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `stock`, `precio`, `descripcion`) VALUES
(1, 'Cable UTP Cat6', 150, 0.85, 'Cable de red por metro, ideal para LAN'),
(2, 'Conector RJ45 CAT6', 500, 0.25, 'Plug de red RJ45 con baño de oro'),
(3, 'Capucha RJ45', 300, 0.15, 'Protector de goma para conectores de red'),
(4, 'Acoplador RJ45', 80, 1.50, 'Unión hembra-hembra para extender cables');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `cedula` varchar(10) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `correo` varchar(250) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `cedula`, `nombres`, `apellidos`, `direccion`, `correo`, `usuario`, `password`) VALUES
(1, '1111111111', 'Juan', 'Pablo', 'Cariamanga', 'abc@gmail.com', 'admin', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(3, '2222222222', 'Pablo', 'Montero', 'Loja', 'cdb@gmail.com', 'pablo', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(4, '3333333333', 'María', 'Cevallos', 'Quito', 'maria@gmail.com', 'maria', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(5, '4444444444', 'José', 'Pérez', 'Guayaquil', 'jose@gmail.com', 'jose', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(6, '5555555555', 'Carmen', 'Maza', 'Loja', 'carme@gmail.com', 'carmen', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220'),
(7, '6666666666', 'Jorge', 'Maza', 'Quito', 'jorge@gmail.com', 'jorge', 'f7c3bc1d808e04732adf679965ccc34ca7ae3441'),
(8, '7777777777', 'Andés', 'Acaro', 'Cariamanga', 'andres@gmail.com', 'andres', '7aaa2e2aef0d8ce64bf8ee2b14854423cd138da9');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
