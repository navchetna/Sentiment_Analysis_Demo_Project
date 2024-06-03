import React, { useState } from "react";
import UploadComponent from "./components/Custom/Upload";
import Result from "./components/Custom/Result";
import {
  processCSV,
  anonymizeData,
  maskProfanity,
  classifyData,
  downloadData,
  fetchResults,
} from "./components/Custom/APIService";

const App = () => {
  const [uploaded, setUploaded] = useState(false);
  const [results, setResults] = useState([]);

  const handleProcess = async () => {
    const process_res = await processCSV();
    console.log("process_res: ", process_res);
    // await anonymizeData();
    await maskProfanity();
    await classifyData();
    const res = await fetchResults();
    console.log("res.data: ", res.data);
    setResults(res.data);
    setUploaded(true);
  };

  return (
    <div className="flex flex-col align-center justify-center m-10 p-10">
      <h1>Sentiment Analysis on Google Reviews</h1>
      <div className="flex flex-col justify-center mt-5">
        <UploadComponent />
      </div>
      {<button onClick={handleProcess} className="w-40 mt-5">Process File</button>}
      {uploaded && <Result results={results} />}
    </div>
  );
};

export default App;
