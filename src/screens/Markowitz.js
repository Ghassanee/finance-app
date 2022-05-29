import React from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import "../components/styles/analyse.css";

export default function Markowitz() {
  let navigate = useNavigate();

  return (
    <div className="analyse">
      <MyButton
        name="Portefeuille risque minimum"
        onClick={() => {
          navigate("/PortefeuilleRisqueMinimum");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/PortOpti");
        }}
        name="Portefeuille optimal pour un niveau de rendement"
      />
      <MyButton
        onClick={() => {
          navigate("/PortMark");
        }}
        name="Portefeuille de marche"
      />
      <MyButton
        name="Frontiere efficiente"
        onClick={() => {
          navigate("/FrontiereEfficiente");
        }}
      />
    </div>
  );
}
