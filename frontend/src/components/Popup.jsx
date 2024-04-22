import React from "react";

const Popup = ({ barangay }) => {
  return (
    <div>
      <h2>{barangay.name}</h2>
      <p>Latitude: {barangay.gps.latitude}</p>
      <p>Longitude: {barangay.gps.longitude}</p>
    </div>
  );
};

export default Popup;
