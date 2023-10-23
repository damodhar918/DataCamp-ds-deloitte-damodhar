-- Define the business_type table below
CREATE TABLE business_type (
	id serial PRIMARY KEY,
  	description TEXT NOT NULL
);

-- Define the applicant table below
CREATE TABLE applicant (
	id serial PRIMARY KEY,
  	name TEXT NOT NULL,
  	zip_code CHAR(5) NOT NULL,
  	business_type_id INTEGER references business_type(id)
);

-- Add a schema for Ann Simmons
CREATE SCHEMA AnnSimmons;

-- Add a schema for Ty Beck
CREATE  SCHEMA ty_beck;

-- Add a schema for production data
CREATE  SCHEMA production;

-- Add users table to the public schema for the pod database
CREATE TABLE users (
  id serial PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  hashed_password CHAR(72) NOT NULL
);
-- Create a table named 'bank' in the 'loan_7a' schema
CREATE TABLE loan_7a.bank (
    id SERIAL PRIMARY KEY,
    name VARCHAR (100) NOT NULL,
  	express_provider BOOLEAN
);
-- Create a table named 'borrower' in the 'loan_504' schema
CREATE TABLE loan_504.borrower (
    id Serial PRIMARY KEY,
    fullname VARCHAR (100) NOT NULL
);

-- Create a table named 'borrower' in the 'loan_7a' schema
Create table loan_7a.borrower (
    id serial PRIMARY KEY,
    full_name VARCHAR (100) NOT NULL,
  	indic BOOLEAN
);

-- Create the project table
create table project (
	-- Unique identifier for projects
	id SERIAL PRIMARY KEY,
    -- Whether or not project is franchise opportunity
	is_franchise BOOLEAN DEFAULT FALSE,
	-- Franchise name if project is franchise opportunity
    franchise_name TEXT DEFAULT NULL,
    -- State where project will reside
    project_state TEXT,
    -- County in state where project will reside
    project_county TEXT,
    -- District number where project will reside
    congressional_district NUMERIC,
    -- Amount of jobs projected to be created
    jobs_supported NUMERIC
);

-- Create the appeal table
Create table appeal (
    -- Specify the unique identifier column
	id SERIAL primary key,
    -- Define a column for holding the text of the appeals
    content text NOT NULL
);
-- Create the client table
create table client(
	-- Unique identifier column
	id serial PRIMARY KEY,
    -- Name of the company
    name VARCHAR(50),
	-- Specify a text data type for variable length urls
	site_url VARCHAR(50),
    -- Number of employees (max of 1500 for small business)
    num_employees smallint,
    -- Number of customers
    num_customers integer
);
-- Create the campaign table
CREATE TABLE campaign (
  -- Unique identifier column
  id SERIAL PRIMARY KEY,
  -- Campaign name column
  name VARCHAR(50),
  -- The campaign's budget
  budget NUMERIC(7, 2),
  -- The duration of campaign in days
  num_days SMALLINT DEFAULT 30,
  -- The number of new applications desired
  goal_amount INTEGER DEFAULT 100,
  -- The number of received applications
  num_applications INTEGER DEFAULT 0
);

CREATE TABLE appeal (
	id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
  	-- Add received_on column
    received_on timestamp DEFAULT CURRENT_TIMESTAMP,
  	
  	-- Add approved_on_appeal column
  	approved_on_appeal boolean DEFAULT NULL,
  	
  	-- Add reviewed column
    reviewed date
);
-- Create the loan table
CREATE TABLE loan (
	borrower_id INTEGER REFERENCES borrower(id),
    bank_id INTEGER REFERENCES bank(id),
  	-- 'approval_date': the loan approval date
    approval_date DATE NOT NULL DEFAULT CURRENT_DATE,
    -- 'gross_approval': amounts up to $5,000,000.00
  	gross_approval DECIMAL(9, 2) NOT NULL,
  	-- 'term_in_months': total # of months for repayment
    term_in_months SMALLINT NOT NULL,
    -- 'revolver_status': TRUE for revolving line of credit
  	revolver_status BOOLEAN NOT NULL DEFAULT FALSE,
  	initial_interest_rate DECIMAL(4, 2) NOT NULL
);
-- Create the place table
CREATE TABLE place (
  -- Define zip_code column
  zip_code CHAR(5) PRIMARY KEY,
  -- Define city column
  city VARCHAR(50) NOT NULL,
  -- Define state column
  state CHAR(2) NOT NULL
);

