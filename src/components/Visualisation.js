import React, { useState } from "react";
import Dataframe from "./cmp/Dataframe";
import "./styles/info.css";

export default function Visualisation() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <Dataframe data={data} />
    </div>
  );
}
