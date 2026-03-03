import os
from pathlib import Path
from collections import defaultdict

EXCLUDED_DIRS = {
    ".venv",
    ".git",
    "__pycache__",
    "logs",
    ".vscode",
    "node_modules"
}


class StructureScanner:

    def __init__(self, root_path):
        self.root = Path(root_path)
        self.stats = defaultdict(lambda: {
            "files": 0,
            "directories": 0,
            "python_files": 0
        })

    def should_exclude(self, path):
        for part in path.parts:
            if part in EXCLUDED_DIRS:
                return True
        return False

    def scan(self):

        for path in self.root.rglob("*"):

            if self.should_exclude(path):
                continue

            try:
                relative_parts = path.relative_to(self.root).parts
            except ValueError:
                continue

            if len(relative_parts) == 0:
                continue

            top_domain = relative_parts[0]

            if path.is_dir():
                self.stats[top_domain]["directories"] += 1

            elif path.is_file():
                self.stats[top_domain]["files"] += 1
                if path.suffix == ".py":
                    self.stats[top_domain]["python_files"] += 1

        return self.stats

    def rank_domains(self):

        ranking = []

        for domain, data in self.stats.items():
            score = (
                data["python_files"] * 3 +
                data["directories"] * 2 +
                data["files"]
            )

            ranking.append((domain, score, data))

        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking


if __name__ == "__main__":

    scanner = StructureScanner("C:/NAYA")
    scanner.scan()
    ranking = scanner.rank_domains()

    print("\n=== STRUCTURAL DOMAIN ANALYSIS ===\n")

    for domain, score, data in ranking:
        print(f"DOMAIN: {domain}")
        print(f"  Score: {score}")
        print(f"  Directories: {data['directories']}")
        print(f"  Files: {data['files']}")
        print(f"  Python Files: {data['python_files']}")
        print("")
