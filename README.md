#  YouTube Title & Description Generator using IBM Watsonx

This project uses IBM Watsonx foundation models to generate catchy YouTube video titles and SEO-optimized descriptions based on a given topic or idea.

##  Features

-  Generates engaging YouTube titles
-  Generates full 2–3 sentence YouTube descriptions
-  Uses IBM watsonx.ai foundation model: `mistralai/mistral-small-3-1-24b-instruct-2503`
-  Ensures complete and clean output using an `---END---` marker

##  Example

**Input:**
```
Facts about real world
```

**Output:**
```
"Unbelievable Real-World Facts That Will Blow Your Mind"

Discover fascinating facts about the real world that will blow your mind. From hidden wonders to astonishing phenomena
```

##  Setup

### 1. Clone the repository

```bash
git clone https://github.com/Tharun7209/youtube-title-and-short-description-generator.git
cd youtube-title-and-short-description-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python youtube_generator.py
```

> You'll be prompted to enter a YouTube topic or idea.
