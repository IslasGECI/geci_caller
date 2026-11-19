from geci_caller.run_stan_endpoint import call_bayesian_model


def test_call_bayesian_model_endpoint():
    effort_and_captures_path = "tests/data/data_effort_captures_for_model.json"
    parameters_path = "tests/data/init_captures_effort_model.json"
    obtained = call_bayesian_model(effort_and_captures_path, parameters_path)
    expected_endpoint = "http://islasgeci.org:200/compute_eradication_bayesian_model_results"
    assert expected_endpoint in obtained.url
