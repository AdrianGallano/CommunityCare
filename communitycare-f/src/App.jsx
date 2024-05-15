import { BrowserRouter, Route, Routes } from "react-router-dom";
import Map from "./components/Map";
import AddFamily from "./components/AddFamily";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element=<Map /> />
        <Route path="/create" element=<AddFamily /> />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
