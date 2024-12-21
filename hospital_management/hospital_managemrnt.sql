CREATE DATABASE hospital_management;

-- Create Departments Table
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- Create Doctors Table
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create Patients Table
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Phone VARCHAR(15) NOT NULL
);

-- Create Appointments Table
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    DoctorID INT,
    PatientID INT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);
