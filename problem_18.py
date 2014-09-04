triangle=[[0]*15 for i in range(15)]
triangle[0]=[75]
triangle[1]= [95, 64]
triangle[2]=[17, 47, 82]
triangle[3]=[18, 35, 87, 10]
triangle[4]=[20, 4, 82, 47, 65]
triangle[5]=[19, 1, 23, 75, 3, 34]
triangle[6]=[88, 2, 77, 73, 7, 63, 67]
triangle[7]=[99, 65, 4, 28, 6, 16, 70, 92]
triangle[8]=[41, 41, 26, 56, 83, 40, 80, 70, 33]
triangle[9]=[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
triangle[10]=[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
triangle[11]=[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
triangle[12]=[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
triangle[13]=[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
triangle[14]=[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
second_to_last=13
for iteration in range(second_to_last,-1,-1):
    length=len(triangle[iteration])
    for i in range(0,length):
        next_row=iteration+1
        sum_1=triangle[iteration][i]+triangle[iteration+1][i]
        next=i+1
        sum_2=triangle[iteration][i]+triangle[next_row][next]
        sum_list=[sum_1,sum_2]
        triangle[iteration][i]=max(sum_list)
maximum_value=int(triangle[0][0])
print(maximum_value)

# for i in range(0,1):
#     j_end=i+1
#     summation=75+triangle[1][i]
#     for j in range(i,j_end):
#         k_end=j+1
#         summation=summation+triangle[2][j]
#         for k in range(j,k_end):
#             l_end=k+1
#             summation=summation+triangle[3][k]
# # #             for l in range(k,l_end):
#                 m_end=l+1
#                 summation=summation+triangle[4][l]
#                 for m in range(l,m_end):
#                     n_end=m+1
#                     summation=summation+triangle[5][m]
#                     for n in range(m,n_end):
#                         o_end=n+1
#                         summation=summation+triangle[6][n]
#                         for o in range(n,o_end):
#                             p_end=o+1
#                             summation=summation+triangle[7][o]
#                             for p in range(o,p_end):
#                                 q_end=p+1
#                                 summation=summation+triangle[8][p]
#                                 for q in range(p,q_end):
#                                     r_end=q+1
#                                     summation=summation+triangle[9][q]
#                                     for r in range(q,r_end):
#                                         s_end=r+1
#                                         summation=summation+triangle[10][r]
#                                         for s in range(r,s_end):
#                                             t_end=s+1
#                                             summation=summation+triangle[11][s]
#                                             for t in range(s,t_end):
#                                                 u_end=t+1
#                                                 summation=summation+triangle[12][t]
#                                                 for u in range(t,u_end):
#                                                     v_end=u+1
#                                                     summation=summation+triangle[13][u]
#                                                     summation_array=[0,0]
# #                                                     number=number
#                                                     for v in range(u,v_end):
#                                                         iteration=v-u
#                                                         summation_array[iteration]=summation+triangle[14][v]
#                                                     summation_max=max(summation_array)
#                                                     triangle_sum[number]=summation_max
#                                                     number=number+1
#                                                     triangle_sum.append(0)