import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a application to college for college email id",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''{
  "id": "cmpl-7TOHFrrn9IWhMwunitZmmdoqpLmGs",
  "object": "text_completion",
  "created": 1687239189,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nTo: Dean of Admissions\n\nXYZ College\n\nSubject: Request for College Email ID\n\nDear Dean,\n\nI am writing to request a college email ID for myself, [your name], so I can stay connected with other members of the college community.\n\nI am currently studying for my [your major/specialism], and I have an ambitious academic schedule, making it difficult for me to stay in contact with other students, teachers, and fellow students. I believe having a college email ID would be a great way to make communication easier and more personal.\n\nHaving a college email ID would also enable me to stay up to date with college news, and receive correspondence about any events happening on campus. It would be a great source of information to help me make the most of my college experience.\n\nI understand there is a process to be followed when making such a request, and I am more than happy to comply with any documentation or information that is needed.\n\nThank you in advance for considering my request.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 225,
    "total_tokens": 234
  }
}'''