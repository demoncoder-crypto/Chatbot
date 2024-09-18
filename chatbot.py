import openai
import spacy
from transformers import pipeline

# Load Spacy NLP model
nlp = spacy.load("en_core_web_sm")

# Set up OpenAI API key
openai.api_key = 'sk-GA8iK5mv4UfhkqNqRca6NsAkQ7dtGXmDpeojGarEAxT3BlbkFJx6unhl6n3G6l53X2tQw67VxkuQ6iPoxlSV8MUj6goA'

# Initialize Hugging Face pipeline
qa_pipeline = pipeline("question-answering")

def preprocess_text(user_input):
    """Use SpaCy to process the input text"""
    doc = nlp(user_input)
    return " ".join([token.text for token in doc])

def get_gpt_response(prompt):
    """Get a response from GPT-4"""
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def answer_question(user_input):
    """Use Hugging Face model to get specific answers for the user"""
    context = "This is some context for answering questions."
    response = qa_pipeline({
        'question': user_input,
        'context': context
    })
    return response['answer']

def generate_response(user_input):
    """Generate AI response using GPT-4 and Hugging Face"""
    processed_input = preprocess_text(user_input)
    gpt_response = get_gpt_response(processed_input)
    return gpt_response
