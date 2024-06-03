import { useMemo } from "react";

export const useColumns = () =>
  useMemo(
    () => [
      {
        accessorKey: "text",
        header: "Text",
        size: 530,
      },
      {
        accessorKey: "Anonymized_Text",
        header: "Anonymized Text",
        size: 530,
      },
      {
        accessorKey: "Masked_Text",
        header: "Masked Text",
        size: 530,
      },
      {
        accessorKey: "Classification_Result",
        header: "Classification Result",
        size: 150,
      },
    ],
    []
  );
