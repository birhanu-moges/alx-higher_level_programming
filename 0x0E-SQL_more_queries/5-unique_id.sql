-- Creates the table unique_id on MySQL server.
   -- Table unique_id:
      -- id INT with DEFAULT value 1 and must be unique
      -- name VARCHAR(256)
CREATE TABLE unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
