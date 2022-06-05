import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Info from "./screens/Info";
import Indices from "./screens/Indices";
import IndicateurDeLiquidte from "./screens/IndicateurDeLiquidte";
import Login from "./screens/Login";
import Analyse from "./screens/Analyse";
import Visualisation from "./screens/Visualisation";
import MoyenMobile from "./screens/MoyenMobile";
import Drawdown from "./screens/Drawdown";
import Combinaison from "./screens/Combinaison";
import Rendement from "./screens/Rendement";
import RendementHist from "./screens/RendementHist";
import Risque from "./screens/Risque";
import Matrice from "./screens/Matrice";
import ConstructeurDePortefeuille from "./screens/ConstructeurDePortefeuille";
import PortefeuilleRisqueMinimum from "./screens/PortefeuilleRisqueMinimum";
import PortOpti from "./screens/PortOpti";
import Markowitz from "./screens/Markowitz";
import PortMark from "./screens/PortMark";
import FrontiereEfficiente from "./screens/FrontiereEfficiente";
import ContrainteDePonderation from "./screens/ContrainteDePonderation";
import RisqueMinimum from "./screens/RisqueMinimum";
import PortOpti2 from "./screens/PortOpti2";
import PortOpti3 from "./screens/PortOpti3";
import ContrainteDeLiquidite from "./screens/ContrainteDeLiquidite";
import OPCVMActions from "./screens/OPCVMActions";
import NivCost from "./screens/NivCost";
import NivVar from "./screens/NivVar";
import StratCoursCible from "./screens/StratCoursCible";
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
        <Route path="StratCoursCible" element={<StratCoursCible />} />
        <Route path="NivCost" element={<NivCost />} />
        <Route path="NivVar" element={<NivVar />} />
        <Route path="RisqueMinimum" element={<RisqueMinimum />} />
        <Route path="PortOpti2" element={<PortOpti2 />} />
        <Route path="PortOpti3" element={<PortOpti3 />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
