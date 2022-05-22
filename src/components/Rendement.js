import React, { useState } from "react";
import { PlotActifLine } from "../api/api";
import Button from "./Button";
import MultipleSelectChip from "./cmp/MultipleSelectChip";
import "./styles/info.css";
import { actifs } from "../data/actif";

export default function Rendement() {
  const [data, setdata] = useState(null);
  const [indices, setindices] = useState(null);
  return (
    <div className="info">
      <MultipleSelectChip
        names={actifs}
        setIndices={(val) => setindices(val)}
      />
      <Button
        name="importer"
        onClick={() => {
          PlotActifLine(indices).then((res) => {
            setdata(res);
          });
        }}
      />
      <img src={data} alt="" />
    </div>
  );
}
