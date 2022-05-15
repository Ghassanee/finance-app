import { TextField } from "@mui/material";
import React, { useState } from "react";
import { actif } from "../data/actif";
import Button from "./Button";
import Combox from "./cmp/Combox";
import "./styles/info.css";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { MobileDatePicker } from "@mui/lab";
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
  const [name, setName] = React.useState("Cat in the Hat");
  const [dateDebut, setdateDebut] = useState(new Date());
  const [dateFin, setdateFin] = useState(new Date());
  const handleChange = (event) => {
    setName(event.target.value);
  };
  const handleChangedateDebut = (newValue) => {
    setdateDebut(newValue);
  };
  const handleChangedateFin = (newValue) => {
    setdateFin(newValue);
  };
  return (
    <div className="info">
      <Combox name="Selectionner actif " data={actif} />
      <div className="imp">
        <Combox name="Selectionner indiquateur" data={listButtonText} />
      </div>
      <TextField
        id="outlined-name"
        label="Prix de transaction"
        value={name}
        onChange={handleChange}
        className="date"
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <MobileDatePicker
          label="Date de debut"
          inputFormat="MM/dd/yyyy"
          value={dateDebut}
          onChange={handleChangedateDebut}
          renderInput={(params) => <TextField className="date" {...params} />}
        />
        <MobileDatePicker
          label="Date de fin"
          inputFormat="MM/dd/yyyy"
          value={dateFin}
          onChange={handleChangedateFin}
          renderInput={(params) => <TextField className="date" {...params} />}
        />
      </LocalizationProvider>
      <Button name="importer" />
      <div></div>
    </div>
  );
}
