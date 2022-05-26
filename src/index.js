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
import ConstructeurDePortefeuille from "./components/ConstructeurDePortefeuille";
import PortefeuilleRisqueMinimum from "./components/PortefeuilleRisqueMinimum";
import PortOpti from "./components/PortOpti";
import Markowitz from "./components/Markowitz";
import PortMark from "./components/PortMark";
import FrontiereEfficiente from "./components/FrontiereEfficiente";
import ContrainteDePonderation from "./components/ContrainteDePonderation";
import RisqueMinimum from "./components/RisqueMinimum";
import PortOpti2 from "./components/PortOpti2";
import ContrainteDeLiquidite from "./components/ContrainteDeLiquidite";
import OPCVMActions from "./components/OPCVMActions";
import NivCost from "./components/NivCost";
import NivVar from "./components/NivVar";

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
        <Route
          path="ConstructeurDePortefeuille"
          element={<ConstructeurDePortefeuille />}
        />
        <Route path="matrice" element={<Matrice />} />
        <Route path="markowitz" element={<Markowitz />} />
        <Route
          path="PortefeuilleRisqueMinimum"
          element={<PortefeuilleRisqueMinimum />}
        />
        <Route path="PortOpti" element={<PortOpti />} />
        <Route path="PortMark" element={<PortMark />} />
        <Route path="FrontiereEfficiente" element={<FrontiereEfficiente />} />
        <Route
          path="ContrainteDePonderation"
          element={<ContrainteDePonderation />}
        />
        <Route
          path="ContrainteDeLiquidite"
          element={<ContrainteDeLiquidite />}
        />
        <Route path="OPCVM" element={<OPCVMActions />} />
        <Route path="NivCost" element={<NivCost />} />
        <Route path="NivVar" element={<NivVar />} />
        <Route path="RisqueMinimum" element={<RisqueMinimum />} />
        <Route path="PortOpti2" element={<PortOpti2 />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
