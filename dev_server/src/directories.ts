import { resolve } from "path";

export const project_dir = resolve(__dirname, "../../");

export const client_dir = resolve(project_dir, "./client");
export const server_dir = resolve(project_dir, "./dev_server");
export const server_dev = resolve(server_dir, "./dev");


export const client_src = resolve(client_dir, "./src");
export const docs_dir = resolve(project_dir, "./docs");
export const client_static = resolve(docs_dir, "./static");
export const code_dir = resolve(docs_dir, "./code");

export const templates_dir = resolve(client_dir, "./templates");
export const data_dir = resolve(server_dir, "./data");
