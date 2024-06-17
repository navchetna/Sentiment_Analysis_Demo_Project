import axios from "axios";

// const API_URL = import.meta.env.API_URL;
const API_URL = "http://localhost:13001";
export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  console.log("sending POST request to /upload");
  return axios.post(`${API_URL}/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const processCSV = async () => {
  console.log("sending GET request to /process_csv");
  return axios.get(`${API_URL}/process_csv`);
};

export const anonymizeData = async () => {
  console.log("sending GET request to /anonymise");
  return axios.get(`${API_URL}/anonymise`);
};

export const maskProfanity = async () => {
  console.log("sending GET request to /mask_profanity");
  return axios.get(`${API_URL}/mask_profanity`);
};

export const classifyData = async () => {
  console.log("sending GET request to /classify");
  return axios.get(`${API_URL}/classify`);
};

export const downloadData = async () => {
  console.log("sending GET request to /download");
  return axios.get(`${API_URL}/download`);
};

export const fetchResults = async () => {
  try {
    console.log("sending GET request to /read-data");
    return axios.get(`${API_URL}/read-data`);
  } catch (error) {
    console.error(error);
  }
};
