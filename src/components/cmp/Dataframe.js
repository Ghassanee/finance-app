import React from "react";
import "./dataframe.css";
export default function Dataframe(props) {
  return (
    <div className="table">
      {props.data &&
        Object.entries(props.data).map(([key, val], i) => (
          <div className="inline_p" key={i}>
            <p className="title">{key}</p>
            {Object.entries(val).map(([key, val], i) => (
              <p key={i + 10000}>{val}</p>
            ))}
          </div>
        ))}
    </div>
  );
}
