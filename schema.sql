CREATE TABLE stakeholders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    role VARCHAR(255)
);

CREATE TABLE requirements (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50),
    description TEXT,
    clarity_score INT,
    completeness_score INT,
    consistency_score INT,
    structure_score INT,
    stakeholder_score INT
);
