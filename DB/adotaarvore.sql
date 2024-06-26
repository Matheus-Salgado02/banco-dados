-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26/06/2024 às 07:11
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

--
-- Despejando dados para a tabela `arvore`
--

INSERT INTO `arvore` (`id`, `cord_latitude`, `cord_longitude`, `id_especie`, `id_locais`, `id_cliente`) VALUES
(1, -22.6161, -44.9708, 1, 1, 1),
(2, -23.5878, -46.6583, 2, 2, 2),
(3, -22.9614, -43.2719, 3, 3, 3),
(4, -25.4244, -49.263, 4, 4, 4),
(5, -25.6848, -54.4401, 5, 5, 5),
(6, -14.1703, -47.7837, 6, 6, 6),
(7, -10.9111, -46.7444, 7, 7, 7),
(8, -2.7264, -42.7982, 8, 8, 8),
(9, -23.3714, -44.8448, 9, 9, 9),
(10, -2.7959, -54.6186, 10, 10, 10);

-- --------------------------------------------------------

--
-- Estrutura para tabela `bioma`
--

CREATE TABLE `bioma` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `descricao` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `bioma`
--

INSERT INTO `bioma` (`id`, `nome`, `descricao`) VALUES
(1, 'Mata Atlântica', 'Bioma de floresta tropical que se estende ao longo da costa atlântica do Brasil.'),
(2, 'Cerrado', 'Bioma de savana tropical encontrado principalmente no Brasil central, caracterizado por suas árvores de pequeno porte e vegetação rasteira.'),
(3, 'Mata de Araucárias', 'Bioma de floresta temperada, predominante no sul do Brasil, onde se encontram principalmente araucárias.'),
(4, 'Amazônia', 'Bioma de floresta tropical, é a maior floresta do mundo, localizada na região norte do Brasil.'),
(5, 'Caatinga', 'Bioma semiárido localizado no Nordeste do Brasil, caracterizado por sua vegetação xerófila adaptada a longos períodos de seca.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `bioma_especie`
--

CREATE TABLE `bioma_especie` (
  `id_especie` int(10) UNSIGNED NOT NULL,
  `id_bioma` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `bioma_especie`
--

INSERT INTO `bioma_especie` (`id_especie`, `id_bioma`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(5, 2),
(10, 5),
(8, 4),
(9, 4),
(6, 2),
(7, 1);

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

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `cpf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `id_UF`) VALUES
(1, 'João Silva', '12345678901', 'São Paulo', 'Centro', 'Rua das Flores', 123, 'Apto 101', 25),
(2, 'Maria Oliveira', '98765432100', 'Rio de Janeiro', 'Jardim das Acácias', 'Avenida Brasil', 456, 'Casa 2', 19),
(3, 'Pedro Santos', '12312312312', 'Belo Horizonte', 'Bela Vista', 'Rua Minas Gerais', 789, 'Bloco B', 13),
(4, 'Ana Costa', '32132132132', 'Rio de Janeiro', 'Copacabana', 'Rua Atlântica', 101, 'Cobertura', 19),
(5, 'Carlos Pereira', '11122233344', 'São Paulo', 'Itaim Bibi', 'Avenida Brigadeiro Faria Lima', 456, 'Sala 305', 25),
(6, 'Mariana Souza', '44455566677', 'São Paulo', 'Jardins', 'Rua Haddock Lobo', 789, 'Apto 202', 25),
(7, 'Lucas Alves', '22233344455', 'Fortaleza', 'Meireles', 'Rua Silva Paulet', 321, 'Casa', 6),
(8, 'Fernanda Lima', '66677788899', 'Curitiba', 'Centro', 'Rua XV de Novembro', 654, 'Apto 808', 16),
(9, 'Rafael Duarte', '55566677788', 'Florianópolis', 'Centro', 'Avenida Beira Mar Norte', 987, 'Cobertura', 24),
(10, 'Patrícia Ribeiro', '99988877766', 'Brasília', 'Asa Sul', 'Rua W3 Sul', 123, 'Bloco G', 7);

-- --------------------------------------------------------

--
-- Estrutura para tabela `especie`
--

CREATE TABLE `especie` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `descricao` tinytext DEFAULT NULL,
  `expectativa_vida` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `especie`
--

INSERT INTO `especie` (`id`, `nome`, `descricao`, `expectativa_vida`) VALUES
(1, 'Carvalho-alvarinho', 'Comumente conhecida como carvalho-alvarinho, é uma árvore grande e caducifólia encontrada na Europa.', 400),
(2, 'Ipê-amarelo', 'Árvore símbolo do Brasil, é conhecida por suas flores amarelas vibrantes e é nativa do Cerrado.', 70),
(3, 'Pinheiro-do-paraná', 'Também conhecido como araucária, é uma árvore de folha perene nativa do sul do Brasil.', 200),
(4, 'Pau-brasil', 'Árvore que dá nome ao Brasil, é conhecida por sua madeira vermelha e é nativa da Mata Atlântica.', 300),
(5, 'Ipê-roxo', 'Árvore nativa do Cerrado, conhecida por suas flores roxas.', 80),
(6, 'Aroeira-vermelha', 'Árvore nativa do Brasil, encontrada principalmente na Mata Atlântica e no Cerrado.', 100),
(7, 'Jequitibá-rosa', 'Uma das maiores árvores da Mata Atlântica, conhecida por sua grande altura.', 500),
(8, 'Copaíba', 'Árvore nativa da Amazônia, conhecida por seu óleo medicinal.', 400),
(9, 'Castanheira-do-Brasil', 'Árvore nativa da Amazônia, famosa por suas castanhas.', 500),
(10, 'Cajueiro', 'Árvore nativa do Nordeste do Brasil, conhecida por seus frutos (caju).', 50);

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
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

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`id`, `nome`, `cpf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `data_nascimento`, `id_UF`) VALUES
(1, 'José Silva', '12345678901', 'São Paulo', 'Centro', 'Rua das Flores', 123, 'Apto 101', '1990-05-15', 25),
(2, 'Ana Oliveira', '98765432100', 'Rio de Janeiro', 'Jardim das Acácias', 'Avenida Brasil', 456, 'Casa 2', '1985-12-10', 19),
(3, 'Carlos Santos', '12312312312', 'Belo Horizonte', 'Bela Vista', 'Rua Minas Gerais', 789, 'Bloco B', '1988-08-25', 13),
(4, 'Maria Costa', '32132132132', 'Rio de Janeiro', 'Copacabana', 'Rua Atlântica', 101, 'Cobertura', '1992-04-30', 19),
(5, 'Paula Pereira', '11122233344', 'São Paulo', 'Itaim Bibi', 'Avenida Brigadeiro Faria Lima', 456, 'Sala 305', '1987-07-20', 25),
(6, 'Fernando Souza', '44455566677', 'São Paulo', 'Jardins', 'Rua Haddock Lobo', 789, 'Apto 202', '1995-01-05', 25),
(7, 'Luciana Alves', '22233344455', 'Fortaleza', 'Meireles', 'Rua Silva Paulet', 321, 'Casa', '1989-09-18', 6),
(8, 'Gabriel Lima', '66677788899', 'Curitiba', 'Centro', 'Rua XV de Novembro', 654, 'Apto 808', '1991-03-12', 16),
(9, 'Patrícia Duarte', '55566677788', 'Florianópolis', 'Centro', 'Avenida Beira Mar Norte', 987, 'Cobertura', '1993-11-08', 24),
(10, 'Mariana Ribeiro', '99988877766', 'Brasília', 'Asa Sul', 'Rua W3 Sul', 123, 'Bloco G', '1986-06-28', 7);

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
  `id_bioma` int(10) UNSIGNED NOT NULL,
  `nome` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `locais`
--

INSERT INTO `locais` (`id`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `id_UF`, `id_bioma`, `nome`) VALUES
(1, 'São Lourenço', 'Centro', 'Avenida das Fontes', 123, 'Entrada principal', 13, 3, 'Parque das Águas'),
(2, 'São Paulo', 'Ibirapuera', 'Avenida Pedro Álvares Cabral', 456, 'Portão 3', 25, 1, 'Parque do Ibirapuera'),
(3, 'Rio de Janeiro', 'Alto da Boa Vista', 'Estrada da Cascatinha', 789, 'Trilha da Cascatinha', 19, 1, 'Parque Nacional da Tijuca'),
(4, 'Curitiba', 'Jardim Botânico', 'Rua Engenheiro Ostoja Roguski', 101, 'Estufa principal', 16, 1, 'Jardim Botânico'),
(5, 'Foz do Iguaçu', 'Área Rural de Foz do Iguaçu', 'Rodovia BR-469', 456, 'Cataratas do Iguaçu', 16, 1, 'Parque Nacional do Iguaçu'),
(6, 'Alto Paraíso de Goiás', 'Vila de São Jorge', 'Estrada GO-239', 321, 'Trilha dos Saltos', 9, 2, 'Parque Nacional da Chapada dos Veadeiros'),
(7, 'Jalapão', 'Mateiros', 'TO-110', 654, 'Trilha das Dunas', 27, 5, 'Parque Estadual do Jalapão'),
(8, 'Lençóis Maranhenses', 'Barreirinhas', 'MA-315', 987, 'Lagoa Azul', 10, 4, 'Parque Nacional dos Lençóis Maranhenses'),
(9, 'Ubatuba', 'Picinguaba', 'Estrada do Corcovado', 123, 'Trilha do Pico Corcovado', 19, 1, 'Parque Estadual da Serra do Mar'),
(10, 'Itaituba', 'Itaituba', 'PA-370', 456, 'Rio Tapajós', 14, 4, 'Parque Nacional da Amazônia');

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

--
-- Despejando dados para a tabela `protocolo`
--

INSERT INTO `protocolo` (`id`, `data_criacao`, `data_plantar`, `deferido`, `id_arvore`, `id_funcionario`) VALUES
(1, '2024-06-25', '2024-07-10', b'1', 1, 1),
(2, '2024-06-25', '2024-07-12', b'1', 2, 2),
(3, '2024-06-25', '2024-07-15', b'0', 3, 3),
(4, '2024-06-25', '2024-07-20', b'1', 4, 2),
(5, '2024-06-25', '2024-07-25', b'0', 5, 2),
(6, '2024-06-25', '2024-08-01', b'1', 6, 6),
(7, '2024-06-25', '2024-08-05', b'1', 7, 7),
(8, '2024-06-25', '2024-08-10', b'0', 8, 5),
(9, '2024-06-25', '2024-08-15', b'1', 9, 9),
(10, '2024-06-25', '2024-08-20', b'0', 10, 10);

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
-- Despejando dados para a tabela `uf`
--

INSERT INTO `uf` (`id`, `nome`, `sigla`) VALUES
(1, 'Acre', 'AC'),
(2, 'Alagoas', 'AL'),
(3, 'Amapá', 'AP'),
(4, 'Amazonas', 'AM'),
(5, 'Bahia', 'BA'),
(6, 'Ceará', 'CE'),
(7, 'Distrito Federal', 'DF'),
(8, 'Espírito Santo', 'ES'),
(9, 'Goiás', 'GO'),
(10, 'Maranhão', 'MA'),
(11, 'Mato Grosso', 'MT'),
(12, 'Mato Grosso do Sul', 'MS'),
(13, 'Minas Gerais', 'MG'),
(14, 'Pará', 'PA'),
(15, 'Paraíba', 'PB'),
(16, 'Paraná', 'PR'),
(17, 'Pernambuco', 'PE'),
(18, 'Piauí', 'PI'),
(19, 'Rio de Janeiro', 'RJ'),
(20, 'Rio Grande do Norte', 'RN'),
(21, 'Rio Grande do Sul', 'RS'),
(22, 'Rondônia', 'RO'),
(23, 'Roraima', 'RR'),
(24, 'Santa Catarina', 'SC'),
(25, 'São Paulo', 'SP'),
(26, 'Sergipe', 'SE'),
(27, 'Tocantins', 'TO');

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
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
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
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `bioma`
--
ALTER TABLE `bioma`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `especie`
--
ALTER TABLE `especie`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `locais`
--
ALTER TABLE `locais`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `protocolo`
--
ALTER TABLE `protocolo`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `uf`
--
ALTER TABLE `uf`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

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
-- Restrições para tabelas `funcionario`
--
ALTER TABLE `funcionario`
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
  ADD CONSTRAINT `protocolo_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
