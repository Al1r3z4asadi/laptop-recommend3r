
import mongoengine

mongoengine.connect('laptops')

class Product(mongoengine.DynamicDocument):

    title = mongoengine.StringField(max_length=240,required=True , primary_key=True)

    def __str__(self):
        return self.title

