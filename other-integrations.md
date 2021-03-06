# Integrating Kogu with your training scripts

Integration from script to Kogu is based on the output of the script. For Python we have created convenience [library](python-library.md) that allows you to use pre-defined methods to do that.

For the scripts in other languages it is possible to use Kogu logging capabilities by printing the data to ```stdout```. In order for the Kogu to process this information print the data as a JSON listed below.

**Each JSON object has to be printed as a single line to stdout.**

## Parameters
To log the input (hyper)parameters for the experiment.

```json
{ "parameters": {
        "a" : 3,
        "b" : -2.4,
        "c" : "Text",
        "d" : true,
        "e" : [2,3,5]
    }
}
```
This defines 5 parameters from ```a``` to ```e```. Parameters must either be numbers, booleans, text or arrays. Numeric, boolean and text arrays are supported. The array type is determined by the first array element.

## Metrics
You can log the metrics to monitor the training progess (using plots) or store final training results. 
```json
{ "metric": {
        "iteration": -1,
        "metrics": {
            "a": 3,
            "b": -2.5,
            "c": true
        }
    }
}
```
This defines metrics calculated by the experiment to be stored to Kogu. ```iteration``` must be numeric. Iteration value ```-1``` has special meaning - these are the final results of experiment. ```metrics``` contains tuples which may have numeric, boolean or text values. You can send several objects with the same iteration value in that case metrics are merged together, metrics sent later take precedence. 

**Example:**
Two metrics passed as: 
```json
{"metric":{"iteration":0, "metrics":{"a":3, "b":-2.5}}}

{"metric":{"iteration":0, "metrics":{"b":5.5, "c":true}}}
```
will result the following metrics for iteration 0:

key | value
-- | --
a | 3
b | 5.5
c | true

## Plots
Use plots to monitor training progess during the experiment. You can plot any metric logged.
```json
{ "plot": {
        "type": "line",
        "name": "Signals",
        "y_label": "Y",
        "metrics": ["a","b"]
    }
}
```
This defines a real-time updated plot to be displayed on experiment details page. At the moment only ```line``` plot is supported. ```metrics``` is an array of metric-names that are to be displayed on the plot (see Metrics above). At the moment only metrics with numeric values can be plotted.

## Comments
You can log random textual information during the experiment for future reference.
```json
{ "comment": "This is a comment!" }
```
Stores comment to the experiment information.

## File Upload
You can upload files. For example images or model generated by the experiment.
```json
{ "upload": {"name": "/path/to/a/file-to-be-uploaded", "append": false} }
```
Uploads the file to the server. Depending on value of ```append``` value the file content passed is either appended to the (potentially) existing file in server, or new file is created (default). Regardless when the upload command appears in the script all files are uploaded after the script has finished executing.

## Tagging/Untagging
Experiments can be tagged with keywords. Later on you can use tags to group and search for the experiment results
```json
{ "tag": "Super" }
```
Tag the experiment with tag "Super"

```json
{ "untag": "Super" }
```
Remove tag "Super" from the experiment


## Naming
By default the experiment name is extracted from the name of the script file. You can alter this name.
```json
{ "name": "New-Experiment" }
```
Change experiment name to "New-Experiment"

## Marking Experiment to Failed
By default, when the script has been executed without errors the experiment is marked as successful. If you want to control the experiment status from the script you have ability to mark the experiment as failed.
```json
{ "fail": "Optional reason for the failure" }
```
Mark experiment as "failed". Optionally you can specify the reason for the failure. Pass empty reason in case you want to omit that data.


# Passing information from Kogu to your script
Kogu supports passing information to the scripts as one additional way of parametrizing the experiments. Passing values is done with command line parameters when calling kogu executable. For example you can call:

```bash
kogu run script.py -p delta=0.0004 -p gamma=-0.7
```
This will pass parameters ```delta``` and ```gamma``` with corresponding values to the script ```script.py``` via ```stdin``` as the following JSON object.

```json
{"delta":0.0004, "gamma":-0.7}
``` 

You can pass numeric, boolean, text and array parameters. Arrays can be either numeric, boolean or text arrays.

In the script you can process the stdin and use passed values as you see fit.
