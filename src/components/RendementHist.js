import React, { useState } from "react";
import { PlotHistogramme } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import "./styles/info.css";

export default function RendementHist() {
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
          data={actifs}
        />
      </div>
      <Button
        name="Plot"
        onClick={() => {
          PlotHistogramme(indice).then((res) => {
            setdata(res);
          });
        }}
      />
      <img src={data} alt="" />
    </div>
  );
}
