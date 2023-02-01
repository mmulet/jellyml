const { buildSync } = require("esbuild");

/**build the server code */
buildSync({
  entryPoints: ["src/server.ts"],
  bundle: true,
  outdir: "build",
  platform: "node",
  target: "node18",
  sourcemap: true,
  external: ["express", "esbuild", "jsdom", "open"],
});
/**convert the client build parameters to javascript
 * then require it and pass it to the buildSync function
 */
const result = buildSync({
  entryPoints: ["src/client_build_parameters.ts"],
  bundle: true,
  write: false,
  platform: "node",
  target: "node18",
  external: ["express", "esbuild", "jsdom", "open"],
});

const m = new module.constructor();
m.paths = module.paths;
m._compile(result.outputFiles[0].text, "src/client_build_parameters.ts");
/**build the client code */
buildSync(m.exports.client_build_parameters);
/**
 * compile the pug templates and save them
 */
m.exports.compile_and_save_templates();
