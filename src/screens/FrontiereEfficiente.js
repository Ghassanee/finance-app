import React, { useEffect, useState } from "react";
import { Plot_Front_Effic } from "../api/api";
import Dataframe from "../components/cmp/Dataframe";
import "../components/styles/info.css";

export default function FrontiereEfficiente() {
  const [data, setdata] = useState(null);
  const [indice, setindice] = useState(null);
  useEffect(() => {
    Plot_Front_Effic().then((res) => {
      setdata(res);
    });
  }, []);
  return (
    <div className="info">
      <Dataframe data={data} />
    </div>
  );
}
