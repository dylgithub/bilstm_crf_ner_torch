# -*- coding: utf-8 -*-
from seqeval.metrics import f1_score, accuracy_score, classification_report, precision_score, recall_score
y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O', 'B-PER', 'I-PER']]
y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'B-MISC', 'I-MISC', 'O', 'B-PER', 'I-PER']]
# 支持BIO和BIOES格式数据
"""
列表中一个有9个元素，其中预测对的元素个数为6个，那么准确率为2/3。
标注的实体总个数为2个，预测的实体总个数为3个，预测正确的实体个数为1个，
那么precision=1/3, recall=1/2, F1=0.4。
"""
print(accuracy_score(y_true, y_pred))
print(precision_score(y_true, y_pred))
print(recall_score(y_true, y_pred))
print(f1_score(y_true, y_pred))
print(classification_report(y_true, y_pred))
