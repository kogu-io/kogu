# Python helper library
This convenience library can be used to integrate your scripts with Kogu. Methods do not create dependency to Kogu infrastructure. The integration is performed using specially formatted standard output lines. With Kogu methods in the script, it can still be executed without Kogu. In this case the methods append nothing to output.

# Installation
You can install the library using ```pip``` by calling: 

```bash
pip install kogu
```

# Terms
<dl>
<dt>Parameter</dt><dd>Input variable for the script.</dd>
<dt>Metric</dt><dd>Variable, which value or values are logged as intermediate or final results of the script execution.</dd>
<dt>Result metric</dt><dd>Result (output) value of the script e.g. result, error_rate</dd>

</dl>

# Methods
- [`Kogu.name(name)`](#name)
- [`Kogu.load_parameters(output=False)`](#load_parameters)
- [`Kogu.update_parameters(dic, output=False)`](#update_parameters)
- [`Kogu.metrics(dic, iteration=-1)`](#metrics)
- [`Kogu.tag(tag)`](#tag)
- [`Kogu.untag(tag)`](#untag)
- [`Kogu.comment(comment)`](#comment)
- [`Kogu.upload(filename)`](#upload)
- [`Kogu.plot(plot_type, series, name=None, y_label=None)`](#plot)
- [`Kogu.fail(reason=None)`](#fail)


# Other topics
- [Identifiers](#identifiers)


---

# <div id='name'></div>`name`
> Creates Kogu specific experiment rename line to calling script stdout.

```python
Kogu.name(name)
```

Arguments:
* `name` – A string to be used as a name.

# <div id='load_parameters'></div>`load_parameters`
> Loads parameters to calling module dictionary. Parameters can be passed to the script as JSON via stdin pipe and/or via parameters.json file located at script folder. Parameters passed via pipe overwrite those passed from parameters.json file.

```python
Kogu.load_parameters(output=False)
```

Arguments:
* `output` – An optional flag to output the parameters loaded to the console as well. By default it is not set.

Example:

When using the following JSON:
```json
{
    "number_of_iterations": 100,
    "learning_rate": 0.02
}
```

variables ```number_of_iterations``` and ```learning_rate``` are defined in script having values 100 and 0.02 correspondingly.

# <div id='update_parameters'></div>`update_parameters`
> Creates Kogu specific parameter registration line to calling script stdout. You can call the method multiple times for the same parameters. In this case the later calls take precedence.

```python
Kogu.update_parameters(dic, output=False)
```
Arguments:
* `dic` – Key-value set of parameters. All the keys must be [valid identifiers](#identifiers).
* `output` – An optional flag to output the parameters updated to the console as well. By default it is not set.

# <div id='metrics'></div>`metrics`
> Creates Kogu specific metric information line to calling script stdout. You can call the method multiple times for the same metrics. In this case the later calls take precedence.

```python
Kogu.metrics(dic, iteration=-1)
```
Arguments:
* `dic` – Key-value set of metrics to report. All the keys must be [valid identifiers](#identifiers).
* `iteration` – Optional iteration number (integer) to be logged with the metrics. The default value of -1 indicates the metrics are the final results.

# <div id='tag'></div>`tag`
> Adds a tag to experiment.

```python
Kogu.tag(tag)
```

Arguments:
* `tag` – A string to be used as a tag.

# <div id='untag'></div>`untag`
> Removes tag from experiment.

```python
Kogu.untag(tag)
```

Arguments:
* `tag` – A tag string to be removed.

# <div id='comment'></div>`comment`
> Creates Kogu specific comment line to calling script stdout. Newlines `\n` are replaced with spaces. Carriage returns `\r` are stripped.

```python
Kogu.comment(comment)
```
Arguments:
* `comment` – Text to add as a comment.

# <div id='upload'></div>`upload`
> Creates Kogu specific File upload line to calling script stdout. The file is uploaded to the Kogu server after the script execution has successfully completed.

```python
Kogu.upload(filename)
```
Arguments:
* `filename` – Relative or absolute path to the file. In case of relative path is passed it is evaluated from the script root.

# <div id='plot'></div>`plot`
> Creates Kogu specific Plot registration line to calling script stdout. The values to be plotted must be sent to kogu using [`metrics`](#metrics) method.

```python
Kogu.plot(plot_type, series, name=None, y_label=None)
```
Arguments:
* `plot_type` – String. Type of the plot to be used. Currently the only supported type is: "line" 
* `series` – List of metrics keys to be used for the plot. All of them must be [valid identifiers](#identifiers).
* `name` – Optional name of the plot. When omitted it will default to plot_type value.
* `y_label` – Optional label for the Y-axis of the plot. When omitted will default to Y.

# <div id='fail'></div>`fail`
> Creates Kogu specific experiment failure line to calling script stdout. This effectively marks experiment as failed.

```python
Kogu.fail(reason=None)
```

Arguments:
* `reason` – An optional string to be used as a failure reason.

# <div id='identifiers'></div>Identifiers
Valid identifiers start with character and may contain both upper and lowercase characters (a-z, A-Z), numbers and underscore. Identifiers are case sensitive. 

Examples of valid identifiers:

```python
variable_3
TheName
a5
B9
metric
```

Examples of invalid identifiers:

```python
3bears
my-name
ä
_a5
my variable
```
