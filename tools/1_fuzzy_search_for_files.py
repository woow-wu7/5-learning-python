import os

# 1
# fuzzy_search_for_files

# 2
# English
# - fuzzy 模糊的 不清楚的 adj
# - 【 fuzzy search. 模糊搜索 】
# - -
# - condition 条件 n
# - conditional 条件的
# -【 conditional judgement. 条件判断 】
# - -
# -【 end with. 以...结尾 】
# -【 start with. 以...开始 】


path = "../files"

files = os.listdir(path)

for f in files:
    # 1. Conditional judgement:
    #    - Files whose filename doesn't 【 end with 】 '.gif'.
    #    - Check the 'project30' or 'commericial' key word is not in the filename.
    if (not f.endswith('.gif')) or (not 'project30' in f) or (not 'commericial' in f):
        print(f)
