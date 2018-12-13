# Command line interface

```bash
$ kogu help [command]
```
>List all available commands, or give specific command help

<br><br>

```bash
$ kogu init [--name project-name] [--link folder-name=target-path ...] [--help]
```
>Initialize new project directory structure based on Cookiecutter Data Science template

Flags:
* `-n`, `--name project-name` – project name
* `-l`, `--link folder-name=target-path ...` – symlinked folders
* `-h`, `--help` – command-specific help

<br><br>

```bash
kogu run script-path [--name experiment-name] [--parameter name=value ...] [--exec executable-name] [--args executable-arguments] [--verbose true|false] [--help]
```
> Execute new experiment

Flags:
* `-n`, `--name experiment-name` – experiment name
* `-p`, `--parameter name=value ...` – parameter name and value
* `-e`, `--exec executable-name` – executable name
* `-a`, `--args executable-arguments` – executable arguments
* `-v`, `--verbose true|false` – verbose output (default true)
* `-h`, `--help` – command-specific help

<br><br>

```bash
$ kogu list [--last] [--csv] [--json [--pretty]] [--verbosity verbosity-level] [--help]
```
> List experiments

Flags:
* `-l`, `--last` – last experiment only
* `-c`, `--csv` – CSV format
* `-j`, `--json` – JSON format
* `-p`, `--pretty` – pretty print JSON
* `-v`, `--verbosity verbosity-level` – verbosity level 1 – 4 (default 2)
* `-h`, `--help` – command-specific help

<br><br>

```bash
$ kogu tag experiment-hash tag-text [--delete] [--help]
```
> Add or remove experiment tag

Flags:
* `-d`, `--delete` – delete the tag
* `-h`, `--help` – command-specific help

<br><br>

```bash
$ kogu name experiment-hash experiment-name [--help]
```
> Rename experiment

Flags:
* `-h`, `--help` –command-specific help

<br><br>

```bash
$ kogu upload experiment-hash file-path [--append] [--help]
```
> Upload and attach file to experiment

Flags:
* `-a`, `--append` – append the file content to the existing file rather than store the content as a new file. Defaults to false.
* `-h`, `--help` – command-specific help

<br><br>

```bash
$ kogu rm experiment-hash [--help]
```
> Remove experiment

Flags:
* `-h`, `--help` – command-specific help
