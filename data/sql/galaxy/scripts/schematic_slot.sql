# --------------------------------------------------------
# Host:                         127.0.0.1
# Server version:               5.3.1-MariaDB
# Server OS:                    Win32
# HeidiSQL version:             6.0.0.3603
# Date/time:                    2011-10-14 14:04:29
# --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

# Dumping structure for table galaxy.schematic_slot
DROP TABLE IF EXISTS `schematic_slot`;
CREATE TABLE IF NOT EXISTS `schematic_slot` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `manufacture_schematic_id` bigint(20) DEFAULT NULL,
  `stf_file` varchar(255) NOT NULL,
  `stf_name` varchar(255) NOT NULL,
  `type` int(11) NOT NULL,
  `ingredient` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `clean` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_1B0D2FAB4DE6846C` (`manufacture_schematic_id`),
  CONSTRAINT `FK_1B0D2FAB4DE6846C` FOREIGN KEY (`manufacture_schematic_id`) REFERENCES `manufacture_schematic` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table galaxy.schematic_slot: ~0 rows (approximately)
DELETE FROM `schematic_slot`;
/*!40000 ALTER TABLE `schematic_slot` DISABLE KEYS */;
/*!40000 ALTER TABLE `schematic_slot` ENABLE KEYS */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
