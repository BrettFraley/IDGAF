import {nodeResolve} from "@rollup/plugin-node-resolve"
export default {
  input: "./code-mirror-editor.mjs",
  output: {
    file: "./editor.bundle.js",
    format: "iife"
  },
  plugins: [nodeResolve()]
}
