import React, { useEffect, useState } from "react";
import axios from "axios";
import TableBasic from "../Tables/TableBasic";

const Result = ({ results }) => {
  if (!results || results.length === 0) {
    return <div>No results</div>;
  }

  const { text, Anonymized_Text, Masked_Text, Classification_Result } =
    results[0];

  return (
    <div>
      <div>
        <TableBasic data={results} />
      </div>
    </div>
  );
};

export default Result;
