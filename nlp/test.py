# 将中文字符串转化为向量（借用 jieba 完成分词）
import jieba

s1 = "这只皮鞋号码大了。那只号码合适"
s2 = "这只皮鞋号码不小，那只更合适"

# read stop words
stop_words = set()
with open('stop_words', 'r', encoding='utf-8') as f:
    for word_lst in f.readlines():
        word = word_lst[0]
        stop_words.add(word)
print(stop_words)

s1_seg = '/'.join([x for x in jieba.cut(s1, cut_all=True) if x not in stop_words and x != ''])
s1_lst = [x for x in jieba.cut(s1, cut_all=True) if x not in stop_words and x != '']
print(s1_lst)
s1_set = set(s1_lst)

s2_seg = '/'.join([x for x in jieba.cut(s2, cut_all=True) if x not in stop_words and x != ''])
s2_lst = [x for x in jieba.cut(s2, cut_all=True) if x not in stop_words and x != '']
print(s2_lst)
s2_set = set(s2_lst)    # remove duplicated data

word_dict = dict()
i = 0
for word in s1_set.union(s2_set):   # get union set of  s1_set and s2_set
    if word in stop_words:
        continue
    word_dict[word] = i
    i += 1
print(word_dict)

def word_to_vec(word_dict, s_lst):
    word_count = dict()
    for word in s_lst:
        if word in stop_words:
            continue
        if word_count.get(word, -1) == -1:
            word_count[word] = 1
        else:
            word_count[word] += 1

    s_vector = [0] * len(word_dict)     # 占位符（Placeholder）

    for word, freq in word_count.items():
        wid = word_dict[word]
        s_vector[wid] = freq
    return s_vector

s1_vector = word_to_vec(word_dict, s1_lst)
print(s1_vector)
s2_vector = word_to_vec(word_dict, s2_lst)
print(s2_vector)