import axios from "axios";

// const API_URL = import.meta.env.API_URL;
const API_URL = "http://localhost:13001";
export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${API_URL}/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const processCSV = async () => {
  return axios.get(`${API_URL}/process_csv`);
};

export const anonymizeData = async () => {
  return axios.get(`${API_URL}/anonymise`);
};

export const maskProfanity = async () => {
  return axios.get(`${API_URL}/mask_profanity`);
};

export const classifyData = async () => {
  return axios.get(`${API_URL}/classify`);
};

export const downloadData = async () => {
  return axios.get(`${API_URL}/download`);
};

export const fetchResults = async () => {
  try {
    console.log("before fetch");
    return axios.get(`${API_URL}/read-data`);
    // return response;
    // setResults("Results will be displayed here")
  } catch (error) {
    console.error(error);
  }
};
