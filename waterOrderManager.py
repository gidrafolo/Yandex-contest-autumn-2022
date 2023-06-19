from functools import cmp_to_key

class TriplPoint:
    inxPointOne: int
    inxValueOne: int
    inxPointTwo: int
    inxValueTwo: int
    inxPointThree: int
    inxValueThree: int
    inxPoint4: int
    inxValue4: int
    inxPoint5: int
    inxValue5: int
    inxPoint6: int
    inxValue6: int
    inxPoint7: int
    inxValue7: int
    inxPoint8: int
    inxValue8: int
    inxPoint9: int
    inxValue9: int

    def init(self):
        pass

    def init(self):
        pass

class Order:
    __start: int
    __finish: int
    __cost: int

    def __init__(self, start, finish, cost):
        self.__start = int(start)
        self.__finish = int(finish)
        self.__cost = int(cost)

    @property
    def start(self):
        return self.__start

    @property
    def finish(self):
        return self.__finish

    @property
    def cost(self):
        return self.__cost


class Question:
    __start: int
    __finish: int
    __type: int

    def __init__(self, start, finish, type):
        self.__start = int(start)
        self.__finish = int(finish)
        self.__type = int(type)

    @property
    def start(self):
        return self.__start

    @property
    def finish(self):
        return self.__finish

    @property
    def type(self):
        return self.__type

# 1
# 10 100 1000
# 6
# 1 10 1
# 1 10 2
# 10 100 1
# 10 100 2
# 100 1000 1
# #100 1000 2

class QuestionA(Question):
    __answer: int

    def __init__(self, question: Question, answer):
        super().__init__(question.start, question.finish, question.type)
        self.__answer = answer

    @property
    def answer(self):
        return self.__answer


def main():
    order_count = input()
    order_list = list()
    i = 0
    while i < int(order_count):
        order_str = input()
        order_list.append(Order(*order_str.split(' ')))
        i += 1

    # составляем список вопросов
    question_count = input()
    question_list = list()
    i = 0
    while i < int(question_count):
        question_str = input()
        question_list.append(Question(*question_str.split(' ')))
        i += 1


    answer_list = []
    a_question_list : list[QuestionA]  = object_input(order_list, question_list)
    for i in range(len(a_question_list)):
        answer_list.append(a_question_list[i].answer)
    ans_str = " ".join(map(str, answer_list))
    print(ans_str)






def object_input(order_list, question_list):
    order_list_srt_by_start = order_list
    order_list_srt_by_finish = order_list.copy()

    order_list_srt_by_start.sort(key = cmp_to_key(compareByStart))
    order_list_srt_by_finish.sort(key = cmp_to_key(compareByFinish))
    triplPointForStart = TriplPoint()
    triplPointForStart.inxPointOne = int(len(order_list) / 10)
    triplPointForStart.inxValueOne = order_list_srt_by_start[triplPointForStart.inxPointOne].start
    triplPointForStart.inxPointTwo = triplPointForStart.inxPointOne * 2
    triplPointForStart.inxValueTwo = order_list_srt_by_start[triplPointForStart.inxPointTwo].start
    triplPointForStart.inxPointThree = triplPointForStart.inxPointOne * 3
    triplPointForStart.inxValueThree = order_list_srt_by_start[triplPointForStart.inxPointThree].start
    triplPointForStart.inxPoint4 = triplPointForStart.inxPointOne * 4
    triplPointForStart.inxValue4 = order_list_srt_by_start[triplPointForStart.inxPoint4].start
    triplPointForStart.inxPoint5 = triplPointForStart.inxPointOne * 5
    triplPointForStart.inxValue5 = order_list_srt_by_start[triplPointForStart.inxPoint5].start
    triplPointForStart.inxPoint6 = triplPointForStart.inxPointOne * 6
    triplPointForStart.inxValue6 = order_list_srt_by_start[triplPointForStart.inxPoint6].start
    triplPointForStart.inxPoint7 = triplPointForStart.inxPointOne * 7
    triplPointForStart.inxValue7 = order_list_srt_by_start[triplPointForStart.inxPoint7].start
    triplPointForStart.inxPoint8 = triplPointForStart.inxPointOne * 8
    triplPointForStart.inxValue8 = order_list_srt_by_start[triplPointForStart.inxPoint8].start
    triplPointForStart.inxPoint9 = triplPointForStart.inxPointOne * 9
    triplPointForStart.inxValue9 = order_list_srt_by_start[triplPointForStart.inxPoint9].start

    triplPointForFinish = TriplPoint()
    triplPointForFinish.inxPointOne = int(len(order_list) / 10)
    triplPointForFinish.inxValueOne = order_list_srt_by_finish[triplPointForFinish.inxPointOne].finish
    triplPointForFinish.inxPointTwo = triplPointForFinish.inxPointOne * 2
    triplPointForFinish.inxValueTwo = order_list_srt_by_finish[triplPointForFinish.inxPointTwo].finish
    triplPointForFinish.inxPointThree = triplPointForFinish.inxPointOne * 3
    triplPointForFinish.inxValueThree = order_list_srt_by_finish[triplPointForFinish.inxPointThree].finish
    triplPointForFinish.inxPoint4 = triplPointForStart.inxPointOne * 4
    triplPointForFinish.inxValue4 = order_list_srt_by_finish[triplPointForFinish.inxPoint4].finish
    triplPointForFinish.inxPoint5 = triplPointForStart.inxPointOne * 5
    triplPointForFinish.inxValue5 = order_list_srt_by_finish[triplPointForFinish.inxPoint5].finish
    triplPointForFinish.inxPoint6 = triplPointForStart.inxPointOne * 6
    triplPointForFinish.inxValue6 = order_list_srt_by_finish[triplPointForFinish.inxPoint6].finish
    triplPointForFinish.inxPoint7 = triplPointForStart.inxPointOne * 7
    triplPointForFinish.inxValue7 = order_list_srt_by_finish[triplPointForFinish.inxPoint7].finish
    triplPointForFinish.inxPoint8 = triplPointForStart.inxPointOne * 8
    triplPointForFinish.inxValue8 = order_list_srt_by_finish[triplPointForFinish.inxPoint8].finish
    triplPointForFinish.inxPoint9 = triplPointForStart.inxPointOne * 9
    triplPointForFinish.inxValue9 = order_list_srt_by_finish[triplPointForFinish.inxPoint9].finish

    qIndex = 0
    while qIndex < len(question_list):
        question_list[qIndex] = QuestionA(question_list[qIndex],
                                          findAnswerTypeOne(question_list[qIndex], order_list_srt_by_start, triplPointForStart)
                                          if question_list[qIndex].type == 1 else
                                          findAnswerTypeTwo(question_list[qIndex], order_list_srt_by_finish, triplPointForFinish))
        qIndex += 1

    return question_list



