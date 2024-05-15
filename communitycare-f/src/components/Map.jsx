import React, { useMemo, useState, useRef, useEffect } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  LayersControl,
  ZoomControl,
  Popup,
  useMapEvents,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import barangays from "./../data/barangays.json";
import { Icon } from "leaflet";
import pin from "./../assets/pin.png";
import CustomPopup from "./Popup";
import MarkerClusterGroup from "react-leaflet-cluster";
import axios from "axios";
import AddFamilyForm from "./AddFamily";

const Map = () => {
  const [coordinates, setCoordinates] = useState(null);
  const [families, setFamilies] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:3000/family")
      .then((res) => setFamilies(res.data))
      .catch((err) => console.log(err));
  }, []);

  const mapRef = useRef();
  const { BaseLayer } = LayersControl;
  const [showMarkers, setShowMarkers] = useState(true);

  const icon = useMemo(
    () =>
      new Icon({
        iconUrl: pin,
        iconSize: [24, 24],
      })
  );

  const handleClick = (event) => {
    console.log("Clicked Coordinates:", event.latlng);
    setCoordinates(event.latlng);
  };

  const toggleMarkers = () => {
    setShowMarkers((prevShowMarkers) => !prevShowMarkers);
  };

  return (
    <>
      <main className="grid grid-cols-2 my-4 gap-2 h-screen z-0 relative">
        <AddFamilyForm coordinates={coordinates} />
        <button
          onClick={toggleMarkers}
          className=" absolute top-4 left-4 z-99999 text-white bg-gray-800 hover:bg-gray-900  font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
        >
          {showMarkers ? "Hide Markers" : "Show Markers"}
        </button>
        <div className="w-full h-screen relative m-4">
          <MapContainer
            center={[14.831583808890002, 120.28337295677551]}
            zoom={10}
            scrollWheelZoom={true}
            zoomControl={false}
            ref={mapRef}
            className="h-screen w-full"
          >
            <LayersControl>
              <BaseLayer checked name="OpenStreetMap View">
                <TileLayer
                  attribution="Gordon College | CCS"
                  url="http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
                  subdomains={["mt0", "mt1", "mt2", "mt3"]}
                />
              </BaseLayer>
              <BaseLayer name="Hybrid View">
                <TileLayer
                  attribution="Gordon College | CCS"
                  url="http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}"
                  subdomains={["mt0", "mt1", "mt2", "mt3"]}
                />
              </BaseLayer>
            </LayersControl>

            <ZoomControl position="bottomright" />
            <MapClickHandler onClick={handleClick} />

            <MarkerClusterGroup chunkedLoading>
              {showMarkers &&
                barangays.map(
                  (barangay) =>
                    barangay.gps && (
                      <Marker
                        key={barangay.id}
                        position={[
                          barangay.gps.latitude,
                          barangay.gps.longitude,
                        ]}
                        icon={icon}
                      >
                        <Popup>
                          <CustomPopup
                            className="relative -top-5"
                            barangay={barangay}
                          />
                        </Popup>
                      </Marker>
                    )
                )}
            </MarkerClusterGroup>

            <MarkerClusterGroup chunkedLoading>
              {showMarkers &&
                families.map((family) => (
                  <Marker
                    key={family.family_id}
                    position={[
                      family.coordinates.latitude,
                      family.coordinates.longitude,
                    ]}
                    icon={icon}
                  >
                    <Popup>
                      <div>
                        <h3>{family.family_name}</h3>
                        <p>
                          {family.address.street}, {family.address.city},{" "}
                          {family.address.state} {family.address.zipcode}
                        </p>
                        <h4>Members:</h4>
                        <ul>
                          {family.members.map((member) => (
                            <li key={member.id}>
                              {member.name} - {member.age} years old
                            </li>
                          ))}
                        </ul>
                      </div>
                    </Popup>
                  </Marker>
                ))}
            </MarkerClusterGroup>
          </MapContainer>
        </div>
      </main>
    </>
  );
};

const MapClickHandler = ({ onClick }) => {
  useMapEvents({
    click: (e) => {
      onClick(e);
    },
  });
  return null;
};

export default Map;
