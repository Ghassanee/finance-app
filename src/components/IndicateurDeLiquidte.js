import { TextField } from "@mui/material";
import React, { useState } from "react";
import { actifs } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import "./styles/info.css";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { MobileDatePicker } from "@mui/lab";
import { getIndicatorDeLiquidity } from "../api/api";
import Dataframe from "./cmp/Dataframe";
const listButtonText = [
  "Fourchette affichee",
  "Prix moyen",
  "Fourchette relative",
  "Fourchette effective relative",
  "Corwin",
  "Quant_moy",
  "LIX",
];

export default function IndicateurDeLiquidte() {
  const [price, setprice] = React.useState("0");
  const [actif, setactif] = React.useState("");
  const [indiquateur, setindiquateur] = React.useState("");
  const [dateDebut, setdateDebut] = useState(new Date());
  const [dateFin, setdateFin] = useState(new Date());
  const [data, setdata] = useState(null);
  const handleChange = (event) => {
    setprice(event.target.value);
  };
  const handleChangedateDebut = (newValue) => {
    setdateDebut(newValue);
  };
  const handleChangedateFin = (newValue) => {
    setdateFin(newValue);
  };
  return (
    <div className="info">
      <Combox
        onChange={(val) => {
          setactif(val);
        }}
        name="Selectionner actif "
        data={actifs}
      />
      <div className="imp">
        <Combox
          onChange={(val) => {
            setindiquateur(val);
          }}
          name="Selectionner indiquateur"
          data={listButtonText}
        />
      </div>
      <TextField
        id="outlined-name"
        label="Prix de transaction"
        value={price}
        type="number"
        onChange={handleChange}
        className="date"
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <MobileDatePicker
          label="Date de debut"
          inputFormat="yyyy/MM/dd"
          value={dateDebut}
          onChange={handleChangedateDebut}
          renderInput={(params) => <TextField className="date" {...params} />}
        />
        <MobileDatePicker
          label="Date de fin"
          inputFormat="yyyy/MM/dd"
          value={dateFin}
          onChange={handleChangedateFin}
          renderInput={(params) => <TextField className="date" {...params} />}
        />
      </LocalizationProvider>
      <Button
        onClick={() => {
          getIndicatorDeLiquidity(
            actif,
            indiquateur,
            price,
            dateDebut,
            dateFin
          ).then((res) => {
            setdata(res);
          });
        }}
        name="importer"
      />
      <Dataframe data={data} />
    </div>
  );
}
