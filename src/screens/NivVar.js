import React, { useState } from "react";
import Dataframe from "../components/cmp/Dataframe";
import "../components/styles/info.css";

export default function NivVar() {
  const [data] = useState(null);
  // const [indice, setindice] = useState(null);
  return (
    <div className="info">
      <Dataframe data={data} />
    </div>
  );
}
