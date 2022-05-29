import React, { useState } from "react";
import { getIndice } from "../api/api";
import Button from "../components/Button";
import Combox from "../components/cmp/Combox";
import Dataframe from "../components/cmp/Dataframe";
import "../components/styles/info.css";
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
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <div className="imp">
        <Combox
          onChange={(val) => {
            setindice(val);
          }}
          name="Choisir l'indice"
          data={listButtonText}
        />
      </div>
      <Button
        name="importer"
        onClick={() => {
          getIndice(indice).then((res) => {
            setdata(res);
          });
        }}
      />
      <Dataframe data={data} />
    </div>
  );
}
