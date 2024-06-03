import { useEffect, useMemo, useState } from "react";
import {
  MaterialReactTable,
  useMaterialReactTable,
} from "material-react-table";
// import data from "../../config/TableDataConfig";
import { useColumns } from "../../hooks/useColumns";
// import { writeData } from "../../actions/writeData";

const TableBasic = ({ data }) => {
  const columns = useColumns();

  const table = useMaterialReactTable({
    columns,
    data, //data must be memoized or stable (useState, useMemo, defined outside of this component, etc.)
  });

  return (
    <>
      <div className="flex flex-col justify-center items-center">
        <MaterialReactTable table={table} />
        {/* <button onClick={readData}>Fetch Data</button> */}
        {/* <button onClick={writeData}>Write Data</button> */}
      </div>
    </>
  );
};

export default TableBasic;
