
DROP INDEX IDX_IOC_SYSTEM_1_3_1_CTIME ON IOC_SYSTEM_1_3_1;

DROP INDEX IDX_IOC_SYSTEM_1_3_1_PRI ON IOC_SYSTEM_1_3_1;

DROP TABLE IF EXISTS IOC_SYSTEM_1_3_1;

/*==============================================================*/
/* Table: IOC_SYSTEM_1_3_1                                            */
/*==============================================================*/
CREATE TABLE IOC_SYSTEM_1_3_1
(
   F5007               VARCHAR(50) NOT NULL,
   FTP_ID               VARCHAR(50),
   DOMAIN_ID            VARCHAR(50) NOT NULL,
   F1642             VARCHAR(50),
   F1316              BIGINT(20),
   F1507           VARCHAR(50),
   F5006                 VARCHAR(200) NOT NULL,
   F1186                 VARCHAR(200) NOT NULL,
   APP_TYPE             VARCHAR(20) NOT NULL,
   IS_SITE              TINYINT(1) NOT NULL DEFAULT 0,
   F1622          TINYINT(1) DEFAULT 0,
   IS_F1375_APP        TINYINT(1) DEFAULT 0,
   F5013               INT(10) NOT NULL DEFAULT 1,
   F5014             INT(10) NOT NULL DEFAULT 10,
   F5017          DATETIME,
   F5010            TIMESTAMP,
   F5008             INT(10) DEFAULT 0,
   F1582          DATETIME,
   F5015          VARCHAR(800),
   SPARE1               VARCHAR(255),
   SPARE2               VARCHAR(255),
   PRIMARY KEY (F5007)
);

/*==============================================================*/
/* Index: IDX_IOC_SYSTEM_1_3_1_PRI                                    */
/*==============================================================*/
CREATE INDEX IDX_IOC_SYSTEM_1_3_1_PRI ON IOC_SYSTEM_1_3_1
(
   F5014
);

/*==============================================================*/
/* Index: IDX_IOC_SYSTEM_1_3_1_CTIME                                  */
/*==============================================================*/
CREATE INDEX IDX_IOC_SYSTEM_1_3_1_CTIME ON IOC_SYSTEM_1_3_1
(
   F5017
);
