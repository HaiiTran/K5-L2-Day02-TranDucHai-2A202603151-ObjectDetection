"""Build a CVAT-importable Ultralytics YOLO archive for drive_042..drive_050.

Boxes are manually estimated from the supplied 640x360 previews. Review them in
CVAT before treating the archive as final ground truth.
"""

from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path


# Ultralytics YOLO indices are mapped by class name on CVAT import.
NAMES = ["car", "truck", "bus", "van"]
WIDTH, HEIGHT = 640, 360

# Pixel boxes: (class name, left, top, right, bottom).
# These cover visually clear vehicles; tiny distant traffic needs review.
BOXES: dict[int, list[tuple[str, int, int, int, int]]] = {
    42: [
        ("bus", 402, 42, 640, 321),
        ("truck", 355, 149, 585, 359),
        ("bus", 146, 238, 432, 359),
        ("car", 198, 273, 288, 359),
        ("car", 25, 82, 48, 114),
    ],
    43: [
        ("car", 57, 276, 126, 359),
        ("van", 164, 153, 216, 214),
        ("car", 83, 153, 123, 215),
        ("car", 365, 181, 453, 253),
        ("car", 322, 249, 421, 359),
        ("car", 465, 88, 498, 123),
        ("car", 530, 86, 572, 125),
    ],
    44: [
        ("car", 0, 131, 83, 207),
        ("car", 85, 93, 126, 137),
        ("car", 194, 112, 251, 158),
        ("van", 438, 134, 498, 208),
        ("car", 253, 273, 346, 359),
        ("car", 477, 236, 566, 359),
        ("van", 307, 185, 362, 238),
    ],
    45: [
        ("bus", 0, 216, 153, 359),
        ("car", 0, 132, 43, 184),
        ("car", 20, 91, 74, 145),
        ("car", 64, 92, 116, 151),
        ("car", 106, 111, 148, 156),
        ("car", 365, 20, 400, 55),
        ("van", 344, 89, 393, 137),
        ("car", 371, 153, 420, 201),
        ("car", 367, 220, 426, 296),
    ],
    46: [
        ("car", 274, 193, 457, 320),
        ("car", 83, 275, 261, 359),
        ("car", 418, 279, 629, 359),
    ],
    47: [
        ("car", 0, 228, 68, 289),
        ("car", 74, 117, 168, 169),
        ("van", 203, 107, 247, 151),
        ("truck", 404, 91, 506, 183),
        ("car", 565, 280, 639, 359),
        ("car", 11, 265, 69, 303),
    ],
    48: [
        ("bus", 0, 146, 76, 259),
        ("bus", 128, 106, 292, 221),
        ("bus", 296, 119, 579, 308),
        ("car", 67, 191, 117, 238),
        ("car", 154, 142, 210, 187),
        ("car", 225, 134, 281, 179),
        ("car", 270, 138, 324, 184),
        ("van", 339, 137, 389, 177),
        ("car", 383, 146, 441, 190),
        ("car", 453, 153, 511, 199),
        ("car", 563, 223, 639, 287),
    ],
    49: [
        ("bus", 0, 216, 153, 359),
        ("car", 0, 132, 42, 184),
        ("car", 20, 91, 74, 145),
        ("car", 64, 92, 116, 151),
        ("car", 106, 111, 148, 156),
        ("van", 47, 84, 105, 139),
        ("car", 365, 20, 400, 55),
        ("van", 344, 89, 393, 137),
        ("car", 371, 153, 420, 201),
        ("car", 367, 220, 426, 296),
    ],
    50: [
        ("bus", 0, 204, 192, 359),
        ("car", 181, 171, 253, 226),
        ("car", 276, 159, 339, 218),
        ("car", 343, 176, 401, 238),
        ("car", 404, 172, 475, 235),
        ("van", 584, 151, 639, 213),
        ("car", 493, 223, 578, 293),
        ("car", 558, 258, 639, 359),
        ("car", 228, 232, 291, 294),
        ("car", 295, 238, 348, 301),
        ("car", 353, 247, 420, 317),
    ],
}


def find_images(source: Path) -> dict[int, Path]:
    by_stem: dict[str, list[Path]] = {}
    for path in source.iterdir():
        if path.is_file():
            by_stem.setdefault(path.stem.lower(), []).append(path)
    found: dict[int, Path] = {}
    missing: list[str] = []
    for number in range(42, 51):
        stem = f"drive_{number:03d}"
        candidates = by_stem.get(stem, [])
        if len(candidates) != 1:
            missing.append(f"{stem} (found {len(candidates)} matching files)")
        else:
            found[number] = candidates[0]
    if missing:
        raise FileNotFoundError("Image check failed: " + "; ".join(missing))
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    images_dir = args.images.resolve()
    output = args.output.resolve()
    images = find_images(images_dir)
    bundle = output.parent / "manual_drive_042_050"
    if bundle.exists():
        shutil.rmtree(bundle)
    image_out = bundle / "images" / "train"
    label_out = bundle / "labels" / "train"
    image_out.mkdir(parents=True)
    label_out.mkdir(parents=True)

    counts: dict[int, int] = {}
    for number, image in images.items():
        shutil.copy2(image, image_out / image.name)
        lines = []
        for label, x1, y1, x2, y2 in BOXES[number]:
            if label not in NAMES or not (0 <= x1 < x2 <= WIDTH and 0 <= y1 < y2 <= HEIGHT):
                raise ValueError(f"Invalid box for drive_{number:03d}: {(label, x1, y1, x2, y2)}")
            class_id = NAMES.index(label)
            cx = ((x1 + x2) / 2) / WIDTH
            cy = ((y1 + y2) / 2) / HEIGHT
            width = (x2 - x1) / WIDTH
            height = (y2 - y1) / HEIGHT
            lines.append(f"{class_id} {cx:.6f} {cy:.6f} {width:.6f} {height:.6f}")
        (label_out / f"{image.stem}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        counts[number] = len(lines)

    (bundle / "train.txt").write_text(
        "".join(f"images/train/{images[n].name}\n" for n in range(42, 51)),
        encoding="utf-8",
    )
    (bundle / "data.yaml").write_text(
        "path: ./\ntrain: train.txt\nnames:\n"
        + "".join(f"  {i}: {name}\n" for i, name in enumerate(NAMES)),
        encoding="utf-8",
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in bundle.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(bundle).as_posix())

    print("Manual draft annotations written:")
    for number, count in counts.items():
        print(f"  drive_{number:03d}: {count} boxes")
    print(f"Upload this archive to CVAT: {output}")


if __name__ == "__main__":
    main()
