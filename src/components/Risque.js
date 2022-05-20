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

export default function Risque() {
  const [price, setprice] = React.useState("0");
  const [actif, setactif] = React.useState("");
  const [indiquateur, setindiquateur] = React.useState("");
  const [dateDebutVal, setdateDebutVal] = useState("2022-05-17");
  const [dateDebut, setdateDebut] = useState(new Date());
  const [dateFinVal, setdateFinVal] = useState("2022-05-17");
  const [dateFin, setdateFin] = useState(new Date());
  const [data, setdata] = useState(null);
  const handleChange = (event) => {
    setprice(event.target.value);
  };
  const handleChangedateDebut = (newValue) => {
    setdateDebut(newValue);
    setdateDebutVal(
      `${newValue.getFullYear()}-${String(newValue.getMonth() + 1).padStart(
        2,
        "0"
      )}-${String(newValue.getDate() + 1).padStart(2, "0")}`
    );
  };
  const handleChangedateFin = (newValue) => {
    setdateFin(newValue);
    setdateFinVal(
      `${newValue.getFullYear()}-${String(newValue.getMonth() + 1).padStart(
        2,
        "0"
      )}-${String(newValue.getDate() + 1).padStart(2, "0")}`
    );
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
            dateDebutVal,
            dateFinVal
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
