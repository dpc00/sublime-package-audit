"""Put the four candidate packages into the portable's Packages dir the way an
install would, so Sublime loads them and the command registry can be inspected."""

import io
import os
import shutil
import urllib.request
import zipfile

DEST = "C:/Users/donal/tools/st_portable/Data/Packages"

PKGS = {
    "Toggle File": "https://codeload.github.com/Harurow/sublime_togglefile/zip/1.2.3",
    "Translate-CN": "https://codeload.github.com/mjd507/Sublime-Translate/zip/2.0.2",
    "NimPlus": "https://codeload.github.com/vanyle/NimPlus/zip/1.1.0",
    "anaconda_php": "https://codeload.github.com/DamnWidget/anaconda_php/zip/v0.1.6",
}

for name, url in PKGS.items():
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "audit"}), timeout=60).read(40_000_000)
    z = zipfile.ZipFile(io.BytesIO(raw))
    top = z.namelist()[0].split("/")[0]
    target = os.path.join(DEST, name)
    if os.path.isdir(target):
        shutil.rmtree(target)
    os.makedirs(target)
    n = 0
    for member in z.namelist():
        if member.endswith("/"):
            continue
        rel = member[len(top) + 1:]
        out = os.path.join(target, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(z.read(member))
        n += 1
    print("installed", name, n, "files")
