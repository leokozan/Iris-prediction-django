from app_iris.models import IrisModel

class IrisValidations:

    def __init__(self):
        self.__sepal_length = 0.0
        self.__sepal_width = 0.0
        self.__petal_length = 0.0
        self.__petal_width = 0.0
        self.__specie = ''

    def set_sepal_length(self, sepal_length):
        if sepal_length <= 0:
            raise ValueError('sepal_length deve ser um valor maior do que zero')
        self.__sepal_length = sepal_length

    def set_sepal_width(self, sepal_width):
        if sepal_width <= 0:
            raise ValueError('sepal_width deve ser um valor maior do que zero')
        self.__sepal_width = sepal_width

    def set_petal_length(self, petal_length):
        if petal_length <= 0:
            raise ValueError('petal_length deve ser um valor maior do que zero')
        self.__petal_length = petal_length

    def set_petal_width(self, petal_width):
        if petal_width <= 0:
            raise ValueError('petal_width deve ser um valor maior do que zero')
        self.__petal_width = petal_width

    def set_specie(self, specie):
        if not specie in ['setosa', 'versicolor', 'virginica']:
            raise ValueError(f'specie deve ser setosa, versicolor ou virginica ({specie}).')
        self.__specie = specie

    def to_model(self):
        iris = IrisModel()
        iris.sepal_length = self.__sepal_length
        iris.sepal_width = self.__sepal_width
        iris.petal_length = self.__petal_length
        iris.petal_width = self.__petal_width
        iris.specie = self.__specie
        return iris