import streamlit as st
from transformers import pipeline

# set_page_config() must be the first Streamlit command
st.set_page_config(page_title="AI Text Generator", layout="centered")


# Load the pre-trained model (distilgpt2)
@st.cache_resource
def load_generator():
    return pipeline('text-generation', model='distilgpt2')


generator = load_generator()

st.title("Creative AI Text Generator")  # This should be after set_page_config
st.markdown("Enter a prompt and let the AI generate creative text for you.")  # This too

user_prompt = st.text_area(
    "Enter your prompt here:",
    "The sun was shining,",
    height=100
)
st.sidebar.header("Generation Settings")

max_length = st.sidebar.slider(
    "Maximum text length:",
    min_value=50,
    max_value=500,
    value=200,
    step=10
)

temperature = st.sidebar.slider(
    "Creativity (Temperature):",
    min_value=0.1,
    max_value=1.5,
    value=0.7,
    step=0.1
)

st.sidebar.info(
    " 'Temperature' controls the randomness of generation. "
    "Higher values produce more creative, less predictable text."
)

if st.button("Generate Text"):
    if user_prompt:
        with st.spinner("Generating..."):
            generated_text = \
                generator(user_prompt, max_length=max_length, temperature=temperature, num_return_sequences=1)[0][
                    'generated_text']
            st.subheader("Generated Text:")
            st.write(generated_text)
    else:
        st.warning("Please enter a prompt.")

st.markdown("---")
st.markdown("Developed with Streamlit and Hugging Face Transformers.")
