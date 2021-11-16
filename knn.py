# -*- coding: UTF-8 -*-

import math
import csv
import operator
"""KNN算法预测"""


class KNearestNeighbor(object):
    def __init__(self):
        pass

    # 读入数据集  训练集和测试集
    @staticmethod
    def read_dataset(filename1, filename2, trainingSet, testSet):
        with open(filename1, 'r') as csvfile:
            lines = csv.reader(csvfile)  # 读取所有的行
            dataset1 = list(lines)       # 转化成列表
            for x in range(len(dataset1)):  # 每一行数据
                for y in range(8):
                    dataset1[x][y] = float(dataset1[x][y])   # 8个参数转换为浮点数
                testSet.append(dataset1[x])    # 生成测试集

        with open(filename2, 'r') as csvfile:
            lines = csv.reader(csvfile)  # 读取所有的行
            dataset2 = list(lines)       # 转化成列表
            for x in range(len(dataset2)):   # 每一行数据
                for y in range(8):
                    dataset2[x][y] = float(dataset2[x][y])  # 8个参数转换为浮点数
                trainingSet.append(dataset2[x])  # 生成训练集

    # 计算欧式距离
    @staticmethod
    def calculateDistance(testdata, traindata, length):  # 计算距离
        distance = 0  # length表示维度 数据共有几维
        for x in range(length):
            distance += pow((int(testdata[x]) - int(traindata[x])), 2)
        return round(math.sqrt(distance), 3)    # 保留3位小数

    # 选取距离最近的K个实例
    def getNeighbors(self, trainingSet, test_instance, k):  # 返回最近的k个边距
        distances = []
        length = len(test_instance)
        # 对训练集的每一个数计算其到测试集的实际距离
        for x in range(len(trainingSet)):
            dist = self.calculateDistance(test_instance, trainingSet[x], length)
            print('训练集：{} --- 距离：{}'.format(trainingSet[x], dist))
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))  # 按距离从小到大排列
        # print(distances)
        neighbors = []
        # 排序完成后取距离最小的前k个
        for x in range(k):
            neighbors.append(distances[x][0])
        print(neighbors)
        return neighbors

    #  获取距离最近的K个实例中占比例较大的分类
    @staticmethod
    def getResponse(neighbors):   # 根据少数服从多数，决定归类到哪一类
        class_votes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]  # 统计每一个分类的多少  空气质量的数字标识
            if response in class_votes:
                class_votes[response] += 1
            else:
                class_votes[response] = 1
        print(class_votes.items())
        sortedVotes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)  # 按分类大小排序  降序
        return sortedVotes[0][0]    # 分类最大的  少数服从多数   为预测结果

    # 准确率计算
    @staticmethod
    def getAccuracy(test_set, predictions):
        correct = 0
        for x in range(len(test_set)):
            # predictions预测的与testset实际的比对  计算预测的准确率
            if test_set[x][-1] == predictions[x]:
                correct += 1
            else:
                # 查看错误预测
                print(test_set[x], predictions[x])

        print('有{}个预测正确，共有{}个测试数据'.format(correct, len(test_set)))
        return (correct / (len(test_set))) * 100.0

    def run(self):
        training_set = []    # 训练集
        test_set = []        # 测试集
        self.read_dataset('test.txt', 'train.txt', training_set, test_set)  # 数据划分
        print('Train set: ' + str(len(training_set)))
        print('Test set: ' + str(len(test_set)))
        # generate predictions
        predictions = []
        k = 6  # 取最近的6个数据
        for x in range(len(test_set)):  # 对所有的测试集进行测试
            neighbors = self.getNeighbors(training_set, test_set[x], k)  # 找到8个最近的邻居
            result = self.getResponse(neighbors)  # 找这7个邻居归类到哪一类
            predictions.append(result)

        accuracy = self.getAccuracy(test_set, predictions)
        print('预测准确度为:  {:.2f}%'.format(accuracy))   # 保留2位小数


if __name__ == '__main__':
    a = KNearestNeighbor()
    a.run()
# -*- codeing = utf-8 -*-
