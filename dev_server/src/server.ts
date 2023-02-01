import express from "express";
const app = express();
const port = 8903;
import {
  client_static,
  docs_dir,
  templates_dir,
  code_dir,
} from "./directories";
import { build } from "esbuild";
import { setup_reload_handler } from "./handle_reload";
import open from "open";
import {
  client_build_parameters,
  compile_and_save_templates,
} from "./client_build_parameters";
import { get_path_url } from "./get_path_url";
import { BuildStatus } from "./BuildStatus";
import { watch } from "fs";
import { client_pages } from "./client_build_parameters";

app.use("/code", express.static(code_dir));

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

app.use("/static", express.static(client_static));

const pages = ["/"].concat(client_pages.map((page) => `/${page.out}`));
if (process.env.DEV !== "1") {
  for (const page of pages) {
    app.get(page, (req, res) => {
      const url = get_path_url(req, port);
      res.sendFile(`${docs_dir}${url.pathname}`);
    });
  }
} else {
  const reload_handler = setup_reload_handler(app, pages, port);
  const build_status = new BuildStatus();
  build({
    ...client_build_parameters,
    watch: {
      onRebuild(error) {
        if (error) {
          return;
        }
        console.clear();
        build_status.print_build_number();

        reload_handler.causeReload();
      },
    },
  }).then((_result) => {
    //watching

    if (process.env.NO_OPEN !== "1") {
      open(`http://localhost:${port}`);
    }
  });
  watch(templates_dir, { recursive: true }, () => {
    compile_and_save_templates();
    reload_handler.causeReload();
  });
}
