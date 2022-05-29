import React from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import "../components/styles/analyse.css";

export default function Analyse() {
  let navigate = useNavigate();

  return (
    <div className="analyse">
      <MyButton
        name="Visualisation prix"
        onClick={() => {
          navigate("/visualisation");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/drawdown");
        }}
        name="Draw Down"
      />
      <MyButton
        onClick={() => {
          navigate("/rendement");
        }}
        name="Rendement"
      />
      <MyButton
        name="Risque"
        onClick={() => {
          navigate("/risque");
        }}
      />
      <MyButton
        name="Moyenne Mobile"
        onClick={() => {
          navigate("/moyenmobile");
        }}
      />
      <MyButton
        name="Combinaison MA/DD"
        onClick={() => {
          navigate("/combinaison");
        }}
      />
      <MyButton
        name="Rendement en histogramme"
        onClick={() => {
          navigate("/rendementHist");
        }}
      />
      <MyButton
        name="Matrice Var/Covar"
        onClick={() => {
          navigate("/matrice");
        }}
      />
    </div>
  );
}
