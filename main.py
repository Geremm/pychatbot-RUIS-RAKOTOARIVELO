from functions import *

Directory = "./cleaned"
Matrix_tf_idf = Matrix_TF_IDF(Directory)
list = list_of_files(Directory,".txt")

L = []

for i in range(len(Matrix_tf_idf)):
    for j in range(len(Matrix_tf_idf[i])):
        if Matrix_tf_idf[i][j] == 0.0:
            dic_word = TF(list[i])
            k = 1
            for cle in dic_word.keys():
                if k == j:
                    L.append(cle)
                else:
                    k += 1

print(L)



