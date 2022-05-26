import React, { useState } from "react";
import { PlotIndicateurMA } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import MultiCheckbox from "./cmp/MultiCheckbox";
import "./styles/moyenMobile.css";
const dataCheckbox = ["Niveau deteremine", "Monte Carlo"];
export default function NivCost() {
  const [data, setdata] = useState(null);
  const [indices, setindices] = useState([]);
  const [actif, setactif] = useState("");
  return (
    <div className="info">
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
      <img
        style={{
          height: 300,
        }}
        src={"data:image/png;base64," + data}
        alt=""
      />
    </div>
  );
}