def compareByStart(order1, order2):
    if order1.start < order2.start:
        return -1
    else:
        return 1

def compareByFinish(order1, order2):
    if order1.finish < order2.finish:
        return -1
    else:
        return 1

def findAnswerTypeOne(question, order_list_srt_by_start, triplPointForStart):
    summCost = 0
    i = 0
    if question.start > triplPointForStart.inxValueOne:  i = triplPointForStart.inxPointOne
    if question.start > triplPointForStart.inxValueTwo:  i = triplPointForStart.inxPointTwo
    if question.start > triplPointForStart.inxValueThree:  i = triplPointForStart.inxPointThree
    if question.start > triplPointForStart.inxValue4:  i = triplPointForStart.inxPoint4
    if question.start > triplPointForStart.inxValue5:  i = triplPointForStart.inxPoint5
    if question.start > triplPointForStart.inxValue6:  i = triplPointForStart.inxPoint6
    if question.start > triplPointForStart.inxValue7:  i = triplPointForStart.inxPoint7
    if question.start > triplPointForStart.inxValue8:  i = triplPointForStart.inxPoint8
    if question.start > triplPointForStart.inxValue9:  i = triplPointForStart.inxPoint9
    while i < len(order_list_srt_by_start):
        if order_list_srt_by_start[i].start < question.start :
            i += 1
            continue
        if order_list_srt_by_start[i].start > question.finish :
            break
        summCost += order_list_srt_by_start[i].cost
        i += 1

    return summCost

def findAnswerTypeTwo(question, order_list_srt_by_finish, triplPointForFinish):
    summTime = 0
    i = 0
    if question.start > triplPointForFinish.inxValueOne:  i = triplPointForFinish.inxPointOne
    if question.start > triplPointForFinish.inxValueTwo:  i = triplPointForFinish.inxPointTwo
    if question.start > triplPointForFinish.inxValueThree:  i = triplPointForFinish.inxPointThree
    if question.start > triplPointForFinish.inxValue4:  i = triplPointForFinish.inxPoint4
    if question.start > triplPointForFinish.inxValue5:  i = triplPointForFinish.inxPoint5
    if question.start > triplPointForFinish.inxValue6:  i = triplPointForFinish.inxPoint6
    if question.start > triplPointForFinish.inxValue7:  i = triplPointForFinish.inxPoint7
    if question.start > triplPointForFinish.inxValue8:  i = triplPointForFinish.inxPoint8
    if question.start > triplPointForFinish.inxValue9:  i = triplPointForFinish.inxPoint9
    while i < len(order_list_srt_by_finish):
        if order_list_srt_by_finish[i].finish < question.start:
            i += 1
            continue
        if order_list_srt_by_finish[i].finish > question.finish:
            break
        summTime += order_list_srt_by_finish[i].finish - order_list_srt_by_finish[i].start
        i += 1
    return summTime

if __name__ == '__main__':
    main()


