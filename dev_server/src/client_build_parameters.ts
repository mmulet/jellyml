import {
  code_dir,
  client_src,
  docs_dir,
  templates_dir,
  data_dir,
} from "./directories";
import { markdown_transform } from "./markdown_transform";
import pug from "pug";
import { writeFileSync, readFileSync } from "fs";
import { resolve } from "path";
/**
 * Required by dev/build.js and server.ts
 */
export const client_build_parameters = {
  entryPoints: [`${client_src}/index.ts`],
  bundle: true,
  outdir: code_dir,
  sourcemap: true,
};

const python_example_args = {
  python_example_css: readFileSync(
    resolve(data_dir, "python_example.css"),
    "utf-8"
  ).toString(),
  python_example_html: readFileSync(
    resolve(data_dir, "python_example.html"),
    "utf-8"
  ).toString(),
};

export const client_pages = [
  {
    path: "./index.pug",
    out: "index.html",
    args: {
      ...python_example_args,
    },
  },
  {
    path: "./docs.pug",
    out: "docs.html",
    args: {
      ...python_example_args,
    },
  },

  { path: "./blog.pug", out: "blog.html", args: {} },
];

export const compile_and_save_templates = () => {
  client_pages.forEach(({ path, out, args }) => {
    const compiledFunction = pug.compileFile(resolve(templates_dir, path), {
      basedir: templates_dir,
      filters: {
        markdown: markdown_transform,
      },
    });
    writeFileSync(resolve(docs_dir, out), compiledFunction(args));
  });
};
