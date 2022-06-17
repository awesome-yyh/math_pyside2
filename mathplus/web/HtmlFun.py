import re
# 分析html
def read_html(table_id):
    try:
        with open('./htmlDownload/'+table_id+'.html', 'r', encoding='UTF-8') as f:
            text = f.read()
    except FileNotFoundError:
        return 0,0,0
 
    questionIdc = re.compile(r'js-question-header-.*?class')
    # questionIdc = re.compile(r'&quot;questionId&quot;:&quot;.*?&quot')
    questionIds = questionIdc.findall(text)

    questionId = []
    for i in questionIds:
        questionId.append(i[19:-7])
    # print(questionId)   #查找所有的questionId
    # questionId = questionId[::4]
    red_word = []
    red_wordi = ''
    for i in range(len(questionId)):
        cc = r'js-question-header-'+str(questionId[i])+'.+?Revert to Last Response'
        # print(cc)
        red_rangec = re.compile(cc, re.DOTALL)
        # red">
        red_range = red_rangec.findall(text)
        # print(red_range[0])
        red_wordc = re.compile(r'red\S>[\d+\.\,\/\-\d\w]+<')  #red">1.4<    #  [\d+\.\d]+|
        red_words = red_wordc.findall(str(red_range))  
        if red_words:
            for i in red_words:
                red_wordi = red_wordi + ',' + i[5:-1]
                # red_wordi.append(i[5:-1])
        else:
            red_wordi = ",none"
        red_word.append(red_wordi[1:])
        # print(red_wordi)
        red_wordi = ''
    # print(red_word) #查找所有的红字
    # print(len(red_word))
    
    length = len(questionId)

    return questionId, red_word, length

if __name__ == '__main__':
    a = '11.6'
    [questionId, red_word, length] = read_html(a)
    print(length,questionId,red_word)
    # questionId = 
    