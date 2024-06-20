CREATE SCHEMA IF NOT EXISTS documentation;

CREATE TABLE IF NOT EXISTS documentation.publications
(
	id           SERIAL PRIMARY KEY,
	name         VARCHAR(512),
	organization VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS documentation.data_tables
(
	id               SERIAL PRIMARY KEY,
	table_name       VARCHAR(256),
	unit_of_analysis VARCHAR(256),
	pub_id           INTEGER,
	acquisition_date TIMESTAMP,
	publish_date     TIMESTAMP,       
	start_date       TIMESTAMP,
	end_date         TIMESTAMP,
	FOREIGN KEY (pub_id) REFERENCES documentation.publications (id)
);

CREATE TABLE IF NOT EXISTS documentation.keywords
(
	id      SERIAL PRIMARY KEY,
	content VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS documentation.tags
(
	table_id INTEGER,
	kw_id    INTEGER,
	PRIMARY KEY (table_id, kw_id),
	FOREIGN KEY (table_id) REFERENCES documentation.data_tables (id),
	FOREIGN KEY (kw_id)    REFERENCES documentation.keywords (id)
);

CREATE TABLE IF NOT EXISTS documentation.variables
(
	id              SERIAL PRIMARY KEY,
	variable_name   VARCHAR(256),
	table_id        INTEGER,
	parent_variable INTEGER,
	FOREIGN KEY (table_id) REFERENCES documentation.data_tables (id),
	FOREIGN KEY (parent_variable) REFERENCES documentation.variables (id)
);

