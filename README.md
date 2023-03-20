## Running Backend

**1. Clone Repo**

```bash
git clone https://github.com/bowu/analyze_code.git
```
**2. Install Dependencies (you may want to create a new virtual env)**

```bash
cd root/backend
pip install -r requirements.txt
```

**3. Set up OpenAI API key**

```bash
export OPENAI_API_KEY=YOUR_KEY
```

**4. Run**

```bash
uvicorn app:app --reload
```

## Running Frontend

**1. Install Dependencies**

```bash
cd root
npm i
```

**2. Run App**

```bash
npm run dev
```

**3. Analyze code in a folder**

Use your browser and visit http://localhost:3000 \
Type "/inspect code_path" (e.g., /inspect /Users/nerd/buggy_code) \
Then Type any question about the code

**4. Manually check the reports**

Code descriptions are stored at `code_path/_comments` \
Code problem/bug reports are stored at `code_path/_problems`