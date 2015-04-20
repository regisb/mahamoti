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

def instances():
    return [
        RunningForm()
    ]
