#!/usr/bin/env node
import { fileURLToPath } from "url";
import path from "path";
import { spawn } from "child_process";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Resolve the actual path of install-skills.mjs in the root
const scriptPath = path.resolve(__dirname, "../install-skills.mjs");

const child = spawn("node", [scriptPath], {
  stdio: "inherit",
});

child.on("exit", (code) => {
  process.exit(code);
});
