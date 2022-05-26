import React, { useState } from "react";
import Dataframe from "./cmp/Dataframe";
import "./styles/info.css";

export default function NivVar() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <Dataframe data={data} />
    </div>
  );
}
