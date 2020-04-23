### Setup Environments
```
brew install pyenv-virtualenv
restart shell
pyenv install 3.7.0
pyenv virtualenv 3.7.0 pact
pyenv activate pact
pip install -r requirements.txt
```

### Run in one terminal
```
export FLASK_APP=app.py
flask run
```

### Run in another terminal
```
pact-verifier --provider-base-url=http://localhost:5000/ --custom-provider-header="x-app-name: my_app" --custom-provider-header="Authorization: ABC" ./pact.json
pact-verifier --provider-base-url=http://localhost:5000/ --custom-provider-header="Authorization: ABC" --custom-provider-header="x-app-name: my_app" ./pact.json
```

The outputs looks like this respectively
```
Host: localhost:5000
Cookie: 
Authorization: ABC
X-Forwarded-For: 127.0.0.1
Content-Length: 0
```

```
Host: localhost:5000
Cookie: 
X-App-Name: my_app
X-Forwarded-For: 127.0.0.1
Content-Length: 0
```