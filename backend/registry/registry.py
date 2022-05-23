class ModelRegistryBase(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        # instantiate a new type corresponding to the type of class being defined
        # this is currently RegisterBase but in child classes will be the child class
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(msc):
        return dict(msc.REGISTRY)


class ModelBaseClass(metaclass=ModelRegistryBase):
    pass


class SVM_GLOVE(ModelBaseClass, SVM):
    def __init__(self, *args, **kwargs):
        pass

class S(ModelBaseClass):
    def __init__(self, *args, **kwargs):
        pass


class ModelFactory():
    models = {} # From abel to Instance

    @classmethod
    def get_model(cls, label):

        if label not in ModelFactory.models:
            registry = ModelRegistryBase.get_registry()
            ModelFactory.models[label] = registry[label]()  # Create an object of the corresponding class

        return ModelFactory.models[label]


print(ModelFactory.get_model('Model_A'))
print(ModelFactory.get_model('Model_B'))
print(ModelFactory.get_model('Model_A'))

