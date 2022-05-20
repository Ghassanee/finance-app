import React, { useState } from "react";
import { getIndice } from "../api/api";
import Button from "./Button";
import MultipleSelectChip from "./cmp/MultipleSelectChip";
import Dataframe from "./cmp/Dataframe";
import "./styles/info.css";
import { actifs } from "../data/actif";

export default function Rendement() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <div className="imp">
        <MultipleSelectChip names={actifs} />
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
