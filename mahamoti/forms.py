from datetime import datetime
import inspect
import sys

import wtforms.ext.dateutil.fields
import wtforms.fields
import wtforms.form
import wtforms.validators

class BaseForm(wtforms.Form):
    name = "Override this in your forms"

    def to_dict(self):
        form_dict = {
            field.name: field.data if not isinstance(field.data, datetime) else str(field.data)
            for field in self
        }
        form_dict["name"] = self.name
        return form_dict

class TimestampedForm(BaseForm):
    time = wtforms.ext.dateutil.fields.DateTimeField(
        "Time",
        default=datetime.now(),
        validators=[wtforms.validators.Required()]
    )

class RunningForm(TimestampedForm):
    name = "Running"
    distance = wtforms.fields.FloatField("Distance", validators=[wtforms.validators.NumberRange(0)])

class TrumpetPlayingForm(TimestampedForm):
    name = "Trumpet"

def classes():
    return [
        obj for _name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass)
        if issubclass(obj, BaseForm) and obj.name != BaseForm.name
    ]

def get_class(name):
    for klass in classes():
        if klass.name == name:
            return klass

def instances(instance=None):
    return [
        klass() if instance is None or klass.name != instance.name else instance
        for klass in classes()
    ]
