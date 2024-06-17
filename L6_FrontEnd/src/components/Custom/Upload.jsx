import React, { useState } from "react";
import axios from "axios";
import { Upload, Button } from "antd";
import { PlusOutlined } from "@ant-design/icons";

const UploadComponent = () => {
  const [fileList, setFileList] = useState([]);
  const API_URL = import.meta.env.API_URL;

  const handleChange = ({ fileList }) => setFileList(fileList);

  const handleUpload = async () => {
    const formData = new FormData();
    fileList.forEach((file) => {
      formData.append("file", file.originFileObj);
    });

    try {
      console.log("sending POST request to /upload");
      const response = await axios.post(
        `http://localhost:13001/upload`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log(response.data);
      // Handle the response as needed
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex flex-row w-48 items-center justify-items-center">
      <Upload
        listType="picture-card"
        fileList={fileList}
        onChange={handleChange}
        style={{
          display: "flex",
          flexDirection: "column",
        }}
      >
        <div>
          <PlusOutlined style={{ color: "white" }} />
          <div style={{ marginTop: 8, color: "white" }}>Add files</div>
        </div>
      </Upload>
      <Button
        style={{ color: fileList.length === 0 ? "grey" : "black" }}
        onClick={handleUpload}
        disabled={fileList.length === 0}
      >
        Upload
      </Button>
    </div>
  );
};

export default UploadComponent;
