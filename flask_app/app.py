from flask import Flask, request, jsonify
from backend import load_or_create_qa_chain
import re
app = Flask(__name__)
qa_chain = load_or_create_qa_chain()

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Please provide a question."}), 400
    
    response = qa_chain.invoke(question)
    
    pattern = rf"Question: {re.escape(question)}\s*(.*?)(?:Question:|$)"
    matches = re.search(pattern, response["result"], re.DOTALL)
    
    if matches:
        cleaned_answer = matches.group(1).strip()
    else:
        # Fallback: try to find just the answer section
        pattern = r"(?:Helpful Answer:)?\s*(.*?)(?:Question:|$)"
        matches = re.search(pattern, response["result"], re.DOTALL)
        if matches:
            cleaned_answer = matches.group(1).strip()
        else:
            # If all else fails, return everything but with prompt removed
            cleaned_answer = re.sub(r"^.*?(?:Helpful Answer:)?\s*", "", response["result"].strip(), flags=re.DOTALL)
    
    # Remove any "Helpful Answer:" prefix that might remain
    cleaned_answer = re.sub(r"^Helpful Answer:\s*", "", cleaned_answer)
    
    print("Original response:", response["result"])
    print("Cleaned answer:", cleaned_answer)
    
    return jsonify({
        "answer": cleaned_answer,
        "sources": [
            {
                "metadata": doc.metadata,
                "content_snippet": doc.page_content[:100]
            } for doc in response["source_documents"]
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
