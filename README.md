# model_definition_test
Repo to test https://modelop.atlassian.net/browse/FSN-1652 and https://modelop.atlassian.net/wiki/spaces/DD/pages/1723465733/Model+Definition+injection


To test, create a scoring batchjob with data `{"input":1}` as embedded input. The action function shoudl yield `{"reciprocal":1.0}`.\
The job log should display, among the standard logs, the following:

```
2021/3/31 21:20:20 [info] MODEL-CONSOLE: 
Model Definition keys: 

dict_keys(['rawJson', 'job'])

Input Schema(s) found!
2021/3/31 21:20:20 [info] MODEL-CONSOLE: 
Input Schema Definition: 

{'type': 'record', 'name': 'input_schema.avsc', 'fields': [{'type': 'double', 'name': 'input'}]}
2021/3/31 21:20:20 [info] MODEL-CONSOLE: 
Output Schema(s) NOT found!
2021/3/31 21:20:20 [info] init succeeded
```

This indicates that the input schema definition was successfull extrated from `rawJson`, whereas no output schemas were found.
