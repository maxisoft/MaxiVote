/*
Target Server Type    : SQLite
Target Server Version : 30706
File Encoding         : 65001

Date: 2013-06-24 15:22:39
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for "sqlite_sequence"
-- ----------------------------
DROP TABLE "sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Records of sqlite_sequence
-- ----------------------------
INSERT INTO "sqlite_sequence" VALUES ('vote_vote', 0);
INSERT INTO "sqlite_sequence" VALUES ('vote_account', 0);

-- ----------------------------
-- Table structure for "vote_account"
-- ----------------------------
DROP TABLE "vote_account";
CREATE TABLE "vote_account" (
"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"login"  VARCHAR NOT NULL,
"password"  VARCHAR NOT NULL,
"sitename"  VARCHAR NOT NULL,
"priority"  INTEGER DEFAULT 0,
"proxy"  VARCHAR,
CONSTRAINT "login_unique" UNIQUE ("login" ASC, "sitename" ASC)
);

-- ----------------------------
-- Table structure for "vote_vote"
-- ----------------------------
DROP TABLE "vote_vote";
CREATE TABLE "vote_vote" (
"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"sitename"  VARCHAR NOT NULL,
"account_id"  INTEGER NOT NULL,
"date"  VARCHAR NOT NULL,
"top"  VARCHAR NOT NULL,
"ip"  VARCHAR,
CONSTRAINT "fk_account" FOREIGN KEY ("account_id") REFERENCES "vote_account" ("id")
);


-- ----------------------------
-- Indexes structure for table vote_account
-- ----------------------------
CREATE INDEX "login_index"
ON "vote_account" ("login" ASC);
CREATE INDEX "sitename_index"
ON "vote_account" ("sitename" ASC);

-- ----------------------------
-- Indexes structure for table vote_vote
-- ----------------------------
CREATE INDEX "index_date"
ON "vote_vote" ("date" ASC);
CREATE INDEX "index_sitename"
ON "vote_vote" ("sitename" ASC);
CREATE INDEX "index_top"
ON "vote_vote" ("top" ASC);
