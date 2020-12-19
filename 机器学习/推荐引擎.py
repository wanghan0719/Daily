"""
基于用户的协同过滤
"""
import json
import numpy as np

# 加载数据
with open('data/ratings.json', 'r') as f:
    rating = json.loads(f.read())
users = list(rating.keys())
# 构建7*7矩阵]
scmat = []
for user1 in users:
    scrow = []
    for user2 in users:
        # 计算user1和user2的欧氏距离
        movies = set()
        for movie in rating[user1].keys():
            if movie in rating[user2]:
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        else:  # 两个人有共同语言 记录两个人为相同电影打过的评分，计算相似度
            user1_vec, user2_vec = [], []
            for movie in movies:
                user1_vec.append(rating[user1][movie])
                user2_vec.append(rating[user2][movie])
            # 计算欧氏距离得分
            user1_vec, user2_vec = np.array(user1_vec), np.array(user2_vec)
            # score=1/(1+np.sqrt(((user1_vec-user2_vec)**2).sum()))
            score = np.corrcoef(user1_vec, user2_vec)[0, 1]
        scrow.append(score)
    scmat.append(scrow)

# 输出得分矩阵
# print(np.round(scmat, 2))

# 获取当前用户的相似用户，遍历相识用户看过的电影，总结出推荐列表
scmat = np.array(scmat)
users = np.array(users)
for i, user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    sim_scores = scmat[i][sorted_indices]
    # 按照相似度得分的顺序获取相似用户的用户名数组
    sim_users = users[sorted_indices][sim_scores > 0]
    # 迭代每个相似用户，获取相似用户看过的电影，作为被推荐电影存入推荐列表
    # 推荐字典：{'电影A':[2,3],'电影B':[4,5,4],'电影C':[1,2,2,1].....}
    rec_dic = {}
    for sim_user in sim_users:
        for movie, score in rating[sim_user].items():
            if movie not in rating[user].keys():
                if movie not in rec_dic.keys():
                    rec_dic[movie] = []
                rec_dic[movie].append(score)
    print(user)
    print(rec_dic)
    movie_list = sorted(rec_dic.items(), key=lambda x: np.mean(x[1]), reverse=True)
    print(movie_list)
