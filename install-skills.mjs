import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Find user's project root (first package.json outside node_modules)
// If none found, fallback to process.cwd()
function findProjectRoot(startDir) {
  let dir = startDir;
  while (dir !== path.parse(dir).root) {
    if (fs.existsSync(path.join(dir, "package.json")) && !dir.includes("node_modules")) {
      return dir;
    }
    dir = path.dirname(dir);
  }
  // fallback to current working directory
  return process.cwd();
}

const projectRoot = findProjectRoot(__dirname);
const packageSkillsDir = path.join(__dirname, "dist", "skills");
const claudeDir = path.join(projectRoot, ".claude");
const skillsDir = path.join(claudeDir, "skills");

// Recursive copy helper
function copyRecursive(src, dest) {
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
  for (const item of fs.readdirSync(src)) {
    const srcPath = path.join(src, item);
    const destPath = path.join(dest, item);
    const stat = fs.statSync(srcPath);
    if (stat.isDirectory()) copyRecursive(srcPath, destPath);
    else fs.copyFileSync(srcPath, destPath);
  }
}

(async () => {
  try {
    // Ensure .claude directory exists
    fs.mkdirSync(claudeDir, { recursive: true });
    console.log(`📁 Created .claude directory at ${claudeDir}`);

    // Ensure .claude/skills exists
    fs.mkdirSync(skillsDir, { recursive: true });
    console.log(`📁 Created .claude/skills directory at ${skillsDir}`);

    // Copy skills if available
    if (fs.existsSync(packageSkillsDir)) {
      console.log("📦 Copying Claude skills to user project...");
      copyRecursive(packageSkillsDir, skillsDir);
      console.log("✅ Skills installed successfully in .claude/skills/");
    } else {
      console.warn("⚠️ No dist/skills folder found — did you run `npm run build` before publish?");
    }
  } catch (err) {
    console.error("❌ Error installing skills:", err);
  }

  console.log("✨ Claude skill installation complete!");
})();
