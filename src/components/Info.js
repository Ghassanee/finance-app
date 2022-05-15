import React from "react";
import { actif } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import "./styles/info.css";
const listButtonText = [
  "Meilleure limite",
  "Donnees seance",
  "Donnee seance precedente",
  "Derniere transaction",
  "Info societe",
  "Plus forte hausse",
  "Plus forte baisse",
  "Actionnaire",
  "Ratio",
  "Dir",
];
export default function Info() {
  return (
    <div className="info">
      <Combox name="Selectionner votre actif " data={actif} />
      <div className="imp">
        <Combox name="Selectionner votre option" data={listButtonText} />
      </div>
      <Button name="importer" />
      <div></div>
    </div>
  );
}
