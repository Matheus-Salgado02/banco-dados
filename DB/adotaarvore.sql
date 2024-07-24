-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/07/2024 às 14:23
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
(10, -2.7959, -54.6186, 10, 10, 10),
(15, 120, 210, 8, 10, 3),
(16, 111, 222, 8, 10, 5),
(17, 222, 111, 8, 10, 5),
(18, 2121, 1231, 8, 10, 6),
(19, 123, 321, 8, 10, 5),
(20, 123, 321, 8, 10, 5),
(21, 978, 78, 8, 10, 6),
(22, 3216, 456456, 8, 10, 7),
(23, 436.45, 456456, 8, 10, 5),
(24, 123, 312, 8, 10, 6),
(25, 45, 45, 8, 10, 5),
(26, 54, 64, 8, 10, 6),
(27, 21, 31, 8, 10, 5),
(28, 54, 45, 8, 10, 6),
(29, 4, 4, 8, 10, 5),
(30, 4, 4, 8, 10, 5),
(31, 5, 5, 8, 10, 7),
(32, 6, 5, 8, 10, 5),
(33, 55, 55, 8, 10, 5);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `arvoreinformacao`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `arvoreinformacao` (
`id` int(10) unsigned
,`cord_latitude` float
,`cord_longitude` float
,`id_especie` int(10) unsigned
,`nome_especie` varchar(40)
,`id_locais` int(10) unsigned
,`Estado` varchar(2)
,`nome_local` varchar(45)
,`tipo_plantio` varchar(45)
,`id_cliente` int(10) unsigned
,`nome_cliente` varchar(40)
,`cli_tel` varchar(13)
,`cli_email` varchar(256)
);

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
-- Estrutura para tabela `car`
--

