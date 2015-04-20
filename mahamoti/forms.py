from datetime import datetime
import wtforms.ext.dateutil.fields
import wtforms.fields
import wtforms.form
import wtforms.validators

class BaseForm(wtforms.Form):
    name = "Override this in your forms"

class TimestampedForm(wtforms.Form):
    time = wtforms.ext.dateutil.fields.DateTimeField(
        "Time",
        default=datetime.now(),
        validators=[wtforms.validators.Required()]
    )

class RunningForm(TimestampedForm):
    name = "Running"
    distance = wtforms.fields.FloatField("Distance", validators=[wtforms.validators.NumberRange(0)])

def classes():
    return [
        RunningForm,
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
