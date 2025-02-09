import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "./Patient.css";

function Register() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ fullName: "", age: "", email: "", password: "", folder: null });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFileUpload = (e) => {
    setFormData({ ...formData, folder: e.target.files });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem("user", JSON.stringify(formData));
    navigate("/login");
  };

  return (
    <div className="form-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="fullName" placeholder="Full Name" onChange={handleChange} required />
        <input type="number" name="age" placeholder="Age" onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <input type="file" directory="" webkitdirectory="" onChange={handleFileUpload} />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

function Login() {
  const navigate = useNavigate();
  const [credentials, setCredentials] = useState({ email: "", password: "" });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const storedUser = JSON.parse(localStorage.getItem("user"));
    if (storedUser && storedUser.email === credentials.email && storedUser.password === credentials.password) {
      navigate("/home");
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

function Home() {
  const [approvedHospitals, setApprovedHospitals] = useState([]);
  const [revokedHospitals, setRevokedHospitals] = useState([]);

  const handleQRCodeScan = () => {
    if (window.confirm("Do you approve the hospital to view your data?")) {
      const hospitalName = prompt("Enter hospital name:");
      if (hospitalName) {
        const updatedHospitals = [...approvedHospitals, hospitalName];
        setApprovedHospitals(updatedHospitals);
        localStorage.setItem("approvedHospitals", JSON.stringify(updatedHospitals));
      }
    }
  };

  const revokeAccess = (hospital) => {
    setApprovedHospitals(approvedHospitals.filter((h) => h !== hospital));
    setRevokedHospitals([...revokedHospitals, hospital]);
  };

  const unRevokeAccess = (hospital) => {
    setRevokedHospitals(revokedHospitals.filter((h) => h !== hospital));
    setApprovedHospitals([...approvedHospitals, hospital]);
  };

  return (
    <div className="home-container">
      <div className="sidebar">
        <h2>Patient Dashboard</h2>
        <p><strong>IPNS Number:</strong> 123</p>
        <p><strong>Encryption Key:</strong> abc</p>
        <button className="scan-button" onClick={handleQRCodeScan}>Add Access</button>

        <h3>Approved Hospitals</h3>
        <ul>
          {approvedHospitals.map((hospital, index) => (
            <li key={index}>
              {hospital}
              <button className="revoke-button" onClick={() => revokeAccess(hospital)}>Revoke</button>
            </li>
          ))}
        </ul>

        <h3>Revoked Access</h3>
        <ul>
          {revokedHospitals.map((hospital, index) => (
            <li key={index}>
              {hospital}
              <button className="unrevoke-button" onClick={() => unRevokeAccess(hospital)}>Unrevoke</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export { Home, Login, Register };
