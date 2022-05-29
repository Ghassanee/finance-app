import React from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import "../components/styles/analyse.css";

export default function ContrainteDePonderation() {
  let navigate = useNavigate();

  return (
    <div className="analyse">
      <MyButton
        name="Risque minimum"
        onClick={() => {
          navigate("/RisqueMinimum");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/PortOpti2");
        }}
        name="Portefeuille optimal "
      />
    </div>
  );
}
