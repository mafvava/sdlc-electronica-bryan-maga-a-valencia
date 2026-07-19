import json
from pathlib import Path
from typing import Any


class JsonLinesRecorder:
    """Guarda lecturas una por una en un archivo JSON-lines."""

    def __init__(self, file_path: str | Path) -> None:
        # Guardamos la ruta como Path para trabajar más cómodo con archivos.
        self.file_path = Path(file_path)

    def record(self, data: dict[str, Any]) -> None:
        """Guarda una lectura nueva al final del archivo."""
        with self.file_path.open("a", encoding="utf-8") as file:
            json.dump(data, file)
            file.write("\n")

    def read_all(self) -> list[dict[str, Any]]:
        """Lee todas las lecturas guardadas."""
        if not self.file_path.exists():
            return []

        records: list[dict[str, Any]] = []

        with self.file_path.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    records.append(json.loads(line))

        return records