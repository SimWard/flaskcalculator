from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class CalculatorForm(FlaskForm):
    myFunction = StringField('Input basic calculation',
                             validators=[DataRequired()])
    submit = SubmitField('Calculate!')

    def validate_myFunction(self, myFunction):
        try:
            eval(myFunction.data)
            problem = None
        except:
            problem = True
        if problem:
            raise ValidationError('Invalid input data. Please try again.')
