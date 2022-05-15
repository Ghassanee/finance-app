import React from "react";
import Button from "./Button";
import Combox from "./cmp/Combox";
import "./styles/info.css";
const listButtonText = [
  "Indice",
  "Volume Global",
  "Plus forte hausse",
  "Plus forte baisse",
  "Resume indice",
  "Indice rentabilite",
  "Indices en devises",
  "Indice FTSE",
  "poids",
];
export default function Indices() {
  return (
    <div className="info">
      <div className="imp">
        <Combox name="Choisir l'indice" data={listButtonText} />
      </div>
      <Button name="importer" />
      <div></div>
    </div>
  );
}
