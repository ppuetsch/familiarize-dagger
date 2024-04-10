# familiarize-dagger

This repository has the purpose of me getting familiar with dagger. 
Any Code in here can be used according to the MIT License. 

# Things I want to do in a CI Pipeline: 
1. Run a Python Test
1. Run static checks (flake8, black, ...)
1. Run online checks (SonarCloud) 
1. Build a Docker Container
1. Push the Container to a Registry
1. Run a Test against the Container

# To run the CI-Steps locally: 

1. Make sure Doc
2. Get Dagger. See [Dagger Windows Installation Manual](https://docs.dagger.io/quickstart/729237/cli). TL;DR: Run in PowerShell: 
```
Invoke-WebRequest -UseBasicParsing -Uri https://dl.dagger.io/dagger/install.ps1 | Invoke-Expression
```
3. Add dagger path to you PATH-Variable
2. Install the Dagger-Python-SDK. See [Dagger Python SDK Getting Started](https://archive.docs.dagger.io/0.9/sdk/python/628797/get-started/). TL;DR: Run:
```
pip install dagger-io
```
3. Run the CI Job locally:
```

```