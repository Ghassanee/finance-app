import React, { useState } from "react";
import {
  Checkbox,
  FormControlLabel,
  FormGroup,
  FormLabel,
} from "@mui/material";
export default function MultiCheckbox(props) {
  const [indices, setindices] = useState([]);

  return (
    <FormGroup>
      <FormLabel component="legend" focused={false}>
        Longueur
      </FormLabel>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
        }}
      >
        {props.dataCheckbox.map((val, key) => (
          <FormControlLabel
            control={
              <Checkbox
                onChange={(event) => {
                  setindices((indices) => {
                    if (event.target.checked) {
                      let d = [...indices, val];
                      props.onSelect(d);
                      return d;
                    } else {
                      let d = indices.filter((x) => x !== val);
                      props.onSelect(d);
                      return d;
                    }
                  });
                }}
              />
            }
            key={key}
            label={val}
          />
        ))}
      </div>
    </FormGroup>
  );
}
