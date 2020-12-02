-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 13, 2020 at 08:12 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pspro`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_arsip`
--

CREATE TABLE `tbl_arsip` (
  `id_arsip` int(10) NOT NULL,
  `no_surat` int(10) NOT NULL,
  `kd_jabatan` int(5) NOT NULL,
  `id_dispo` int(10) NOT NULL,
  `nrp` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_dispo`
--

CREATE TABLE `tbl_dispo` (
  `id_dispo` int(10) NOT NULL,
  `nm_dispo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_jabatan`
--

CREATE TABLE `tbl_jabatan` (
  `kd_jabatan` int(5) NOT NULL,
  `nm_jabatan` varchar(100) NOT NULL,
  `kd_pangkat` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_kategori`
--

CREATE TABLE `tbl_kategori` (
  `id_kategori` int(10) NOT NULL,
  `nm_kategori` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_klasifikasi`
--

CREATE TABLE `tbl_klasifikasi` (
  `id_klasifikasi` int(10) NOT NULL,
  `nm_klasifikasi` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_korp_raport`
--

CREATE TABLE `tbl_korp_raport` (
  `id_korp` int(10) NOT NULL,
  `kd_jabatan` int(10) NOT NULL,
  `kd_pangkat` int(10) NOT NULL,
  `id_dispo` int(10) NOT NULL,
  `nrp` int(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nrp1` int(20) NOT NULL,
  `nama1` varchar(100) NOT NULL,
  `keperluan` varchar(100) NOT NULL,
  `tanggapan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pangkat`
--

CREATE TABLE `tbl_pangkat` (
  `kd_pangkat` int(5) NOT NULL,
  `nm_pangkat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pejabat`
--

CREATE TABLE `tbl_pejabat` (
  `nrp` int(20) NOT NULL,
  `nm_pejabat` varchar(200) NOT NULL,
  `tmt_jabatan` int(20) NOT NULL,
  `kd_jabatan` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_surat_keluar`
--

CREATE TABLE `tbl_surat_keluar` (
  `id_surat_keluar` int(11) NOT NULL,
  `no_surat` int(11) NOT NULL,
  `id_kategori` int(10) NOT NULL,
  `id_klasifikasi` int(10) NOT NULL,
  `nrp` int(20) NOT NULL,
  `tujuan` int(100) NOT NULL,
  `tembusan` int(100) NOT NULL,
  `perihal` varchar(100) NOT NULL,
  `file_path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_surat_masuk`
--

CREATE TABLE `tbl_surat_masuk` (
  `id_surat_masuk` int(10) NOT NULL,
  `no_surat` int(10) NOT NULL,
  `id_kategori` int(10) NOT NULL,
  `id_klasifikasi` int(10) NOT NULL,
  `nrp` int(20) NOT NULL,
  `pengirim` int(100) NOT NULL,
  `perihal` varchar(100) NOT NULL,
  `file_path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_userlog`
--

CREATE TABLE `tbl_userlog` (
  `nrp` int(20) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_arsip`
--
ALTER TABLE `tbl_arsip`
  ADD PRIMARY KEY (`id_arsip`);

--
-- Indexes for table `tbl_dispo`
--
ALTER TABLE `tbl_dispo`
  ADD PRIMARY KEY (`id_dispo`);

--
-- Indexes for table `tbl_jabatan`
--
ALTER TABLE `tbl_jabatan`
  ADD PRIMARY KEY (`kd_jabatan`),
  ADD KEY `R_Pangkat_Jabatan` (`kd_pangkat`);

--
-- Indexes for table `tbl_kategori`
--
ALTER TABLE `tbl_kategori`
  ADD PRIMARY KEY (`id_kategori`);

--
-- Indexes for table `tbl_klasifikasi`
--
ALTER TABLE `tbl_klasifikasi`
  ADD PRIMARY KEY (`id_klasifikasi`);

--
-- Indexes for table `tbl_pangkat`
--
ALTER TABLE `tbl_pangkat`
  ADD PRIMARY KEY (`kd_pangkat`);

--
-- Indexes for table `tbl_pejabat`
--
ALTER TABLE `tbl_pejabat`
  ADD PRIMARY KEY (`nrp`),
  ADD KEY `R_Jabatan_Pejabat` (`kd_jabatan`);

--
-- Indexes for table `tbl_userlog`
--
ALTER TABLE `tbl_userlog`
  ADD PRIMARY KEY (`nrp`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_jabatan`
--
ALTER TABLE `tbl_jabatan`
  ADD CONSTRAINT `R_Pangkat_Jabatan` FOREIGN KEY (`kd_pangkat`) REFERENCES `tbl_pangkat` (`kd_pangkat`);

--
-- Constraints for table `tbl_pejabat`
--
ALTER TABLE `tbl_pejabat`
  ADD CONSTRAINT `R_Jabatan_Pejabat` FOREIGN KEY (`kd_jabatan`) REFERENCES `tbl_jabatan` (`kd_jabatan`);

--
-- Constraints for table `tbl_userlog`
--
ALTER TABLE `tbl_userlog`
  ADD CONSTRAINT `R_Pejabat_userlog` FOREIGN KEY (`nrp`) REFERENCES `tbl_pejabat` (`nrp`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
