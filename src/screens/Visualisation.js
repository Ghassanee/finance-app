import React, { useState } from "react";
import { PlotActifLine } from "../api/api";
import Button from "../components/Button";
import Combox from "../components/cmp/Combox";
import "../components/styles/info.css";
import { actifs } from "../data/actif.js";
export default function Visualisation() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <Combox
        onChange={(val) => {
          setindice(val);
        }}
        name="Choisir l'indice"
        data={actifs}
      />
      <Button
        name="PLot"
        onClick={() => {
          PlotActifLine(indice).then((res) => {
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
