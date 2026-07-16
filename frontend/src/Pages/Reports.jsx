import React from 'react';
import './Reports.css';
import { Link } from 'react-router-dom';

const Reports = () => {
  return (
    <div>
      <header className="header">
        <h1>Reports</h1>
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
        {/* <a href="/dashboard">Dashboard</a> */}
        {/* <a href="/manage-reservations">Manage Reservations</a>
        <a href="/manage-slots">Manage Slots</a>
        <a href="manage-customers">Manage Customers</a>
        <a href="/reports">Reports</a>
        <a href="/logout" className="logout-link">Logout</a> */}
      </nav>
      <div className="container">
        <h2>Parking Management Reports</h2>
        <div className="report-section">
          <h3>Parking Lot Usage</h3>
          <p>Details about the usage of parking lots (occupancy, capacity, etc.).</p>
          <button className="view-report-button">View Report</button>
        </div>
        <div className="report-section">
          <h3>Slot Availability</h3>
          <p>Details about the availability of parking slots across all parking lots.</p>
          <button className="view-report-button">View Report</button>
        </div>
        <div className="report-section">
          <h3>Customer Activity</h3>
          <p>Details about customer activities, bookings, and payments.</p>
          <button className="view-report-button">View Report</button>
        </div>
      </div>
    </div>
  );
};

export default Reports;
