CREATE TABLE `proposals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `identifier` VARCHAR(45) NULL,
  `title` VARCHAR(45) NULL,
  `category` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `team_member_count` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `identifier_UNIQUE` (`identifier` ASC) VISIBLE);

ALTER TABLE `proposals` 
CHANGE COLUMN `team_member_count` `team_member_count` INT NULL DEFAULT NULL ,
CHANGE COLUMN `status` `status` INT NULL DEFAULT NULL ;

