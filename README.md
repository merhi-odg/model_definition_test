# model_definition_test
Repo to test https://modelop.atlassian.net/browse/FSN-1652 and https://modelop.atlassian.net/wiki/spaces/DD/pages/1723465733/Model+Definition+injection


To test, create a scoring batchjob with data `{"input":1}` as embedded input. The action function shoudl yield `{"reciprocal":1.0}`.\
The job log should display, among the standard logs, the following:

```
2021/3/31 21:57:57 [info] state changes to RUNNING
2021/3/31 21:57:57 [info] MODEL-CONSOLE: 
Model Definition keys: 

dict_keys(['rawJson', 'job'])
2021/3/31 21:57:57 [info] MODEL-CONSOLE: 
Model Reference Key:  model

Input Schema(s) found!


Input Schema Definition: 

{'type': 'record', 'name': 'input_schema.avsc', 'fields': [{'type': 'double', 'name': 'input'}]}

Output Schema(s) NOT found!
2021/3/31 21:57:58 [info] init succeeded
2021/3/31 21:57:58 [info] MODEL-CONSOLE: action input:  {'input': 1}
num:  1
output:  {'reciprocal': 1.0}
2021/3/31 21:57:58 [info] state changes to FINISHING
2021/3/31 21:57:58 [info] MODEL-CONSOLE: Model runner exits
2021/3/31 21:57:58 [info] state changes to FINISHED
```

This indicates that the input schema definition was successfull extrated from `rawJson`, whereas no output schemas were found.


Model definitions can also be tested through a deployedModel. To do so, first deploy this model to an engine, then make a POST request with data `{"input":1}`. Engine logs should display the same as above.
