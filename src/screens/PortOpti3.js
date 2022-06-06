/* eslint-disable no-unused-vars */
import { TextField } from "@mui/material";
import React, { useState } from "react";
import { actifs } from "../data/actif";
import Button from "../components/Button";
import "../components/styles/info.css";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { MobileDatePicker } from "@mui/lab";
import { CovarianceMatrice } from "../api/api";

export default function PortOpti3() {
  const [indices, setindices] = React.useState("");
  const [indice1, setindice1] = React.useState("");
  const [indice2, setindice2] = React.useState("");
  const [indice3, setindice3] = React.useState("");
  const [dateDebutVal, setdateDebutVal] = useState("2022-05-17");
  const [dateDebut, setdateDebut] = useState(new Date());
  const [dateFinVal, setdateFinVal] = useState("2022-05-17");
  const [dateFin, setdateFin] = useState(new Date());
  const [data, setdata] = useState(null);

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
      <TextField
        id="outlined-name"
        label="Esperance de rendement"
        value={indice1}
        onChange={(val) => setindice1(val)}
      />
      <TextField
        id="outlined-name"
        label="Taux sans risque"
        value={indice2}
        onChange={(val) => setindice2(val)}
        style={{
          marginTop: 30,
        }}
      />
      <TextField
        id="outlined-name"
        label="Taux sans risque"
        value={indice3}
        onChange={(val) => setindice3(val)}
        style={{
          marginTop: 30,
        }}
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <MobileDatePicker
          label="Date de debut"
          inputFormat="yyyy/MM/dd"
          value={dateDebut}
          onChange={handleChangedateDebut}
          renderInput={(params) => <TextField className="date1" {...params} />}
        />
        <MobileDatePicker
          label="Date de fin"
          inputFormat="yyyy/MM/dd"
          value={dateFin}
          onChange={handleChangedateFin}
          renderInput={(params) => <TextField className="date1" {...params} />}
        />
      </LocalizationProvider>

      <Button
        onClick={() => {
          CovarianceMatrice(indices, dateDebutVal, dateFinVal).then((res) => {
            setdata(res);
          });
        }}
        name="importer"
      />
      <Button
        onClick={() => {
          CovarianceMatrice(indices, dateDebutVal, dateFinVal).then((res) => {
            setdata(res);
          });
        }}
        name="Backtest"
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
