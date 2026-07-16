import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div>
      <header className="header">
        <h1>Welcome to ParkZone</h1>
      </header>
      <nav className="nav">
      <Link to="/dashboard" >
            Dashboard
      </Link>
      <Link to="/manage-reservations" >
      Manage Reservations
      </Link>
      <Link to="/manage-slots" >
      Manage Slots
      </Link>
      <Link to="/manage-customers" >
      Manage Customers
      </Link>
      <Link to="/manage-payments" >
      Manage Payments
      </Link>
      <Link to="/reports" >
      Reports
      </Link>
      <Link to="/logout" lassName="logout-link">
      Logout
      </Link>
        {/* <Link to="/home">Home</Link>
        <a href="/manage-reservations">Manage Reservations</a>
        <Link to="/manage-slots">Manage Slots</Link>
        <Link to="/manage-customers">Manage Customers</Link>
        <Link to="/manage-payments">Manage Payments</Link>
        <Link to="/reports">Reports</Link>
        <Link to="/logout">Logout</Link> */}
        
      </nav>
      <div className="home-container">
        <h2>Your One-Stop Solution for Parking Management</h2>
        <p>
          ParkZone helps you manage parking lots, track slot availability, monitor customer usage, and generate detailed reports. Navigate through the menu to get started!
        </p>
        <div className="actions">
          <Link to="#" className="action-button">
            Manage Parking Lots
          </Link>
          <Link to="/reports" className="action-button">
            View Reports
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
