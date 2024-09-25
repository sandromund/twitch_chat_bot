# python_template
Template with my most used setup.


https://twitchapps.com/tmi/

```shell
mkdir source
mkdir configs
mkdir docs 
mkdir resources 
mkdir tests 
mkdir logs
```

## Install
````shell
pip install --upgrade pip
pip install pylint black pyinstaller
pip install -r requirements.txt
````

## Run
````shell
python source/main.py run --config configs/default.yaml
````

## Development
Lint
```shell
pylint $(git ls-files '*.py')
```
Test
````shell
pytest
````
Format 
````shell
black source 
black tests
````
## Deployment
Create an Exe
````shell
pyinstaller --onefile source/main.py --name=app
```` 
Run the Exe 
````shell
dist/app.exe run --config configs/default.yaml
````