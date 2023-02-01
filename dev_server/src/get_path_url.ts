import { Request } from "express";

export const get_path_url = (req: Request, port: number): URL => {
  const url = new URL(req.url, `http://localhost:${port}`);
  url.pathname = url.pathname.replace(/\/$/, "/index.html");
  return url;
};
