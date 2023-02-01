import express, { Request, Response } from "express";
import { readFileSync } from "fs";
import { JSDOM } from "jsdom";
import { docs_dir, server_dev } from "./directories";
import { get_path_url } from "./get_path_url";

const reloadPath = "reload";

const inject_reload_script = readFileSync(
  server_dev + "/injectReload.js",
  "utf8"
).toString();

class Reload_Handler {
  reloadNumber = 0;
  causeReload = () => {
    this.reloadNumber++;
  };
  injectReloaderIntoHTML = (port: number) => (req: Request, res: Response) => {
    const url = get_path_url(req, port);
    JSDOM.fromFile(`${docs_dir}${url.pathname}`).then((dom) => {
      const scriptElem = dom.window.document.createElement("script");
      scriptElem.text = inject_reload_script
        .replace("replaceReloadNumber", this.reloadNumber.toString())
        .replace("replaceReloadPath", reloadPath);
      dom.window.document.querySelector("body")!.appendChild(scriptElem);
      res.set("Content-Type", "text/html");
      res.send(dom.serialize());
    });
  };
}

export const setup_reload_handler = (
  app: express.Application,
  get_paths: string[],
  port: number
): Reload_Handler => {
  const reload_handler = new Reload_Handler();
  for (const path of get_paths) {
    app.get(path, reload_handler.injectReloaderIntoHTML(port));
  }

  app.get(`/${reloadPath}`, (_req, res) => {
    res.setHeader("Content-Type", "text/plain");
    //set header so that it won't cache
    res.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
    res.send(reload_handler.reloadNumber.toString());
  });
  return reload_handler;
};
