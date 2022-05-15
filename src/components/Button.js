import { Button } from "@mui/material";
import React from "react";

export default function MyButton(props) {
  return (
    <Button
      style={{
        margin: 16,
        fontSize: 20,
      }}
      variant="outlined"
      size="large"
      {...props}
    >
      {props.name}
    </Button>
  );
}
