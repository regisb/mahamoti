import wtforms.fields
import wtforms.form
import wtforms.validators

class TimestampedForm(wtforms.Form):
    time = wtforms.fields.DateTimeField("Time")

class RunningForm(TimestampedForm):
    distance = wtforms.fields.FloatField("Distance", validators=[wtforms.validators.NumberRange(0)])

def instances():
    return [
        RunningForm()
    ]
