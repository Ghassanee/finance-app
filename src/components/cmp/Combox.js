import { FormControl, InputLabel, MenuItem } from "@mui/material";
import { useEffect, useState } from "react";
import "./combox.css";
import Select from "@mui/material/Select";

export default function Combox(props) {
  const [val, setVal] = useState("");
  const [data, setData] = useState([]);
  const handleChange = (event) => {
    console.log(event.target.value);
    setVal(event.target.value);
    props.onChange(event.target.value);
  };

  useEffect(() => {
    let data = [];
    for (let index = 0; index < props.data.length; index++) {
      const element = props.data[index];
      data.push({
        id: index,
        label: element,
      });
    }
    setData(data);
  }, [props.data]);

  return (
    <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">{props.name} </InputLabel>
      <Select value={val} label={props.name} onChange={handleChange}>
        {data.map((val) => (
          <MenuItem key={val.id} value={val.label}>
            {val.label}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
