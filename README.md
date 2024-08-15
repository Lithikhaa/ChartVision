# ChartVision: A Comprehensive Solution for Query-Driven Chart Analysis 🧠📊

## Project Overview

**ChartVision** is an advanced deep-learning solution designed to process chart images and respond to user queries about the visual data presented in those charts. This project integrates multiple large language models (LLMs) including **T5**, **VL-T5**, **VisionTapas**, and a custom model trained using the **PaliGemma** framework. These models are combined into a unified system stored as `.safetensor` models to manage and process complex visual and textual data effectively.

The primary objective of this project is to create a system that takes a chart image and a user query as input and returns accurate, context-aware responses about the chart's content. This README will guide you through the entire process, from setting up your environment to deploying the models.

### 🌐 WEB DEMO: Experience ChartVision live by trying out the web demo on Hugging Face Spaces: 
[ChartVision Web Demo](https://huggingface.co/spaces/lithi/ChartVision)



## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- 🐍 Python 3.8+
- 🖥️ PyTorch
- 🤗 Transformers
- 📦 safetensors
- 🗃️ Pandas
- 📸 OpenCV

### Installation

1. **Clone the Repository:**

   Start by cloning the repository to your local machine.

2. **Install the Required Packages:**

   Install all necessary packages by following the instructions provided in the `requirements.txt` file.

3. **Set Up Your Environment:**

   Set up the necessary environment variables and paths to ensure smooth execution of the training and deployment processes.

## 📚 Datasets

The full ChartQA dataset (including the annotations) can be downloaded from Hugging Face: [Full ChartQA Dataset](https://huggingface.co/datasets/ahmed-masry/ChartQA)

![image](https://github.com/user-attachments/assets/a36b14d2-7c97-435e-ab2d-42671ad0b21f)

## 🔄 Workflow Overview

### Loading the Dataset

Load the dataset by correctly specifying the directory paths. Ensure that the images, annotations, and tables are loaded into memory for subsequent processing.

### Preprocessing the Data

#### 🖼️ Image Preprocessing

Perform necessary preprocessing steps on the chart images, such as resizing, normalization, and augmentation. Ensure the images are correctly formatted before feeding them into the model.

#### 📝 Text Preprocessing

Tokenize and encode the textual data, including annotations and queries, using the appropriate tokenizer. Proper text preprocessing is crucial for ensuring the models understand and respond to the queries effectively.

### Model Training and Fine-Tuning

#### 💻 Loading Pretrained Models

Load the pre-trained models that will be used in this project, including **T5**, **VL-T5**, **VisionTapas**, and the **PaliGemma** model. Ensure the models are correctly initialized and ready for fine-tuning.

#### 🛠️ Training with PaliGemma

Fine-tune the PaliGemma model using the prepared dataset. Monitor the training process to ensure the model learns effectively from the data and produces accurate responses.

#### 🔗 Combining Models

Once all models are trained, combine their weights into a unified format. Ensure the combined model is coherent and capable of handling the input data as expected.

### Model Deployment

#### 💾 Saving Models as .safetensors

After training and combining the models, save the final model weights into `.safetensors` files. Split the model into parts to efficiently manage storage and loading during deployment.

#### 🌐 Deploying the Combined Model

Deploy the combined model to process input chart images and respond to user queries. The safetensors models are stored on Hugging Face: [Chartvision Model Repository](https://huggingface.co/lithi/Chartvision) and deployed in Hugging Face Space: [ChartVision Space](https://huggingface.co/spaces/lithi/ChartVision).

### 🧪 Evaluation and Testing

Evaluate the performance of the deployed model by testing it on various chart images and queries. Monitor the accuracy and response time to ensure the model meets the project's objectives.

Each annotation JSON file follows a format similar to the PlotQA and FigureQA datasets. For more details, you can refer to the documentation: [PlotQA Dataset](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md) and [FigureQA Dataset](https://www.microsoft.com/en-us/research/project/figureqa-dataset/)

## 🧠 Models

- **VL-T5**  
  Please refer to [VL-T5](https://github.com/vis-nlp/ChartQA/tree/main/Models/VL-T5)

- **T5**  
  Please refer to [T5](https://github.com/vis-nlp/ChartQA/tree/main/Models/T5)

- **VisionTapas**  
  Please refer to [VisionTapas](https://github.com/vis-nlp/ChartQA/tree/main/Models/VisionTapas)

## 🛠️ Usage Guide

### Input Format

Provide the chart image and query in the correct format. The model will process the input and return a response based on the chart's content.

### Example Queries

Test the model with various queries to see how it responds. For example:
- "When does the line reach the peak?"
- "How much does the value of Approve decrease from Jul 2015 to Sep 2015?"

## 🤝 Contributing

Contributions to the project are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.
