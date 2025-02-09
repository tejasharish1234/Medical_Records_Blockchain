import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "./Doc.css";

// ✅ Doctor/Admin Login Component
function DoctorLogin() {
  const [credentials, setCredentials] = useState({
    hospitalName: "",
    email: "",
    password: "",
  });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  // ✅ Handle Input Changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  // ✅ Form Submission Handler
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Basic validation
    if (!credentials.hospitalName || !credentials.email || !credentials.password) {
      setError("All fields are required.");
      return;
    }

    setError(""); // Clear previous errors
    navigate("/doctor");
  };

  return (
    <div className="form-container">
      <h2>Doctor/Admin Login</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="hospitalName"
          placeholder="Hospital Name"
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

// ✅ Doctor Dashboard Component
function DoctorPage() {
  const navigate = useNavigate();
  const [search, setSearch] = useState("");
  const patients = ["John Doe", "Jane Smith", "Alice Johnson"];

  // Filter patients based on search
  const filteredPatients = patients.filter((p) =>
    p.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="doctor-container">
      <h2>Hospital Dashboard</h2>
      <input
        type="text"
        className="search-bar"
        placeholder="Search patients..."
        onChange={(e) => setSearch(e.target.value)}
      />
      <ul className="patient-list">
        {filteredPatients.length > 0 ? (
          filteredPatients.map((patient, index) => (
            <li key={index} onClick={() => navigate(`/patient/${encodeURIComponent(patient)}`)}>
              {patient}
            </li>
          ))
        ) : (
          <li className="no-results">No patients found.</li>
        )}
      </ul>
    </div>
  );
}

// ✅ Patient Details Component
function PatientDetails() {
  const { name } = useParams();
  
  return (
    <div className="patient-details">
      <h2>Patient Details</h2>
      <p><strong>Name:</strong> {decodeURIComponent(name)}</p>
      <p><strong>IPNS:</strong> 123</p>
      <p><strong>Encryption Key:</strong> abc</p>
      <h3>AI-summarised medical history</h3>
      <p>
      Patient presented with fatigue and shortness of breath.  History of penicillin allergy. Recent two-week course of amoxicillin for a sinus infection. Physical exam revealed mild pallor and tachycardia.  Lab results suggest iron deficiency anemia.
      </p>
    </div>
  );
}

// ✅ Exporting Components
export { DoctorLogin, DoctorPage, PatientDetails };
