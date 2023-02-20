def WriteJoke(Joke):  # 写笑话
    Path = 'C:/Files/Python/ChatGPT/Joke/Joke.txt'
    Txt = open(Path, 'a', encoding='utf-8')  # 返回文本文件对象
    import time
    Txt.write(time.strftime('%Y-%m-%d %H:%M:%S') + '\n') # 写系统日期时间
    from Function import CountChinese
    Txt.write('字数：' + str(CountChinese(Joke)) + ' 长度：' + str(len(Joke)) + '\n')  # 写字数长度
    Txt.write('每日一笑')
    Txt.write(Joke + '\n'*2)
    Txt.close()

def GenJokes(TtlJokes):  # 生产笑话
    print('笑话总数：' + str(TtlJokes))
    i = 1  # 计数
    while i <= TtlJokes:  # 生产指定总数的笑话
        from Function import GetText
        from Joke.Variable import Model, MaxTokens, Temperature, Prompt
        Joke = GetText(Model, MaxTokens, Temperature, Prompt)  # 得到笑话
        WriteJoke(Joke)  # 写笑话
        print(i)  # 打印计数
        i += 1