# large-language-model
This project demonstrates how to use large language model (LLM) API (e.g OpenAI and PaLM) and vector database. It focuses on the PineCone vector database and implements some concepts in generative AI. OpenAI API and PaLM API are implemented together with LangChain. LangChain is a framework designed to simplify the creation of applications using LLM. As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis. I will also briefly discuss the parameter-efficient tuning method that provides better tuning on our custom data.<br>
There are three main types of LLM:
<ol>
  <li>Generic (or Raw) LLM: Predicts the next word or token based on the language in the training data. E.g The dog is on -----. The LLM model will perform autocomplete of the words in the sentence based on the probabilities of the next tokens or words in the training model.</li>
  <li>Instruction Tuned LLM: Trained to predict a response to the instruction prompt given as input. E.g List the best food for breakfast. Limit answers to 5. Here, we instruct the LLM to execute our prompt and produce the answers. An example of LLM in PaLM that provides this operation is <strong>text-bison-001</strong>. We will implement this model in this demo.</li>
  <li>Dialog Tuned LLM: Trained to have a dialogue by predicting the next response. It is a special case of instruction tuned. A typical example is ChatBot (like ChatGPT). An example of LLM in PaLM that provides this operation is <strong>chat-bison-001</strong>. We will implement this model in this demo.</li>
</ol>
````
pip install 
````
