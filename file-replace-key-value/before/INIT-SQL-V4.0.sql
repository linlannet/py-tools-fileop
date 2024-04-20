
DROP INDEX IDX_GLOBAL_APP_CTIME ON GLOBAL_APP;

DROP INDEX IDX_GLOBAL_APP_PRI ON GLOBAL_APP;

DROP TABLE IF EXISTS GLOBAL_APP;

/*==============================================================*/
/* Table: GLOBAL_APP                                            */
/*==============================================================*/
CREATE TABLE GLOBAL_APP
(
   APP_ID               VARCHAR(50) NOT NULL,
   FTP_ID               VARCHAR(50),
   DOMAIN_ID            VARCHAR(50) NOT NULL,
   ORGAN_ID             VARCHAR(50),
   XZQH_ID              BIGINT(20),
   SERTYPE_ID           VARCHAR(50),
   NAME                 VARCHAR(200) NOT NULL,
   PATH                 VARCHAR(200) NOT NULL,
   APP_TYPE             VARCHAR(20) NOT NULL,
   IS_SITE              TINYINT(1) NOT NULL DEFAULT 0,
   IS_DISABLED          TINYINT(1) DEFAULT 0,
   IS_MOBILE_APP        TINYINT(1) DEFAULT 0,
   STATUS               INT(10) NOT NULL DEFAULT 1,
   PRIORITY             INT(10) NOT NULL DEFAULT 10,
   CREATE_TIME          DATETIME,
   LAST_TIME            TIMESTAMP,
   DEL_FLAG             INT(10) DEFAULT 0,
   DELETE_TIME          DATETIME,
   DESCRIPTION          VARCHAR(800),
   SPARE1               VARCHAR(255),
   SPARE2               VARCHAR(255),
   PRIMARY KEY (APP_ID)
);

/*==============================================================*/
/* Index: IDX_GLOBAL_APP_PRI                                    */
/*==============================================================*/
CREATE INDEX IDX_GLOBAL_APP_PRI ON GLOBAL_APP
(
   PRIORITY
);

/*==============================================================*/
/* Index: IDX_GLOBAL_APP_CTIME                                  */
/*==============================================================*/
CREATE INDEX IDX_GLOBAL_APP_CTIME ON GLOBAL_APP
(
   CREATE_TIME
);
