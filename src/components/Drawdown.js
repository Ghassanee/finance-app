import React, { useState } from "react";
import { getInfo } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import Dataframe from "./cmp/Dataframe";
import "./styles/info.css";
const listButtonText = ["MAX", "MIN"];

export default function Drawdown() {
  const [data, setdata] = useState(null);
  const [actif, setactif] = useState("");
  const [option, setoption] = useState("");

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
            setoption(val);
          }}
          data={listButtonText}
        />
      </div>
      <Button
        name="importer"
        onClick={() => {
          getInfo(actif, option).then((res) => {
            setdata(res);
          });
        }}
      />
      <Dataframe data={data} />
    </div>
  );
}
