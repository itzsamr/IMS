CREATE DATABASE IMSDB;

USE IMSDB;

CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE Clients (
    clientId INT PRIMARY KEY,
    clientName VARCHAR(255) NOT NULL,
    contactInfo VARCHAR(255) NOT NULL,
    policyId INT,
    FOREIGN KEY (policyId) REFERENCES Policies(policyId)
);

CREATE TABLE Claims (
    claimId INT PRIMARY KEY,
    claimNumber VARCHAR(50) NOT NULL,
    dateFiled DATE NOT NULL,
    claimAmount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    policyId INT,
    clientId INT,
    FOREIGN KEY (policyId) REFERENCES Policies(policyId),
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);

CREATE TABLE Payments (
    paymentId INT PRIMARY KEY,
    paymentDate DATE NOT NULL,
    paymentAmount DECIMAL(10, 2) NOT NULL,
    clientId INT,
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);

CREATE TABLE Policies (
    policyId INT PRIMARY KEY,
    policyName VARCHAR(255) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
);

