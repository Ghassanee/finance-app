import { TextField } from "@mui/material";
import React, { useState } from "react";
import { actifs } from "../data/actif";
import Button from "./Button";
import "./styles/info.css";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { MobileDatePicker } from "@mui/lab";
import { CovarianceMatrice } from "../api/api";
import MultipleSelectChip from "./cmp/MultipleSelectChip";

export default function Matrice() {
  const [indices, setindices] = React.useState([]);
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
      <MultipleSelectChip
        names={actifs}
        setIndices={(val) => setindices(val)}
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
      <img src={data} alt="" />
    </div>
  );
}
