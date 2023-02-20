def GetText(Model, MaxTokens, Temperature, Prompt):  # 得到文本
  import openai
  openai.api_key = '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'
  response = openai.Completion.create(
    model=Model,
    max_tokens=MaxTokens,
    temperature=Temperature,
    prompt=Prompt,
  )
  return response.choices[0].text

def CountChinese(String):  # 统计中文字个数
  i = 0  # 计数
  for c in String:
    import string
    if c in string.ascii_letters:  # 英文
      continue
    elif c.isdigit():  # 数字
      continue
    elif c.isspace():  # 空格
      continue
    elif c.isalpha():  # 中文,除了英文之外,剩下的字符认为就是中文
      i += 1
  return i  # 返回计数


