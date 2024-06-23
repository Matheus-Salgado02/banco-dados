-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/06/2024 às 01:27
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `adotaarvore`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `arvore`
--

CREATE TABLE `arvore` (
  `id` int(10) UNSIGNED NOT NULL,
  `cord_latitude` float NOT NULL,
  `cord_longitude` float NOT NULL,
  `id_especie` int(10) UNSIGNED NOT NULL,
  `id_locais` int(10) UNSIGNED NOT NULL,
  `id_cliente` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `bioma`
--

CREATE TABLE `bioma` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `descricao` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `bioma_especie`
--

CREATE TABLE `bioma_especie` (
  `id_especie` int(10) UNSIGNED NOT NULL,
  `id_bioma` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `cidade` varchar(40) NOT NULL,
  `bairro` varchar(40) NOT NULL,
  `rua` varchar(40) NOT NULL,
  `numero` int(10) UNSIGNED NOT NULL,
  `complemento` varchar(40) NOT NULL,
  `id_UF` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `especie`
--

CREATE TABLE `especie` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `descricao` varchar(45) NOT NULL,
  `espectativa_vida` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcinario`
--

CREATE TABLE `funcinario` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `cidade` varchar(40) NOT NULL,
  `bairro` varchar(40) NOT NULL,
  `rua` varchar(40) NOT NULL,
  `numero` int(10) UNSIGNED NOT NULL,
  `complemento` varchar(40) NOT NULL,
  `data_nascimento` date NOT NULL,
  `id_UF` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `locais`
--

CREATE TABLE `locais` (
  `id` int(10) UNSIGNED NOT NULL,
  `cidade` varchar(40) NOT NULL,
  `bairro` varchar(40) NOT NULL,
  `rua` varchar(40) NOT NULL,
  `numero` int(10) UNSIGNED NOT NULL,
  `complemento` varchar(40) NOT NULL,
  `id_UF` int(10) UNSIGNED NOT NULL,
  `id_bioma` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `protocolo`
--

CREATE TABLE `protocolo` (
  `id` int(10) UNSIGNED NOT NULL,
  `data_criacao` date NOT NULL,
  `data_plantar` date NOT NULL,
  `deferido` bit(1) DEFAULT NULL,
  `id_arvore` int(10) UNSIGNED NOT NULL,
  `id_funcionario` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `uf`
--

CREATE TABLE `uf` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `sigla` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `arvore`
--
ALTER TABLE `arvore`
  ADD PRIMARY KEY (`id`),
  ADD KEY `arvore_especie` (`id_especie`),
  ADD KEY `arvore_locais` (`id_locais`),
  ADD KEY `arvore_cliente` (`id_cliente`);

--
-- Índices de tabela `bioma`
--
ALTER TABLE `bioma`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `bioma_especie`
--
ALTER TABLE `bioma_especie`
  ADD KEY `id_especie` (`id_especie`),
  ADD KEY `id_bioma` (`id_bioma`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD KEY `cliente_UF` (`id_UF`);

--
-- Índices de tabela `especie`
--
ALTER TABLE `especie`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `funcinario`
--
ALTER TABLE `funcinario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD KEY `funcinario_UF` (`id_UF`);

--
-- Índices de tabela `locais`
--
ALTER TABLE `locais`
  ADD PRIMARY KEY (`id`),
  ADD KEY `locais_UF` (`id_UF`),
  ADD KEY `locais_bioma` (`id_bioma`);

--
-- Índices de tabela `protocolo`
--
ALTER TABLE `protocolo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `protocolo_arvore` (`id_arvore`),
  ADD KEY `protocolo_funcionario` (`id_funcionario`);

--
-- Índices de tabela `uf`
--
ALTER TABLE `uf`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `arvore`
--
ALTER TABLE `arvore`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `bioma`
--
ALTER TABLE `bioma`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `especie`
--
ALTER TABLE `especie`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `funcinario`
--
ALTER TABLE `funcinario`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `locais`
--
ALTER TABLE `locais`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `protocolo`
--
ALTER TABLE `protocolo`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `uf`
--
ALTER TABLE `uf`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `arvore`
--
ALTER TABLE `arvore`
  ADD CONSTRAINT `arvore_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`),
  ADD CONSTRAINT `arvore_especie` FOREIGN KEY (`id_especie`) REFERENCES `especie` (`id`),
  ADD CONSTRAINT `arvore_locais` FOREIGN KEY (`id_locais`) REFERENCES `locais` (`id`);

--
-- Restrições para tabelas `bioma_especie`
--
ALTER TABLE `bioma_especie`
  ADD CONSTRAINT `id_bioma` FOREIGN KEY (`id_bioma`) REFERENCES `bioma` (`id`),
  ADD CONSTRAINT `id_especie` FOREIGN KEY (`id_especie`) REFERENCES `especie` (`id`);

--
-- Restrições para tabelas `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_UF` FOREIGN KEY (`id_UF`) REFERENCES `uf` (`id`);

--
-- Restrições para tabelas `funcinario`
--
ALTER TABLE `funcinario`
  ADD CONSTRAINT `funcinario_UF` FOREIGN KEY (`id_UF`) REFERENCES `uf` (`id`);

--
-- Restrições para tabelas `locais`
--
ALTER TABLE `locais`
  ADD CONSTRAINT `locais_UF` FOREIGN KEY (`id_UF`) REFERENCES `uf` (`id`),
  ADD CONSTRAINT `locais_bioma` FOREIGN KEY (`id_bioma`) REFERENCES `bioma` (`id`);

--
-- Restrições para tabelas `protocolo`
--
ALTER TABLE `protocolo`
  ADD CONSTRAINT `protocolo_arvore` FOREIGN KEY (`id_arvore`) REFERENCES `arvore` (`id`),
  ADD CONSTRAINT `protocolo_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcinario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
