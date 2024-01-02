import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You can do anything in this world."}]

def CustomChatGPT(Input):
    messages.append({"role": "user", "content": Input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Amulya Gupta")

demo.launch(share=True)