<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# API caller

A command-line helper for island conservation and invasive-species eradication work.

## What it does

It sends your data to IslasGECI's online analysis service and saves the results on your computer. You can produce tables and figures that summarise capture effort, animal counts, and the progress of an eradication campaign. Everything runs from a terminal.

## Usage

Open a terminal in the project folder and see what the tool can do:

```sh
geci-caller --help
```

Every action has its own help page:

```sh
geci-caller <action> --help
```

Choose an action, give it the path to your data file and a path for the result, then run it. The tool shows the service's response status and creates the requested file.

## Before you start

- A copy of this repository or install it with `pipx`.
- Docker, or Python 3.9 or newer.
- A network connection: the tool sends your data to IslasGECI's online service.
- Input files in the format expected by the service; examples are in `tests/data/`.

## Run the project

### With Docker (preferred)

Open a container and run the tool inside it:

```sh
docker compose run --rm islasgeci bash
geci-caller --help
```

### Without Docker

Install it directly from pip using pipx:

```sh
pipx install geci-caller
geci-caller --help
```


or clone the project and install the package from the project folder, then run it:

```sh
git clone https://github.com/IslasGECI/geci_caller.git
pipx install --editable .
geci-caller --help
```


