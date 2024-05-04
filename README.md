### bostonhousepricing_GitActions

### software and tools Requirements

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
5. [postman](https://www.postman.com/downloads)

Create a new environment

For conda environment
```
conda create -p venv python==3.10 -y
```

For activate conda environment
```
conda activate venv/
```

For venv environment
```
python3 -m venv bostonvenv
```

For activate venv environment(macos)
```
source bostonvenv/bin/activate
```

For checking api request need postman (JSON for postman) 
```
{
   "data":{
      "CRIM":0.00632,
      "EN":12.0,
      "INDUS":4.31,
      "CHAS":0.0,
      "NOX":0.5638,
      "RM":1.575,
      "AGE":1.2,
      "DIS":1.0900,
      "RAD":2.0,
      "TAX":100,
      "PTRATIO":15.3,
      "LSTATE":1.90
   }
}
```
