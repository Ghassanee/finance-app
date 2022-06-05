import { TextField } from "@mui/material";
import React, { useState } from "react";
import { actifs } from "../data/actif";
import Button from "../components/Button";
import "../components/styles/info.css";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { MobileDatePicker } from "@mui/lab";
import { CovarianceMatrice } from "../api/api";
import MultipleSelectChip from "../components/cmp/MultipleSelectChip";
import MultiCheckbox from "../components/cmp/MultiCheckbox";

export default function Matrice() {
  const [indices, setindices] = React.useState([]);
  const [dateDebutVal, setdateDebutVal] = useState(
    `${new Date().getFullYear()}-${String(new Date().getMonth() + 1).padStart(
      2,
      "0"
    )}-${String(new Date().getDate() + 1).padStart(2, "0")}`
  );
  const [dateDebut, setdateDebut] = useState(new Date());
  const [dateFinVal, setdateFinVal] = useState(
    `${new Date().getFullYear()}-${String(new Date().getMonth() + 1).padStart(
      2,
      "0"
    )}-${String(new Date().getDate() + 1).padStart(2, "0")}`
  );
  const [dateFin, setdateFin] = useState(new Date());

  const [data, setdata] = useState(null);
  const [val, setVal] = useState("non");

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
      <MultiCheckbox
        dataCheckbox={["Plot"]}
        onSelect={(val) => {
          setVal(val.length > 0 ? "Oui" : "Non");
        }}
      />
      <Button
        onClick={() => {
          CovarianceMatrice(indices, dateDebutVal, dateFinVal, val).then(
            (res) => {
              setdata(res);
            }
          );
        }}
        name="importer"
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
