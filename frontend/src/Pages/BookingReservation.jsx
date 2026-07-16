import React, { useState } from 'react';
import './BookingReservation.css';

const BookingReservation = () => {
  const [parkingLot, setParkingLot] = useState('');
  const [category, setCategory] = useState('');
  const [timeSlot, setTimeSlot] = useState('');
  const [date, setDate] = useState('');
  const [price, setPrice] = useState('');

  const handleBooking = (e) => {
    e.preventDefault();
    alert(`Booking successful for ${parkingLot} on ${date} at ${timeSlot} in ${category} category!`);
    // Implement backend booking API call here
  };

  return (
    <div className="booking-container">
      <h1>Book Parking Slot</h1>
      <form className="booking-form" onSubmit={handleBooking}>
        <div className="form-group">
          <label htmlFor="parkingLot">Select Parking Lot:</label>
          <select
            id="parkingLot"
            value={parkingLot}
            onChange={(e) => setParkingLot(e.target.value)}
            required
          >
            <option value="">Select Parking Lot</option>
            <option value="Downtown Parking">Downtown Parking</option>
            <option value="Airport Parking">Airport Parking</option>
            {/* Add more parking lots */}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="category">Select Category:</label>
          <select
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          >
            <option value="">Select Category</option>
            <option value="temporary">Temporary Parking</option>
            <option value="permanent">Permanent Parking</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="date">Select Date:</label>
          <input
            type="date"
            id="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="timeSlot">Select Time Slot:</label>
          <input
            type="time"
            id="timeSlot"
            value={timeSlot}
            onChange={(e) => setTimeSlot(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <input
            type="text"
            id="price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            placeholder="Enter price"
            required
          />
        </div>
        <button type="submit" className="book-button">Book Now</button>
      </form>
    </div>
  );
};

export default BookingReservation;
