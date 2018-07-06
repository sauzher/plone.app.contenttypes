# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IRichTextMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IRichText(model.Schema):

    text = RichTextField(
        title=_(u'Text'),
        description=u'',
        required=False,
    )
    form.widget('text', RichTextFieldWidget)
    model.primary('text')


@implementer(IRichText)
@adapter(IDexterityContent)
class RichText(object):

    def __init__(self, context):
        self.context = context

    @property
    def text(self):
        return self.context.text

    @text.setter
    def text(self, value):
        self.context.text = value


class WidgetView(WidgetsView):
    schema = IRichText
