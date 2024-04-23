import React from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  LayersControl,
  ZoomControl,
  Popup,
} from "react-leaflet";
import { useMapEvents } from "react-leaflet/hooks";
import "leaflet/dist/leaflet.css";
import { useRef, useState } from "react";
import barangays from "./../data/barangays.json";
import { Icon } from "leaflet";
import pin from "./../assets/pin.png";
import CustomPopup from "./Popup";

export const icon = (url) => {
  return new Icon({
    iconUrl: url,
    iconSize: [24, 24],
  });
};

function LocationMarker({}) {
  const [position, setPosition] = useState(null);
  const map = useMapEvents({
    click() {
      map.locate({ enableHighAccuracy: true });
    },
    locationfound(e) {
      if (e.error) {
        console.error("Geolocation error:", e.error.message);
      } else {
        setTimeout(() => {
          setPosition(e.latlng);
          map.flyTo(e.latlng, map.getZoom(), { duration: 1 });
        }, 1000);
      }
    },
  });

  return position === null ? null : (
    <Marker position={position} icon={icon(pin)}></Marker>
  );
}

const GapoMap = () => {
  const mapRef = useRef();

  const config = {
    center: [14.831583808890002, 120.28337295677551],
    zoom: 15,
    scroll: true,
    zoomCtr: false,
  };

  const { BaseLayer } = LayersControl;

  return (
    <>
      <MapContainer
        center={config.center}
        zoom={config.zoom}
        scrollWheelZoom={config.scroll}
        zoomControl={config.zoomCtr}
        ref={mapRef}
        className="h-screen w-screen block absolute z-0"
      >
        <LocationMarker />
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
          <BaseLayer name="Terrain View">
            <TileLayer
              attribution="Gordon College | CCS"
              url="http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
              subdomains={["mt0", "mt1", "mt2", "mt3"]}
            />
          </BaseLayer>
          <BaseLayer name="Traffic View">
            <TileLayer
              attribution="Gordon College | CCS"
              url="https://{s}.google.com/vt/lyrs=m@221097413,traffic&x={x}&y={y}&z={z}"
              subdomains={["mt0", "mt1", "mt2", "mt3"]}
            />
          </BaseLayer>
        </LayersControl>
        <ZoomControl position="bottomright" />

        <div>
          {barangays.map(
            (barangay) =>
              barangay.gps && (
                <Marker
                  key={barangay.id}
                  position={[barangay.gps.latitude, barangay.gps.longitude]}
                  icon={icon(pin)}
                >
                  <Popup>
                    <CustomPopup barangay={barangay} />
                  </Popup>
                </Marker>
              )
          )}
        </div>
      </MapContainer>
    </>
  );
};

export default GapoMap;
