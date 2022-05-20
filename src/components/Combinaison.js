import { Checkbox, FormControlLabel, FormGroup } from "@mui/material";
import React, { useState } from "react";
import { getIndice } from "../api/api";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import Dataframe from "./cmp/Dataframe";
import "./styles/moyenMobile.css";
const listButtonText = ["MAX", "MIN"];

export default function Combinaison() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  const [option, setoption] = useState("");

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
      <div className="imp">
        <Combox
          name="MIN ou MAX"
          onChange={(val) => {
            setoption(val);
          }}
          data={listButtonText}
        />
      </div>
      <div>
        <FormGroup
          style={{
            display: "flex",
            flexDirection: "row",
          }}
        >
          <p
            style={{
              marginRight: 50,
            }}
          >
            Longueur
          </p>
          <FormControlLabel control={<Checkbox />} label="20" />
          <FormControlLabel control={<Checkbox />} label="50" />
          <FormControlLabel control={<Checkbox />} label="100" />
          <FormControlLabel control={<Checkbox />} label="200" />
          <FormControlLabel control={<Checkbox />} label="500" />
        </FormGroup>
      </div>
      <Button
        name="PLot"
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
