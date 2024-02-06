import React, { useState } from 'react';
import axios from 'axios';
import './findTrucks.css'; // Import the CSS file

const FindTrucks = () => {
  const [radius, setRadius] = useState(100); // Default radius
  const [location, setLocation] = useState(null);
  const [foodTrucks, setFoodTrucks] = useState([]);

  const handleRadiusChange = (event) => {
    setRadius(event.target.value);
  };

  const handleLocationChange = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
          });
        },
        (error) => {
          console.error('Error getting location:', error);
        }
      );
    } else {
      console.error('Geolocation is not supported by your browser');
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/get_food_trucks/', {
        radius: radius,
        location: location,
      });

      setFoodTrucks(response.data)
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="find-trucks-container">
      <h2>Food Truck Locator</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Radius (in meters):
          <input type="number" value={radius} onChange={handleRadiusChange} />
        </label>
        <br />
        <button type="button" onClick={handleLocationChange}>
          Get My Location
        </button>
        <br />
        <button type="submit">Find Food Trucks</button>
      </form>

      {foodTrucks.length > 0 && (
        <div>
          <h3>Found Food Trucks</h3>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Distance</th>
                <th>Address</th>
                <th>Menu</th>

              </tr>
            </thead>
            <tbody>
              {foodTrucks.map((truck) => (
                <tr key={truck.id}>
                  <td>{truck.name}</td>
                  <td>{truck.distance} km</td>
                  <td>{truck.address}</td>
                  <td>{truck.menu}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default FindTrucks;
