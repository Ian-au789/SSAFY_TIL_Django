import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance_pjt.settings")
django.setup()
from your_app.web import crawl_toss_comments_by_name

from openai import OpenAI

company = '삼성전자'
result = crawl_toss_comments_by_name(company)
comments = result['comments']
print(len(comments))
comment_text = "\n".join(comments)

OPENAI_API_KEY= "your API key"
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
  model="gpt-4o-mini",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": "너는 증권 웹사이트에서 댓글들의 내용을 분석하고 현재 해당 주식에 대한 주주들의 여론을 판단하는 금융 AI야."
          "내가 주는 댓글들을 읽어보고 주주들의 두드러지는 의견을 3가지 정도 제시해주고 현재 여론이 긍정적인지 부정적인지 혹은 중립적인지 마지막에 결론지어줘."
          "너의 답변은 보고서 형식으로 3가지 특징을 간단히 요약해서 알려주고 그로 인해 여론은 어떠한 상태로 유추할 수 있다고 결론내리는 형식으로 답변해줘"
          "보고서 형식을 유지하되 소제목은 사용하지 말고 하나의 문단으로 답변을 완성해줘"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": comment_text
        }
      ]
    }
  ],
  temperature=1,
  max_output_tokens=512
)

print(response.output_text)
