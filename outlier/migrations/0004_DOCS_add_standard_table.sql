CREATE TABLE documentation.standards
(
	id          SERIAL PRIMARY KEY,
	maintainer  VARCHAR(256),
	description TEXT
);

CREATE TABLE documentation.variable_standard
(
	var_id INTEGER UNIQUE,
	std_id INTEGER,
	PRIMARY KEY (var_id, std_id),
	FOREIGN KEY (var_id) REFERENCES documentation.variables (id),
	FOREIGN KEY (std_id) REFERENCES documentation.standards (id)
);

