from modeltranslation.translator import translator, TranslationOptions
from stadium.models import FieldsModel, BronModel

class FieldsTranslationOptions(TranslationOptions):
    fields = ('field_name', 'field_adress')


translator.register(FieldsModel, FieldsTranslationOptions)