# self-attention 实现​
import torch
from torch import nn
from math import sqrt


class Self_Attention(nn.Module):
    # 输入 x 的形状是 [batch_size, seq_len, input_dim]
    # 比如一个批次有 4 个句子，每个句子 3 个词，每个词 embedding 维度为 2：
    # X = torch.randn(4, 3, 2)
    # input : batch_size * seq_len * input_dim
    # q : batch_size * input_dim * dim_k
    # k : batch_size * input_dim * dim_k
    # v : batch_size * input_dim * dim_v
    def __init__(self, input_dim, dim_k, dim_v):
        super(Self_Attention, self).__init__()
        self.q = nn.Linear(input_dim, dim_k)
        self.k = nn.Linear(input_dim, dim_k)
        self.v = nn.Linear(input_dim, dim_v)
        self._norm_fact = 1 / sqrt(dim_k)

    def forward(self, x):
        # Q=X*q,这里的q是W_q，权重
        # Q: batch_size * seq_len * dim_k
        Q = self.q(x)
        # K: batch_size * seq_len * dim_k
        K = self.k(x)
        # V: batch_size * seq_len * dim_v
        V = self.v(x)

        # 注意：缩放因子应在 softmax 前乘
        # torch.bmm 是批量矩阵乘法。Q @ K.T：计算每个词对其他词的相似度。
        scores = torch.bmm(Q, K.permute(0, 2, 1)) * self._norm_fact
        atten = nn.Softmax(dim=-1)(scores)  # batch_size * seq_len * seq_len

        # output: batch_size * seq_len * dim_v
        output = torch.bmm(atten, V)
        return output


# 测试代码
X = torch.randn(4, 3, 2) #是在用 PyTorch 生成一个形状为 [4, 3, 2] 的随机张量。4个样本，每个句子三个词，每个词用2维表示
# X = torch.tensor([
#     [0.2, 0.1],
#     [0.3, 0.4],
#     [0.5, 0.6],
#     [0.8, 0.9]
# ]).unsqueeze(0)

print("输入张量 X:\n", X)

self_atten = Self_Attention(2, 4, 5)  # input_dim=2, dim_k=4, dim_v=5
res = self_atten(X)
print("输出形状:", res.shape)  # [4,3,5]
print("输出向量:", res)