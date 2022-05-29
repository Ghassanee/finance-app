import React, { useState } from "react";
import { PlotIndicateurDrawdown } from "../api/api";
import { actifs } from "../data/actif";
import Button from "../components/Button";
import Combox from "../components/cmp/Combox";
import "../components/styles/info.css";
const listButtonText = ["MAX", "MIN"];

export default function Drawdown() {
  const [data, setdata] = useState(null);
  const [actif, setactif] = useState("");
  const [tp, setTp] = useState("");

  return (
    <div className="info">
      <Combox
        name="Selectionner votre actif "
        onChange={(val) => {
          setactif(val);
        }}
        data={actifs}
      />
      <div className="imp">
        <Combox
          name="MIN ou MAX"
          onChange={(val) => {
            setTp(val);
          }}
          data={listButtonText}
        />
      </div>
      <Button
        name="importer"
        onClick={() => {
          PlotIndicateurDrawdown(actif, tp).then((res) => {
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
