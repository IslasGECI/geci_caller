from geci_caller.files_and_buffer_helpers import read_file_as_buffer

import requests


def call_bayesian_model(traps_cameras_effort_captures_path, parameters_path):
    url = "http://islasgeci.org:200/compute_eradication_bayesian_model_results"
    data_file_like = read_file_as_buffer(traps_cameras_effort_captures_path)
    initial_parameters_file_like = read_file_as_buffer(parameters_path)
    files = {
        "data_path": (traps_cameras_effort_captures_path, data_file_like, "application/json"),
        "initial_parameters_path": (
            parameters_path,
            initial_parameters_file_like,
            "application/json",
        ),
    }
    data = {"model_type": "traps-and-cameras"}
    response = requests.post(url, files=files, data=data)
    return response
