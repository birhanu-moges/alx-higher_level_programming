-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server.
  -- Table - states:
    -- id INT UNIQUE, auto generated, not NULL and is PRIMARY KEY
    -- name VARCHAR(256) not NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);