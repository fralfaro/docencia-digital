"""
Renderiza todas las presentaciones RevealJS del directorio slides/
y las deja en docs/slides/

Uso:
    python render_slides.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SLIDES_DIR = ROOT / "slides"

print("Renderizando presentaciones...")
result = subprocess.run(
    ["quarto", "render"],
    cwd=SLIDES_DIR,
)

if result.returncode == 0:
    print("Presentaciones renderizadas correctamente en docs/slides/")
else:
    print("Error al renderizar las presentaciones.")
    sys.exit(1)
