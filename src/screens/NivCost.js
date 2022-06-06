import React, { useState } from "react";
import { PlotIndicateurMA } from "../api/api";
import Button from "../components/Button";
import MultiCheckbox from "../components/cmp/MultiCheckbox";
import "../components/styles/moyenMobile.css";
const dataCheckbox = ["Niveau deteremine", "Monte Carlo"];
export default function NivCost() {
  const [data, setdata] = useState(null);
  const [indices, setindices] = useState([]);
  const [actif] = useState("");
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
