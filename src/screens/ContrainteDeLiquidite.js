import React from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import "../components/styles/analyse.css";

export default function ContrainteDeLiquidite() {
  let navigate = useNavigate();

  return (
    <div className="analyse">
      <MyButton
        name="Strategie de cours cible"
        onClick={() => {
          navigate("/StratCoursCible");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/PortOpti3");
        }}
        name="Portefeuille optimal "
      />
    </div>
  );
}
