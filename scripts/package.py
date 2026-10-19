"""Build deterministic plugin and marketplace archives with SHA-256 checksums."""

import hashlib
from pathlib import Path
import zipfile

from validate import PLUGIN, ROOT, validate


def archive(destination, paths, base):
    """Fix timestamps, permissions and ordering, then verify every archived byte."""
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(paths):
            entry = zipfile.ZipInfo(path.relative_to(base).as_posix(), (2020, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(entry, path.read_bytes())
    with zipfile.ZipFile(destination) as bundle:
        expected = {path.relative_to(base).as_posix(): path.read_bytes() for path in paths}
        if len(bundle.namelist()) != len(expected) or set(bundle.namelist()) != set(expected):
            raise ValueError(f"Archive inventory mismatch: {destination}")
        for name, content in expected.items():
            if bundle.read(name) != content:
                raise ValueError(f"Archive content mismatch: {name}")


def package():
    """Produce both install formats from exactly the validated source inventory."""
    version, paths = validate()
    output = ROOT / "artifacts"
    output.mkdir(exist_ok=True)
    plugin_zip = output / f"pair-{version}-plugin.zip"
    marketplace_zip = output / f"pair-{version}-marketplace.zip"
    archive(plugin_zip, [path for path in paths if path.is_relative_to(PLUGIN)], PLUGIN)
    archive(marketplace_zip, paths, ROOT)
    checksums = "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
                        for path in (plugin_zip, marketplace_zip))
    (output / "SHA256SUMS").write_text(checksums, encoding="utf-8", newline="\n")
    print(checksums, end="")


if __name__ == "__main__":
    package()
