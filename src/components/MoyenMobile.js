import React, { useState } from "react";
import { PlotIndicateurMA } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import MultiCheckbox from "./cmp/MultiCheckbox";
import "./styles/moyenMobile.css";
const dataCheckbox = [20, 50, 100, 200, 500];
export default function MoyenMobile() {
  const [data, setdata] = useState(null);
  const [indices, setindices] = useState([]);
  const [actif, setactif] = useState("");
  return (
    <div className="info">
      <div className="imp">
        <Combox
          onChange={(val) => {
            setactif(val);
          }}
          name="Choisir l'indice"
          data={actifs}
        />
      </div>
      <MultiCheckbox
        dataCheckbox={dataCheckbox}
        onSelect={(val) => setindices(val)}
      />
      <Button
        name="PLot"
        onClick={() => {
          PlotIndicateurMA(actif, indices).then((res) => {
            setdata(res);
          });
        }}
      />
      <img src={data} alt="" />
    </div>
  );
}
