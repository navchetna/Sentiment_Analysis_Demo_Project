import React from "react";
import ReactPlayer from "react-player/lazy";

export const VideoPlayer = ({ videoURL }) => {
  return (
    <>
      <div className="m-5 p-2 border border border-slate-500 w-fit rounded-md">
        <ReactPlayer url={videoURL} />
      </div>
    </>
  );
};
