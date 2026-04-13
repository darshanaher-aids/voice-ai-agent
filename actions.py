import os

OUTPUT_DIR = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_file():
    try:
        file_path = os.path.join(OUTPUT_DIR, "new_file.txt")
        with open(file_path, "w") as f:
            f.write("This is a new file.")

        return f"File created successfully: {file_path}"

    except Exception as e:
        return f"Error creating file: {str(e)}"


def write_code(filename="generated.py"):
    try:
        file_path = os.path.join(OUTPUT_DIR, filename)

        code = """def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
"""

        with open(file_path, "w") as f:
            f.write(code)

        return f"Code written successfully in: {file_path}"

    except Exception as e:
        return f"Error writing code: {str(e)}"


def summarize_text(text):
    try:
        # Simple summary (first 20 words)
        words = text.split()
        summary = " ".join(words[:20])

        return f"Summary: {summary}..."

    except Exception as e:
        return f"Error summarizing text: {str(e)}"


def execute_action(intent_data, text=""):
    intent = intent_data.get("intent")

    if intent == "create_file":
        return create_file()

    elif intent == "write_code":
        filename = intent_data.get("filename", "generated.py")
        return write_code(filename)

    elif intent == "summarize":
        return summarize_text(text)

    elif intent == "chat":
        return f"Chat response: You said '{text}'"

    else:
        return "Unknown intent"
