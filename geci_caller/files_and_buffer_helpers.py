import io


def read_file_as_buffer(file_path):
    with open(file_path, "rb") as file:
        buffer_file = io.BytesIO(file.read())
    return buffer_file
