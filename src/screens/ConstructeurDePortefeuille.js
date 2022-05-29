import React from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import "../components/styles/analyse.css";

export default function ConstructeurDePortefeuille() {
  let navigate = useNavigate();

  return (
    <div className="analyse">
      <MyButton
        name="Markowitz"
        onClick={() => {
          navigate("/markowitz");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/ContrainteDePonderation");
        }}
        name="Contrainte de ponderation"
      />
      <MyButton
        onClick={() => {
          navigate("/ContrainteDeLiquidite");
        }}
        name="Contrainte de liquidite"
      />
      <MyButton
        name="OPCVM Actions"
        onClick={() => {
          navigate("/OPCVM");
        }}
      />
    </div>
  );
}