CREATE TABLE borrower (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  approved BOOLEAN DEFAULT NULL,
  
  -- Remove zip_code column (defined below)
  
  -- Remove city column (defined below)
  
  -- Remove state column (defined below)
  
  -- Add column referencing place table
  place_id CHAR(5) REFERENCES place(zip_code)
);
-- Create the contact table
CREATE TABLE contact (
  	-- Define the id column
	id SERIAL PRIMARY KEY,
  	-- Define the name column
  	name VARCHAR(50) NOT NULL,
    -- Define the email column
  	email VARCHAR(50) NOT NULL
);

-- Add contact_id to the client table
ALTER TABLE client ADD contact_id INTEGER NOT NULL;

-- Add FOREIGN KEY constraint on contact_id to client table
ALTER TABLE client ADD CONSTRAINT fk_c_id FOREIGN KEY (contact_id) REFERENCES contact(id);
-- Create the test_grade table
create table test_grade (
    -- Include a column for the student id
	student_id integer NOT NULL,
  
  	-- Include a column for the course name
    course_name varchar(50) NOT NULL,
  
  	-- Add a column to capture a single test grade
    grade Numeric NOT NULL
);

INSERT INTO loan (
  	borrower_id, bank_id, approval_month, approval_day,
  	approval_year, gross_approval, term_in_months,
  	revolver_status, initial_interest_rate
) VALUES (12, 14, 12, 1, 2013, 421115, 120, false, 4.42);

--INSERT INTO loan (
--  	borrower_id, bank_id, approval_month, approval_day,
--  	approval_year, gross_approval, term_in_months,
--  	revolver_status, initial_interest_rate
--) VALUES (3, 201, 6, 42, 2017, 30015, 60, true, 3.25);

INSERT INTO loan (
  	borrower_id, bank_id, approval_month, approval_day,
  	approval_year, gross_approval, term_in_months,
  	revolver_status, initial_interest_rate
) VALUES (19, 5, 8, 19, 2018, 200000, 120, false, 6.3);

