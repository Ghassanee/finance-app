import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import MyButton from "../components/Button";
import bmce_capital from "../assets/bmce_capital.png";
import ifa from "../assets/ifa.png";
import Noo from "../assets/bmce_capital.png";
import "../components/styles/menu.css";
import { getCookie } from "../data/cookies";
export default function Menu() {
  let navigate = useNavigate();
  useEffect(() => {
    if (!getCookie("loggedin")) {
      navigate("/login");
    }
  });

  return (
    <div className="menu">
      <div className="imgs">
        <img src={bmce_capital} alt="" />
        <img src={ifa} alt="" />
        <img src={Noo} alt="" />
      </div>
      <MyButton
        name="Analyse"
        onClick={() => {
          navigate("/analyse");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/ConstructeurDePortefeuille");
        }}
        name="Constructeur de portefeuille"
      />
      <MyButton
        name="Info"
        onClick={() => {
          navigate("/info");
        }}
      />
      <MyButton
        onClick={() => {
          navigate("/indicateurDeLiquidte");
        }}
        name="Indicateur de liquidite"
      />
      <MyButton
        onClick={() => {
          navigate("/indices");
        }}
        name="Indices"
      />
    </div>
  );
}
