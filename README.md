# Llama2 Blog Generator

This is a web application that uses the **Llama2 model** to generate blog posts based on user input. Built with **Streamlit**, it allows users to specify a blog topic, desired word count, and target audience. The generated content can be downloaded as either a **PDF** or **Text file**.

## Features

- **Topic Input**: Users can enter a blog topic.
- **Word Count**: Users can specify the number of words for the blog post.
- **Writing Style**: Choose from different writing styles (e.g., Researchers, Data Scientists, Common People).
- **PDF and Text File Downloads**: After generating a blog, users can download it as a **PDF** or **Text file**.
  
## How It Works

1. **User Input**:
    - Users input a **blog topic**, desired **word count**, and select a **writing style**.
  
2. **Model**: 
    - The **Llama2** model generates blog content based on the provided inputs.
  
3. **Output**:
    - The generated blog is displayed, and users can download it as either **PDF** or **Text file**.

## Installation Guide

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/llama2-blog-generator.git
    cd llama2-blog-generator
    ```

2. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Llama2 Model**:
   Ensure you have the Llama2 model file stored in the specified directory (`models`):
    ```
    E:/GenerativeAIProjects/models/llama-2-7b-chat.ggmlv3.q8_0.bin
    ```

4. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

5. Open [http://localhost:8501](http://localhost:8501) to start using the app.

## Example Input

- **Topic**: Cyber Law
- **Word Count**: 300
- **Target Audience**: Researchers

The app will generate a **Cyber Law** blog targeted at **Researchers**, and it will be close to 300 words in length.



