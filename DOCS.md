# DOCS.md

### cli write-posterior-results --input-path --initial-parameters-path --output-path

Writes posterior results for a population model to a CSV file.

Parameters:
- `--input-path`: Path of input data.
- `--initial-parameters-path`: Path of initial parameters.
- `--output-path`: Path of output file.

Returns:
- Writes the results to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli plot-cumulative-cpue-series-by-season --input-path --output-path

Writes a plot of cumulative catch-per-unit-effort by season.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli plot-cumulative-series-cpue-by-flight --input-path --output-path

Writes a plot of the cumulative catch-per-unit-effort series by flight.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli write-bootstrap-progress-intervals --input-path --bootstrapping-number --output-path

Writes bootstrap progress intervals to a JSON file.

Parameters:
- `--input-path`: Path of input data.
- `--bootstrapping-number`: Number of bootstraps.
- `--output-path`: Path of figure to write.

Returns:
- Writes the intervals to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli filter-by-method --input-path --method --output-path

Writes the rows matching an extraction method to a CSV file.

Parameters:
- `--input-path`: Path of input data.
- `--method`: Extraction method.
- `--output-path`: Path of figure to write.

Returns:
- Writes the filtered rows to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli write-aerial-monitoring --input-path --bootstrapping-number --output-path

Writes aerial-monitoring results to a JSON file.

Parameters:
- `--input-path`: Path of input data.
- `--bootstrapping-number`: Number of bootstraps.
- `--output-path`: Path of figure to write.

Returns:
- Writes the results to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli write-population-status-from-mixed-methods --first-method-status --second-method-status --output-path

Writes population status combining two methods to a JSON file.

Parameters:
- `--first-method-status`: Path of the first method's status data.
- `--second-method-status`: Path of the second method's status data.
- `--output-path`: Path of output file.

Returns:
- Writes the combined status to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli plot-comparative-yearly-cpue --socorro-path --guadalupe-path --output-path

Writes a plot comparing yearly catch-per-unit-effort for Socorro and Guadalupe.

Parameters:
- `--socorro-path`: Path of Socorro data.
- `--guadalupe-path`: Path of Guadalupe data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli plot-comparative-catch-curves --socorro-path --guadalupe-path --output-path

Writes a plot comparing catch curves for Socorro and Guadalupe.

Parameters:
- `--socorro-path`: Path of Socorro data.
- `--guadalupe-path`: Path of Guadalupe data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli write-population-status --input-path --bootstrapping-number --output-path

Writes population status results to a JSON file.

Parameters:
- `--input-path`: Path of input data.
- `--bootstrapping-number`: Number of bootstraps.
- `--output-path`: Path of figure to write.

Returns:
- Writes the results to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli write-instantaneous-and-cumulative-cpue --input-path --output-path --resolution

Writes instantaneous and cumulative catch-per-unit-effort to a CSV file.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path to write.
- `--resolution`: Temporal resolution: monthly, season.

Returns:
- Writes the table to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli write-csv-probability --input-path --bootstrapping-number --output-path --window-length --resolution

Writes eradication progress probabilities to a CSV file.

Parameters:
- `--input-path`: Path of input data.
- `--bootstrapping-number`: Number of bootstrap by window.
- `--output-path`: Path of csv file to write.
- `--window-length`: Number of months by window.
- `--resolution`: Temporal resolution.

Returns:
- Writes the probabilities to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli write-probability-progress-figure --input-path --output-path

Writes a figure of eradication progress probability.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

### cli plot-custom-cpue-vs-cum-captures --input-path --config-path --output-path

Writes a plot of catch-per-unit-effort against cumulative captures using a configuration file.

Parameters:
- `--input-path`: Path of input data.
- `--config-path`: Path of config file.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli plot-cpue-vs-cum-captures --input-path --output-path

Writes a plot of catch-per-unit-effort against cumulative captures.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli render-instantaneous-and-cumulative-cpue-time-series --input-path --output-path

Writes a time-series plot of instantaneous and cumulative catch-per-unit-effort.

Parameters:
- `--input-path`: Path of input data.
- `--output-path`: Path of figure to write.

Returns:
- Writes the figure to `--output-path` and exits.

Errors:
- HTTP error responses abort the command.

Notes:
- The figure format follows the extension of `--output-path`.

### cli version

Prints the installed version.

Parameters:
- None.

Returns:
- Prints the version string and exits.