-- Create the course table
create table course (
    -- Add a column for the course table
	id serial Primary key,
  
  	-- Add a column for the course table
  	name varchar(50) not null,
  
  	-- Add a column for the course table
  	max_students smallint
);
CREATE TABLE ingredient (
  -- Add PRIMARY KEY for table
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE meal (
    -- Make id a PRIMARY KEY
	id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
  
  	-- Remove the 2 columns (below) that do not satisfy 2NF
    avg_student_rating NUMERIC,
    total_calories SMALLINT NOT NULL
);

CREATE TABLE meal_date (
    -- Define a column referencing the meal table
  	meal_id INTEGER REFERENCES meal(id),
    date_served DATE NOT NULL
);

CREATE TABLE meal_ingredient (
  	meal_id INTEGER REFERENCES meal(id),
  
    -- Define a column referencing the ingredient table
    ingredient_id INTEGER REFERENCES ingredient(id)
);
-- Complete the definition of the table for zip codes
CREATE TABLE zip (
	code INTEGER PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL
);

-- Complete the definition of the "zip_code" column
CREATE TABLE school (
	id serial PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    street_address VARCHAR(100) NOT NULL,
    zip_code INTEGER REFERENCES zip(code)
);

-- Add new columns to the borrower table
ALTER TABLE borrower
ADD COLUMN first_name VARCHAR (50) NOT NULL,
ADD COLUMN last_name VARCHAR (50) NOT NULL;

-- Remove column from borrower table to satisfy 1NF
ALTER TABLE borrower
DROP COLUMN full_name;

-- Add columns to the borrower table
ALTER TABLE borrower
ADD COLUMN first_name VARCHAR (50) NOT NULL,
ADD COLUMN last_name VARCHAR (50) NOT NULL;

-- Remove column from borrower table to satisfy 1NF
ALTER TABLE borrower
DROP COLUMN full_name;

-- Add a new column called 'zip' to the 'bank' table 
ALTER TABLE bank
ADD COLUMN zip VARCHAR(10) NOT NULL;

-- Remove a corresponding column from 'loan' to satisfy 2NF
ALTER TABLE loan
DROP COLUMN bank_zip;

-- Define 'program' table with max amount for each program
CREATE TABLE program (
  	id serial PRIMARY KEY,
  	description text NOT NULL,
  	max_amount DECIMAL(9,2) NOT NULL
);

-- Alter the 'loan' table to satisfy 3NF
ALTER TABLE loan
ADD COLUMN program_id INTEGER REFERENCES program (id),
DROP COLUMN program,
DROP COLUMN max_amount;

-- Add columns to the borrower table
ALTER TABLE borrower
ADD COLUMN first_name VARCHAR (50) NOT NULL,
ADD COLUMN last_name VARCHAR (50) NOT NULL;

-- Remove column from borrower table to satisfy 1NF
ALTER TABLE borrower
DROP COLUMN full_name;

-- Add a new column called 'zip' to the 'bank' table
ALTER TABLE bank
ADD COLUMN zip VARCHAR(10) NOT NULL;

-- Remove a corresponding column from 'loan' to satisfy 2NF
ALTER TABLE loan
DROP COLUMN bank_zip;

-- Define 'program' table with max amount for each program
CREATE TABLE program (
  	id serial PRIMARY KEY,
  	description text NOT NULL,
  	max_amount DECIMAL(9,2) NOT NULL
);

-- Add columns to the borrower table
ALTER TABLE borrower
ADD COLUMN first_name VARCHAR (50) NOT NULL,
ADD COLUMN last_name VARCHAR (50) NOT NULL;

-- Remove column from borrower table to satisfy 1NF
ALTER TABLE borrower
DROP COLUMN full_name;

-- Add a new column named 'zip' to the 'bank' table 
ALTER TABLE bank
ADD COLUMN zip VARCHAR(10) NOT NULL;

-- Remove corresponding column from 'loan' to satisfy 2NF
ALTER TABLE loan
DROP COLUMN bank_zip;

-- Add new columns to the borrower table
ALTER TABLE borrower
ADD COLUMN first_name VARCHAR (50) NOT NULL,
ADD COLUMN last_name VARCHAR (50) NOT NULL;

-- Remove column from borrower table to satisfy 1NF
ALTER TABLE borrower
DROP COLUMN full_name;

-- Create sgold with a temporary password
create user sgold with password 'changeme';

-- Update the password for sgold
alter user sgold with password 'kxqr478-?egH%&FQ';



-- Grant the INSERT privilege
GRANT insert ON loan TO sgold;
-- Grant the UPDATE privilege
GRANT update ON loan TO sgold;
-- Grant the SELECT privilege
Grant select ON loan TO sgold;
-- Grant the DELETE privilege
Grant delete on loan to sgold;


-- Provide sgold with the required table privileges
alter TABLE loan owner TO sgold;

-- Create a user account for Ronald Jones
CREATE user rjones WITH password 'changeme';

-- Create a user account for Kim Lopez
Create user klopez with password 'changeme';

-- Create a user account for Jessica Chen
create user jchen with password 'changeme';

-- Create the dev_team group
create group dev_team;

-- Grant privileges to dev_team group on loan table
GRANT insert, update, delete, select ON loan TO dev_team;

-- Add the new user accounts to the dev_team group
ALTER GROUP dev_team ADD USER rjones, klopez, jchen;

-- Create the development schema
create schema development;

-- Grant usage privilege on new schema to dev_team
grant usage ON SCHEMA development TO dev_team;

-- Create a loan table in the development schema
create table development.loan (
	borrower_id INTEGER,
	bank_id INTEGER,
	approval_date DATE,
	program text NOT NULL,
	max_amount DECIMAL(9,2) NOT NULL,
	gross_approval DECIMAL(9, 2) NOT NULL,
	term_in_months SMALLINT NOT NULL,
	revolver_status BOOLEAN NOT NULL,
	bank_zip VARCHAR(10) NOT NULL,
	initial_interest_rate DECIMAL(4, 2) NOT NULL
);

-- Grant privileges on development schema
Grant select, insert, update, delete ON ALL TABLES IN SCHEMA development TO dev_team;



-- Remove the specified privileges for Kim
Revoke insert, update, delete ON development.loan FROM klopez;

-- Create the project_management group
create group project_management;

-- Grant project_management SELECT privilege
GRANT select ON loan TO project_management;

-- Add Kim's user to project_management group
alter group project_management ADD USER klopez;

-- Remove Kim's user from dev_team group
REVOKE dev_team FROM klopez;


-- Create the new analysis schema
CREATE SCHEMA analysis;

-- Create a table unapproved loan under the analysis schema
CREATE TABLE analysis.unapproved_loan (
    id serial PRIMARY KEY,
    loan_id INTEGER REFERENCES loan(id),
    description TEXT NOT NULL
);

-- Create 'data_scientist' user with password 'changeme'
CREATE USER data_scientist WITH PASSWORD 'changeme';

-- Give 'data_scientist' ability to use 'analysis' schema 
GRANT USAGE ON SCHEMA analysis TO data_scientist;

-- Grant read-only access to table for 'data_scientist' user
GRANT SELECT ON analysis.unapproved_loan TO data_scientist;