# Unbabel CLI Application


This application parses an `--input_file`, here, expressed as a stream of events (translations), processed line by line until reach out an aggregated output. 


### Module SMA

The Simple Moving Average (SMA), is processed every minute within a window event sized in the arguments of the cli (`--window_size`).
The application is assuming that new events are tailed, as the example below verified by the `timestamp` key. 
For that manner, we are expecting that input has at least an `translation_id`, the `timestamp` and the `duration` of the translation for SMA calculations.


### Application Setup

##### Activate a virtual environment (recommended)

```
	$ python3 -m venv venv
	$ source venv/bin/activate

```


##### Build

```
	$ pip install poetry
	$ poetry install

```

##### Tests

```
	$ pytest tests

```


##### Run

If we want to count, for each minute, the moving average delivery time of all translations for the past 10 minutes:
```
	$ unbabel_cli --input_file events.json --window_size 10
```
	
The input file format would be something like:
```
	{"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20}
	{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31}
	{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}
```


The output file would be something in the following format.

```
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
```


#### Notes

For a deeper understanding of the project decisions, 
I would highly recommend to visit :arrow_right: babel-into-unbabel .
Your input and updates are welcome! :smiley:

##### Credits
Part of the base structure was inspired by the templates - [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
