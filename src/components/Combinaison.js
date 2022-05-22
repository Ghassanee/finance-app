import React, { useState } from "react";
import { CombinaisonIndicateurs } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import MultiCheckbox from "./cmp/MultiCheckbox";
import "./styles/moyenMobile.css";
const listButtonText = ["MAX", "MIN"];
const dataCheckbox = [20, 50, 100, 200, 500];

export default function Combinaison() {
  const [data, setdata] = useState(null);
  const [indices, setindices] = useState([]);
  const [option, setoption] = useState("");
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
      <div className="imp">
        <Combox
          name="MIN ou MAX"
          onChange={(val) => {
            setoption(val);
          }}
          data={listButtonText}
        />
      </div>
      <MultiCheckbox
        dataCheckbox={dataCheckbox}
        onSelect={(val) => setindices(val)}
      />
      <Button
        name="PLot"
        onClick={() => {
          CombinaisonIndicateurs(actif, option, indices).then((res) => {
            setdata(res);
          });
        }}
      />
      <img src={data} alt="" />
    </div>
  );
}
