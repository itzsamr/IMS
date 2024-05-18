
INSERT INTO Users (userId, username, password, role) VALUES
(1, 'user1', 'password1', 'admin'),
(2, 'user2', 'password2', 'user'),
(3, 'user3', 'password3', 'user'),
(4, 'user4', 'password4', 'user');


INSERT INTO Clients (clientId, clientName, contactInfo, policyId) VALUES
(1, 'Client 1', 'contact1@example.com', 1),
(2, 'Client 2', 'contact2@example.com', 2),
(3, 'Client 3', 'contact3@example.com', 3),
(4, 'Client 4', 'contact4@example.com', 4);


INSERT INTO Claims (claimId, claimNumber, dateFiled, claimAmount, status, policyId, clientId) VALUES
(1, 'CLAIM001', '2024-05-01', 1000.00, 'Pending', 1, 1),
(2, 'CLAIM002', '2024-05-02', 1500.00, 'Approved', 2, 2),
(3, 'CLAIM003', '2024-05-03', 2000.00, 'Pending', 3, 3),
(4, 'CLAIM004', '2024-05-04', 2500.00, 'Approved', 4, 4);


INSERT INTO Payments (paymentId, paymentDate, paymentAmount, clientId) VALUES
(1, '2024-05-05', 500.00, 1),
(2, '2024-05-06', 700.00, 2),
(3, '2024-05-07', 900.00, 3),
(4, '2024-05-08', 1100.00, 4);


INSERT INTO Policies (policyId, policyName, startDate, endDate) VALUES
(1, 'Policy 1', '2024-01-01', '2024-12-31'),
(2, 'Policy 2', '2024-02-01', '2024-11-30'),
(3, 'Policy 3', '2024-03-01', '2024-10-31'),
(4, 'Policy 4', '2024-04-01', '2024-09-30');
