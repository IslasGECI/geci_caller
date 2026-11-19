import io


def read_file_as_buffer(file_path):
    with open(file_path, "rb") as file:
        buffer_file = io.BytesIO(file.read())
    return buffer_file


def write_response_content(output_path, response):
    with open(output_path, "wb") as out_file:
        out_file.write(response.content)
