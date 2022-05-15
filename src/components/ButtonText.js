import React from "react";
import Button from "./Button";
import "./styles/buttontext.css";
export default function ButtonText(props) {
  return (
    <div className="buttonText">
      <div>{props.name} </div>
      <Button name="Calculer" />
    </div>
  );
}
