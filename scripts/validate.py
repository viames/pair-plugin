"""Validate the public Pair distribution without running application tools."""

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "pair"
SKILLS = {"pair", "api-safety", "module-workflow", "frontend-forms",
          "migration-review", "crud-review"}
ROOT_FILES = {"README.md", "README.it.md", "LICENSE", "CHANGELOG.md", "PUBLISHING.md",
              "requirements-dev.txt", ".gitignore", ".gitattributes"}
ROOT_DIRS = {".agents", ".github", "docs", "plugins", "scripts"}
IGNORED = {".git", ".venv", "artifacts", "__pycache__", ".DS_Store"}


def require(condition, message):
    """Fail with a useful release diagnostic even when Python uses optimization."""
    if not condition:
        raise ValueError(message)


def files():
    """Return the explicit distribution inventory, excluding generated outputs."""
    result = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in IGNORED for part in relative.parts):
            continue
        require(not path.is_symlink(), f"Symlinks are not distributable: {relative}")
        if not path.is_file():
            continue
        require(relative.parts[0] in ROOT_DIRS or relative.as_posix() in ROOT_FILES,
                f"Unexpected public file: {relative}")
        require(path.suffix not in {".pyc", ".pem", ".key", ".env"},
                f"Unexpected private/generated file: {relative}")
        result.append(path)
    return sorted(result)


def local_path(base, value, boundary=ROOT):
    """Resolve a local reference and reject missing or escaping targets."""
    require(isinstance(value, str) and value, f"Invalid path: {value!r}")
    target = (base / unquote(urlsplit(value).path)).resolve()
    require(target.is_relative_to(boundary.resolve()), f"Path escapes package: {value}")
    require(target.exists(), f"Missing target from {base.relative_to(ROOT)}: {value}")
    return target


def validate():
    """Check metadata and references; this is not a model behavior evaluation."""
    inventory = files()
    manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    require(manifest["name"] == "pair", "Unexpected plugin name")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Invalid version")
    require(manifest["license"] == "MIT", "License mismatch")
    require(manifest["author"]["name"] == "Viames Marino", "Author mismatch")
    require(not (PLUGIN / ".codex-plugin").exists(), "Ambiguous duplicate manifest")
    interface = manifest["extensions"]["com.openai"]["interface"]
    for key in ("composerIcon", "logo"):
        local_path(PLUGIN, interface[key], PLUGIN)
    for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        require(interface[key].startswith("https://viames.github.io/pair-plugin/"),
                f"Unexpected public URL: {key}")

    catalog = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    require(catalog["name"] == "viames-pair", "Marketplace name mismatch")
    require(len(catalog["plugins"]) == 1, "Expected one marketplace plugin")
    entry = catalog["plugins"][0]
    require(entry["name"] == "pair" and entry["source"]["source"] == "local",
            "Invalid marketplace source")
    require(local_path(ROOT, entry["source"]["path"]) == PLUGIN, "Wrong plugin source")

    skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
    require({path.parent.name for path in skills} == SKILLS, "Skill inventory mismatch")
    for path in skills:
        content = path.read_text(encoding="utf-8")
        require(content.startswith("---\n"), f"Missing skill metadata: {path}")
        metadata = yaml.safe_load(content.split("---", 2)[1])
        require(metadata["name"] == path.parent.name, f"Skill name mismatch: {path}")
        require(isinstance(metadata.get("description"), str) and
                0 < len(metadata["description"]) <= 1024, f"Invalid description: {path}")
    for path in (PLUGIN / "skills").glob("*/agents/openai.yaml"):
        metadata = yaml.safe_load(path.read_text(encoding="utf-8"))
        require(isinstance(metadata.get("interface"), dict), f"Invalid agent metadata: {path}")

    links = 0
    for path in inventory:
        if path.suffix not in {".md", ".html"}:
            continue
        content = path.read_text(encoding="utf-8")
        references = (re.findall(r"!?\[[^\]\n]*\]\(([^)\s]+)\)", content)
                      if path.suffix == ".md" else
                      re.findall(r'(?:href|src)="([^"]+)"', content))
        for reference in references:
            url = urlsplit(reference)
            if url.scheme or reference.startswith(("#", "//")):
                continue
            local_path(path.parent, reference, PLUGIN if path.is_relative_to(PLUGIN) else ROOT)
            links += 1
    require((ROOT / "LICENSE").read_bytes() == (PLUGIN / "LICENSE").read_bytes(),
            "Root and plugin licenses differ")
    print(f"Validated Pair {manifest['version']}: {len(skills)} skills, "
          f"{links} local references, {len(inventory)} public files. Model scenarios: not run.")
    return manifest["version"], inventory


if __name__ == "__main__":
    validate()
