/*
 Navicat MySQL Data Transfer

 Source Server         : sun
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3306
 Source Schema         : mydatabse

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 03/06/2024 18:15:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `cno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cteacher` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ist` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`cno`) USING BTREE,
  INDEX `tno`(`tno`) USING BTREE,
  CONSTRAINT `class_ibfk_1` FOREIGN KEY (`tno`) REFERENCES `teacher` (`tno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('110', '数据库', '宋老师', '1122423', '是');
INSERT INTO `class` VALUES ('111', '计组', '张老师', '1122424', '否');
INSERT INTO `class` VALUES ('112', 'c语言', '宋老师', '1122423', '是');

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `tno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `grade` int NULL DEFAULT NULL,
  PRIMARY KEY (`cno`, `sno`) USING BTREE,
  INDEX `grade_ibfk_1`(`sno`, `cno`) USING BTREE,
  CONSTRAINT `grade_ibfk_1` FOREIGN KEY (`sno`, `cno`) REFERENCES `selclass` (`sno`, `cno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES ('1122423', '2212422', '110', 0);
INSERT INTO `grade` VALUES ('1122424', '2212422', '111', 99);
INSERT INTO `grade` VALUES ('1122424', '2212423', '111', 100);

-- ----------------------------
-- Table structure for selclass
-- ----------------------------
DROP TABLE IF EXISTS `selclass`;
CREATE TABLE `selclass`  (
  `sno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ist` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`sno`, `cno`) USING BTREE,
  INDEX `selclass_ibfk_2`(`cno`) USING BTREE,
  CONSTRAINT `selclass_ibfk_1` FOREIGN KEY (`sno`) REFERENCES `student` (`sno`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `selclass_ibfk_2` FOREIGN KEY (`cno`) REFERENCES `class` (`cno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of selclass
-- ----------------------------
INSERT INTO `selclass` VALUES ('2212422', '110', '是');
INSERT INTO `selclass` VALUES ('2212422', '111', '否');
INSERT INTO `selclass` VALUES ('2212423', '110', '是');
INSERT INTO `selclass` VALUES ('2212423', '111', '否');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `sno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NOT NULL,
  `department` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('2212422', '孙七四', '男', 20, '计算机学院', '123456');
INSERT INTO `student` VALUES ('2212423', '孙七五', '男', 20, '计算机学院', '123456');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NOT NULL,
  `department` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tpassword` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`tno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1122422', '陈是', '男', 36, '计算机学院', '123456');
INSERT INTO `teacher` VALUES ('1122423', '宋老师', '女', 20, '计算机学院', '123456');
INSERT INTO `teacher` VALUES ('1122424', '张老师', '男', 38, '计算机学院', '123456');

-- ----------------------------
-- View structure for gradev
-- ----------------------------
DROP VIEW IF EXISTS `gradev`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `gradev` AS select `grade`.`cno` AS `cno`,`class`.`name` AS `name`,`class`.`cteacher` AS `cteacher`,`grade`.`grade` AS `grade`,`grade`.`sno` AS `sno` from (`grade` join `class` on((`class`.`cno` = `grade`.`cno`)));

-- ----------------------------
-- Procedure structure for tuike
-- ----------------------------
DROP PROCEDURE IF EXISTS `tuike`;
delimiter ;;
CREATE PROCEDURE `tuike`(IN `id` VARCHAR(20), IN `ist` VARCHAR(20))
BEGIN  
    IF ist = '是' OR ist = '否' THEN  
        UPDATE class
        inner JOIN selclass ON class.cno = selclass.cno  
        SET class.ist = ist, selclass.ist = ist  
        WHERE class.cno = id;  
				
    ELSE  
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '输入不正确';  
    END IF;  
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table grade
-- ----------------------------
DROP TRIGGER IF EXISTS `before_update_grade`;
delimiter ;;
CREATE TRIGGER `before_update_grade` BEFORE UPDATE ON `grade` FOR EACH ROW BEGIN  
    IF NEW.grade > 100 OR NEW.grade < 0 THEN  
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '成绩区间不对';  
    END IF;  
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table selclass
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_after_delete_selclass`;
delimiter ;;
CREATE TRIGGER `trg_after_delete_selclass` BEFORE DELETE ON `selclass` FOR EACH ROW BEGIN  
    IF OLD.ist = '否' THEN  
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '不能退课';  
    END IF;  
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table selclass
-- ----------------------------
DROP TRIGGER IF EXISTS `before_insert_selclass`;
delimiter ;;
CREATE TRIGGER `before_insert_selclass` BEFORE INSERT ON `selclass` FOR EACH ROW BEGIN  
    IF EXISTS (SELECT 1 FROM selclass WHERE cno = NEW.cno AND sno = NEW.sno) THEN  
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '不能重复选课.';  
    END IF;  
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
