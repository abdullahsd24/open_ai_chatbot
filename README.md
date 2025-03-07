# open_ai_chatbot


## PreRquisits 
For Linux
1. Install pyenv
2. Install Python Vision via Pyenv
3. Create Virtual Environment



## Virtual Env Using pyenv

On Linux and Mac Install `pyenv` accordingly
Then

### Create Env

```bash
pyenv virtualenv 3.12.3 bot-venv
```

### Activate Env

```bash
pyenv activate bot-venv
```

### Install requirements/libraries 

```
pip install -r requirements-dev.txt
```


### create .env
create .env file and store OPENAI_API_KEY value



### Run App on local
Prompt From Project Root:
```
python main.py
```

# Test Using Postman

## store prompt method
request=POST

url=http://127.0.0.1:5000/promt

body = {
    "prompt": "is react a library or framework"
}

## update prompt method
request=PUT
url=http://127.0.0.1:5000/response/prompt_index

body = {
    "new_prompt": "is react a library or framework"
}

## delete prompt method
request=DELETE

url=http://127.0.0.1:5000/response/prompt_index

## Prompt response from open ai method
request=GET

url=http://127.0.0.1:5000/response/prompt_index


# Methodology USED for Storage (IN-Memory Data Structure)

I have used in-memory data structure for my this crud. this method have many Pros and cons. a short description mentioned below

## Pros of In-Memory Storage
1. **Simple Setup:** No extra tools or configurations needed.

2. **Speed:** Instant access since everything is stored in RAM.

3. **No External Tools:** Works without databases or file systems.

4. **Great for Temporary Data:** Perfect for short-lived or session-specific info.

## Cons of In-Memory Storage
1. **Data Loss:** Data is lost on application restart or crash.

2. **Scalability Issues:** Limited by system RAM, not suitable for large datasets.

3. **Not for Long-Term Use:** Bad for production where data needs to stick around.

4. **Concurrency Problems:** Multiple users or processes can cause conflicts.

## When to Use It
Quick prototypes, temporary data, testing, or small projects.

## When to Avoid It
Production apps, large-scale systems, or when data must be saved permanently.

# Better Alternatives
**File Storage:** Saves data to files but slower than memory.