CREATE TABLE `car` (
  `id` int(10) UNSIGNED NOT NULL,
  `reserva_legal` int(10) UNSIGNED NOT NULL,
  `apps` int(10) UNSIGNED NOT NULL,
  `uso_terra` tinytext NOT NULL,
  `id_locais` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `car`
--

INSERT INTO `car` (`id`, `reserva_legal`, `apps`, `uso_terra`, `id_locais`) VALUES
(1, 15, 10, 'Pastagem', 1),
(2, 26, 15, 'Cultivo', 2),
(3, 18, 8, 'Silvicultura', 3),
(4, 23, 12, 'Agricultura', 4),
(5, 20, 9, 'Pastagem', 5),
(6, 21, 11, 'Cultivo', 6),
(7, 24, 14, 'Silvicultura', 7),
(8, 24, 13, 'Agricultura', 8),
(9, 18, 7, 'Pastagem', 9),
(10, 26, 16, 'Cultivo', 10);

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
  `id_UF` int(10) UNSIGNED NOT NULL,
  `telefone` varchar(13) NOT NULL,
  `email` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `cpf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `id_UF`, `telefone`, `email`) VALUES
(1, 'João Silva', '12345678901', 'São Paulo', 'Centro', 'Rua das Flores', 111, 'Apto 101', 25, '981234567', 'maria.silva@gmail.com'),
(2, 'Maria Oliveira', '98765432100', 'Rio de Janeiro', 'Jardim das Acácias', 'Avenida Brasil', 222, 'Casa 2', 19, '992345678', 'joao.pereira@hotmail.com'),
(3, 'Pedro Santos', '12312312312', 'Belo Horizonte', 'Bela Vista', 'Rua Minas Gerais', 333, 'Bloco B', 13, '973456789', 'ana.souza@outlook.com'),
(4, 'Ana Costa', '32132132132', 'Rio de Janeiro', 'Copacabana', 'Rua Atlântica', 444, 'Cobertura', 19, '984567890', 'carlos.lima@gmail.com'),
(5, 'Carlos Pereira', '11122233344', 'São Paulo', 'Itaim Bibi', 'Avenida Brigadeiro Faria Lima', 555, 'Sala 305', 25, '995678901', 'fernanda.rodrigues@hotmail.com'),
(6, 'Mariana Souza', '44455566677', 'São Paulo', 'Jardins', 'Rua Haddock Lobo', 666, 'Apto 202', 25, '976789012', 'paulo.almeida@outlook.com'),
(7, 'Lucas Alves', '22233344455', 'Fortaleza', 'Meireles', 'Rua Silva Paulet', 777, 'Casa', 6, '987890123', 'juliana.martins@gmail.com'),
(8, 'Fernanda Lima', '66677788899', 'Curitiba', 'Centro', 'Rua XV de Novembro', 888, 'Apto 808', 16, '998901234', 'roberto.gomes@hotmail.com'),
(9, 'Rafael Duarte', '55566677788', 'Florianópolis', 'Centro', 'Avenida Beira Mar Norte', 999, 'Cobertura', 24, '969012345', 'patricia.oliveira@outlook.com'),
(10, 'Patrícia Ribeiro', '99988877766', 'Brasília', 'Asa Sul', 'Rua W3 Sul', 101010, 'Bloco G', 7, '979123456', 'ricardo.ferreira@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `especie`
--

CREATE TABLE `especie` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(40) NOT NULL,
  `descricao` tinytext DEFAULT NULL,
  `expectativa_vida` int(11) DEFAULT NULL,
  `nome_cientifico` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `especie`
--

INSERT INTO `especie` (`id`, `nome`, `descricao`, `expectativa_vida`, `nome_cientifico`) VALUES
(1, 'Carvalho-alvarinho', 'Comumente conhecida como carvalho-alvarinho, é uma árvore grande e caducifólia encontrada na Europa.', 400, 'Quercus robur'),
(2, 'Ipê-amarelo', 'Árvore símbolo do Brasil, é conhecida por suas flores amarelas vibrantes e é nativa do Cerrado.', 70, 'Handroanthus albus'),
(3, 'Pinheiro-do-paraná', 'Também conhecido como araucária, é uma árvore de folha perene nativa do sul do Brasil.', 200, 'Araucaria angustifolia'),
(4, 'Pau-brasil', 'Árvore que dá nome ao Brasil, é conhecida por sua madeira vermelha e é nativa da Mata Atlântica.', 300, 'Paubrasilia echinata'),
(5, 'Ipê-roxo', 'Árvore nativa do Cerrado, conhecida por suas flores roxas.', 80, 'Handroanthus impetiginosus'),
(6, 'Aroeira-vermelha', 'Árvore nativa do Brasil, encontrada principalmente na Mata Atlântica e no Cerrado.', 100, 'Schinus terebinthifolius'),
(7, 'Jequitibá-rosa', 'Uma das maiores árvores da Mata Atlântica, conhecida por sua grande altura.', 500, 'Cariniana legalis'),
(8, 'Copaíba', 'Árvore nativa da Amazônia, conhecida por seu óleo medicinal.', 400, 'Copaifera langsdorffii'),
(9, 'Castanheira-do-Brasil', 'Árvore nativa da Amazônia, famosa por suas castanhas.', 500, 'Bertholletia excelsa'),
(10, 'Cajueiro', 'Árvore nativa do Nordeste do Brasil, conhecida por seus frutos (caju).', 50, 'Anacardium occidentale');

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
  `nome` varchar(45) NOT NULL,
  `descricao` tinytext NOT NULL,
  `croqui` tinytext NOT NULL,
  `tipo_plantio` varchar(45) NOT NULL,
  `area_total` float UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `locais`
--

INSERT INTO `locais` (`id`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `id_UF`, `id_bioma`, `nome`, `descricao`, `croqui`, `tipo_plantio`, `area_total`) VALUES
(1, 'São Lourenço', 'Centro', 'Avenida das Fontes', 123, 'Entrada principal', 13, 3, 'Parque das Águas', 'Plantio de espécies nativas em monocultura.', 'croqui1.png', 'Monocultura', 100.5),
(2, 'São Paulo', 'Ibirapuera', 'Avenida Pedro Álvares Cabral', 456, 'Portão 3', 25, 1, 'Parque do Ibirapuera', 'Plantio em sistema agroflorestal com diversidade de culturas.', 'croqui2.png', 'Sistema Agroflorestal', 200.75),
(3, 'Rio de Janeiro', 'Alto da Boa Vista', 'Estrada da Cascatinha', 789, 'Trilha da Cascatinha', 19, 1, 'Parque Nacional da Tijuca', 'Plantio de árvores frutíferas em monocultura.', 'croqui3.png', 'Monocultura', 150),
(4, 'Curitiba', 'Jardim Botânico', 'Rua Engenheiro Ostoja Roguski', 101, 'Estufa principal', 16, 1, 'Jardim Botânico', 'Sistema agroflorestal com árvores e culturas agrícolas.', 'croqui4.png', 'Sistema Agroflorestal', 175.25),
(5, 'Foz do Iguaçu', 'Área Rural de Foz do Iguaçu', 'Rodovia BR-469', 456, 'Cataratas do Iguaçu', 16, 1, 'Parque Nacional do Iguaçu', 'Monocultura de eucaliptos.', 'croqui5.png', 'Monocultura', 125.5),
(6, 'Alto Paraíso de Goiás', 'Vila de São Jorge', 'Estrada GO-239', 321, 'Trilha dos Saltos', 9, 2, 'Parque Nacional da Chapada dos Veadeiros', 'Área de reflorestamento com espécies nativas.', 'croqui6.png', 'Sistema Agroflorestal', 220.3),
(7, 'Jalapão', 'Mateiros', 'TO-110', 654, 'Trilha das Dunas', 27, 5, 'Parque Estadual do Jalapão', 'Sistema agroflorestal integrado com pastagem.', 'croqui7.png', 'Monocultura', 190.75),
(8, 'Lençóis Maranhenses', 'Barreirinhas', 'MA-315', 987, 'Lagoa Azul', 10, 4, 'Parque Nacional dos Lençóis Maranhenses', 'Plantio experimental de novas espécies.', 'croqui8.png', 'Sistema Agroflorestal', 210.4),
(9, 'Ubatuba', 'Picinguaba', 'Estrada do Corcovado', 123, 'Trilha do Pico Corcovado', 19, 1, 'Parque Estadual da Serra do Mar', 'Área de conservação ambiental.', 'croqui9.png', 'Monocultura', 130.6),
(10, 'Itaituba', 'Itaituba', 'PA-370', 456, 'Rio Tapajós', 14, 4, 'Parque Nacional da Amazônia', 'Produção sustentável em sistema agroflorestal.', 'croqui10.png', 'Sistema Agroflorestal', 205.85);

-- --------------------------------------------------------

--
-- Estrutura para tabela `protocolo`
--

CREATE TABLE `protocolo` (
  `id` int(10) UNSIGNED NOT NULL,
  `data_criacao` date NOT NULL,
  `data_plantar` date DEFAULT NULL,
  `deferido` varchar(1) NOT NULL,
  `id_arvore` int(10) UNSIGNED NOT NULL,
  `id_funcionario` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `protocolo`
--

INSERT INTO `protocolo` (`id`, `data_criacao`, `data_plantar`, `deferido`, `id_arvore`, `id_funcionario`) VALUES
(1, '0000-00-00', '0000-00-00', '0', 1, 1),
(2, '2024-06-25', '2024-07-12', '1', 2, 2),
(3, '2024-06-25', '0000-00-00', '0', 3, 3),
(4, '0000-00-00', '0000-00-00', '0', 4, 2),
(5, '2024-06-25', '2024-07-25', '1', 5, 2),
(6, '2024-06-25', '2024-08-01', '1', 6, 6),
(7, '2024-06-25', '2024-08-05', '1', 7, 7),
(8, '2024-06-25', '2024-08-10', '1', 8, 5),
(9, '2024-06-25', '2024-08-15', '1', 9, 9),
(10, '2024-06-25', '2024-09-22', '1', 10, 7),
(20, '2024-07-16', '0000-00-00', '0', 27, 1),
(21, '2024-07-16', '2024-07-16', '1', 28, 1),
(23, '2024-07-16', '0000-00-00', '0', 31, 3),
(24, '2024-07-16', '0000-00-00', '0', 33, 4);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `protocoloview`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `protocoloview` (
`Prot_id` int(10) unsigned
,`ID_Arvore` int(10) unsigned
,`ID_Cli` int(10) unsigned
,`NomeCli` varchar(40)
,`local_id` int(10) unsigned
,`cidade` varchar(40)
,`Estado` varchar(2)
,`LocalArvore` varchar(45)
,`DT_cria` date
,`DT_plant` date
,`ID_Func` int(10) unsigned
,`NomeFunc` varchar(40)
,`Deferido` varchar(1)
);

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

-- --------------------------------------------------------

--
-- Estrutura para view `arvoreinformacao`
--
DROP TABLE IF EXISTS `arvoreinformacao`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `arvoreinformacao`  AS SELECT `arvore`.`id` AS `id`, `arvore`.`cord_latitude` AS `cord_latitude`, `arvore`.`cord_longitude` AS `cord_longitude`, `arvore`.`id_especie` AS `id_especie`, `especie`.`nome` AS `nome_especie`, `arvore`.`id_locais` AS `id_locais`, `uf`.`sigla` AS `Estado`, `locais`.`nome` AS `nome_local`, `locais`.`tipo_plantio` AS `tipo_plantio`, `arvore`.`id_cliente` AS `id_cliente`, `cliente`.`nome` AS `nome_cliente`, `cliente`.`telefone` AS `cli_tel`, `cliente`.`email` AS `cli_email` FROM ((((`arvore` join `especie` on(`arvore`.`id_especie` = `especie`.`id`)) join `locais` on(`arvore`.`id_locais` = `locais`.`id`)) join `cliente` on(`arvore`.`id_cliente` = `cliente`.`id`)) join `uf` on(`locais`.`id_UF` = `uf`.`id`)) ;

-- --------------------------------------------------------

--
-- Estrutura para view `protocoloview`
--
DROP TABLE IF EXISTS `protocoloview`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `protocoloview`  AS SELECT `protocolo`.`id` AS `Prot_id`, `arvore`.`id` AS `ID_Arvore`, `arvore`.`id_cliente` AS `ID_Cli`, `cliente`.`nome` AS `NomeCli`, `locais`.`id` AS `local_id`, `locais`.`cidade` AS `cidade`, `uf`.`sigla` AS `Estado`, `locais`.`nome` AS `LocalArvore`, `protocolo`.`data_criacao` AS `DT_cria`, `protocolo`.`data_plantar` AS `DT_plant`, `funcionario`.`id` AS `ID_Func`, `funcionario`.`nome` AS `NomeFunc`, `protocolo`.`deferido` AS `Deferido` FROM (((((`protocolo` join `funcionario` on(`protocolo`.`id_funcionario` = `funcionario`.`id`)) join `arvore` on(`protocolo`.`id_arvore` = `arvore`.`id`)) join `locais` on(`arvore`.`id_locais` = `locais`.`id`)) join `cliente` on(`arvore`.`id_cliente` = `cliente`.`id`)) join `uf` on(`uf`.`id` = `locais`.`id_UF`)) ;

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
-- Índices de tabela `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`),
  ADD KEY `car_locais` (`id_locais`);

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
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de tabela `bioma`
--
ALTER TABLE `bioma`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `car`
--
ALTER TABLE `car`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

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
-- Restrições para tabelas `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `car_locais` FOREIGN KEY (`id_locais`) REFERENCES `locais` (`id`);

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
