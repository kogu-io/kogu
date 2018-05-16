# Integrating Kogu with your training scripts

Integration from script to Kogu is based on the output of the script. For Python we have created convenience [library](python-library.md) that allows you to use pre-defined methods to do that.

For the scripts in other languages it is possible to integrate with Kogu by printing your data to ```stdout```. In order for the Kogu to process this information it must be passed in the following JSON objects. 

*Each JSON object has to be printed as a single line to stdout.*

## Parameters
The parameters are stored as input (hyper)parameters for the experiment

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
This defines 6 parameters from ```a``` to ```e```. Parameters must either be numbers, booleans, text or arrays. Numeric, boolean and text arrays are supported. The array type is determined by the first array element.

## Metrics
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
This defines metrics calculated by the training experiment to be stored to Kogu. ```iteration``` must be numeric. Iteration value ```-1``` has special meaning - these are the final results of experiment. ```metrics``` contains tuples which may have numeric, boolean or text values. You can send several objects with the same iteration value in that case metrics are merged together, metrics sent later take precedence. 

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
```json
{ "plot": {
        "type": "line",
        "name": "Signals",
        "y_label": "Y",
        "metrics": ["a","b"]
    }
}
```
This defines a real-time updated plot to be displayed on experiment details page. At the moment only ```line``` plot is supported. ```metrics``` is an array metric-names that are to be displayed on the plot (see Metrics above). At the moment only numeric metrics can be plotted.

## Comments
```json
{ "comment": "This is a comment!" }
```
Stores comment to the experiment inforation.

## File Upload
```json
{ "upload": "/path/to/a/file-to-be-uploaded" }
```
Uploads the file to the server. Regardless when the upload command appears in the script all files are uploaded after the script has finished executing.

## Tagging/Untagging
```json
{ "tag": "Super" }
```
Tag the experiment with tag "Super"

```json
{ "untag": "Super" }
```
Remove tag "Super" from the experiment


## Naming
```json
{ "name": "New-Experiment" }
```
Change experiment name to "New-Experiment"

## Marking Experiment to Failed
```json
{ "fail": "Optional reason for the failure" }
```
Mark experiment as "failed". You optoinally can specify the reason for the failure. Pass empty reason in case you do not want pass that info.


# Passing information from Kogu to your script
Kogu supports passing information to scripts defined as command line parameters. For example you can call:

```bash
kogu run script.py -p delta=0.0004 -p gamma=-0.7
```
This will pass parameters ```delta``` and ```gamma``` with corresponding values to the script via ```stdin``` as the following JSON object.

```json
{"delta":0.0004, "gamma":-0.7}
``` 
