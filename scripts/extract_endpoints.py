# usage: python scripts/extract_endpoints.py diff.json endpoints.json
import sys, json, re, pathlib
DIFF_JSON, OUT_JSON = sys.argv[1], sys.argv[2]
diff = json.load(open(DIFF_JSON))

changed = []
for f in diff.get("files", []):
    if f.get("status") in {"added","modified"} and f["filename"].endswith(".py"):
        changed.append(f["filename"])

ROUTE_RE = re.compile(r'@(?:app|router)\.(get|post|put|patch|delete)\(\s*[\'"]([^\'"]+)[\'"]')
endpoints = []
for p in changed:
    path = pathlib.Path(p)
    if not path.exists():
        continue
    txt = path.read_text(encoding="utf-8", errors="ignore")
    for m in ROUTE_RE.finditer(txt):
        method, path_ = m.group(1).upper(), m.group(2)
        endpoints.append({"file": p, "method": method, "path": path_})

json.dump({"endpoints": endpoints}, open(OUT_JSON,"w"), ensure_ascii=False, indent=2)
print("found endpoints:", endpoints)
