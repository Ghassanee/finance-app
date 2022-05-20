import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Info from "./components/Info";
import Indices from "./components/Indices";
import IndicateurDeLiquidte from "./components/IndicateurDeLiquidte";
import Login from "./components/Login";
import Analyse from "./components/Analyse";
import Visualisation from "./components/Visualisation";
import MoyenMobile from "./components/MoyenMobile";
import Drawdown from "./components/Drawdown";
import Combinaison from "./components/Combinaison";
import Rendement from "./components/Rendement";
import RendementHist from "./components/RendementHist";
import Risque from "./components/Risque";
import Matrice from "./components/Matrice";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
        <Route path="info" element={<Info />} />
        <Route path="indices" element={<Indices />} />
        <Route path="indicateurDeLiquidte" element={<IndicateurDeLiquidte />} />
        <Route path="analyse" element={<Analyse />} />
        <Route path="visualisation" element={<Visualisation />} />
        <Route path="moyenmobile" element={<MoyenMobile />} />
        <Route path="drawdown" element={<Drawdown />} />
        <Route path="combinaison" element={<Combinaison />} />
        <Route path="rendement" element={<Rendement />} />
        <Route path="rendementHist" element={<RendementHist />} />
        <Route path="risque" element={<Risque />} />
        <Route path="matrice" element={<Matrice />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
