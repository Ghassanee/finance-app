import React, { useState } from "react";
import { PlotHistogramme } from "../api/api";
import { actifs } from "../data/actif";
import Button from "../components/Button";
import Combox from "../components/cmp/Combox";
import "../components/styles/info.css";

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
