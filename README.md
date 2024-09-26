# Twitch Chat Bot

Bot that can chat with other users on Twitch.


# Setup

````shell
pip install --upgrade pip
pip install pylint black pyinstaller
pip install -r requirements.txt
````
1. Create a [Twitch](twitch.tv) Account and get a [Token](https://twitchapps.com/tmi/)
2. Setup [LM Studio](https://lmstudio.ai/) and 
   1. Install it and download a model
   3. Run a local inference server
3. Adapt the config file based on 1. and 2.

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
Create an Exe
````shell
pyinstaller --onefile source/main.py --name=app
```` 
Run the Exe 
````shell
dist/app.exe run --config configs/default.yaml
````