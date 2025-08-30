import sys


def edit_mvhd(file_path, new_value):
    new_bytes = new_value.to_bytes(4, byteorder="big")
    print(f"New bytes to write: {new_bytes.hex()} (decimal {new_value})")

    with open(file_path, "rb+") as f:
        data = f.read()

        # Find the mvhd box
        idx = data.find(b"mvhd")
        if idx == -1:
            raise ValueError("mvhd box not found in file")

        # Move 16 bytes after "mvhd"
        target_offset = idx + 4 + 16

        # Read the current 4 bytes
        f.seek(target_offset)
        old_bytes = f.read(4)
        old_value = int.from_bytes(old_bytes, byteorder="big")
        print(
            f"Current 4 bytes at offset {target_offset}: {old_bytes.hex()} (decimal {old_value})"
        )

        # Overwrite with new bytes
        f.seek(target_offset)
        f.write(new_bytes)

    print(
        f"Edited 4 bytes at offset {target_offset} to {new_value} (0x{new_value:08X})"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Drag and drop a video file onto this script to edit its video duration metadata."
        )
        sys.exit(1)

    video_path = sys.argv[1]  # file path from drag-and-drop
    video_duration_milliseconds = int(
        input("Enter desired video duration metadata in milliseconds: ")
    )
    edit_mvhd(video_path, video_duration_milliseconds)
