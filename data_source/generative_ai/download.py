import os
import wget

file_links = [
    {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805"
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903"
    },
    {
        "title": "Denoising Diffusion Probabilistic Models",
        "url": "https://arxiv.org/pdf/2006.11239"
    },
    {
        "title": "Instruction Tuning for Large Language Models - A Survey",
        "url": "https://arxiv.org/pdf/2308.10792"
    },
    {
        "title": "Llama 2 - Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288"
    }
]


def is_exist(file_link):
    filename = f"data_source/generative_ai/{file_link['title']}.pdf"
    return os.path.exists(filename)


for file_link in file_links:
    if not is_exist(file_link):
        print(f"Downloading: {file_link['title']}")
        wget.download(
            file_link["url"], out=f"data_source/generative_ai/{file_link['title']}.pdf")
