# 构造 {'18960653':['6.1', 'm61']}
# 改成构造 {'6.1':'m61'}
import json

# deploymentId = list(range(18960653, 18960684))
# deploymentId.remove(18960672)
# deploymentId.append(20235856)
# deploymentId = [str(i) for i in deploymentId]
# print(deploymentId)

t6 = list(range(61,66))
t7 = list(range(71,79))
t7.remove(76)
t8 = list(range(81,84))
t10 = list(range(101,105))
t11 = list(range(111,120))
t11.extend(list(range(1110,1112)))
t85 = [85]
tt = t6+t7+t8+t10+t11+t85
ttstr = []
mt = []
for i in tt:
    mt.append('m'+str(i))
    if i // 1000: #4位数及以上
        i = i/100
    else:
        i = i/10
    ttstr.append(str(i))
t1110 = ttstr.index('11.1',20) #修改第二个11.1为11.10
ttstr[t1110] = '11.10'
# print(ttstr)

# deployment_value = []
# for index, value in enumerate(ttstr):
#     value = value.split(',')
#     value.append(mt[index])
#     deployment_value.append(value)
# print(deployment_value)

t_dict = dict(zip(ttstr, mt))
# print(t_dict)

# print(t_dict['8.5'])




# 保存构造的数据
with open("t_dict_db.json","w") as f:
    json.dump(t_dict,f)
    print("加载入文件完成...")

# 打开时只用下面这个
# import json

# with open("t_dict_db.json",'r') as load_f:
#     t_dict = json.load(load_f)

# print(t_dict['18960653'])
