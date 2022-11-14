
class File:
    def __init__(self):
        pass
    def get_data(self):
        fileName = 'input.txt'
        response = open(fileName, 'r')
        dataSource = []
        for text in response:
            dataSource.append(text.replace('\n', ''))
        return dataSource 
        #return list of all data in text file 
        #Example ['create_hotel 2 3', 'book 203 Thor 32', 'book 101 PeterParker 16']


            